from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from hunt.decorators import hunt_status, not_banned
from hunt.models import AdditionalHint, Question
from hunt.models import LevelTracking, AnswerAttempt, SampleQuestion
from accounts.models import Profile
from hunt.utils import match_answer, get_rank
from sentry_sdk import capture_exception
# Create your views here.


def index(request):
    return render(request, 'base.html')


def offline(request):
    return render(request, 'offline.html')


@hunt_status
@login_required
@not_banned
def play(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.current_level > 1:
        return render(request, 'complete.html')
    else:
        question = Question.objects.get(level=profile.current_level)
        additionalhints = AdditionalHint.objects.filter(question=question)
        return render(request, 'play.html', {
            'question': question,
            'additionalhints': additionalhints,
            'url_name': 'play'})


@hunt_status
@login_required
def check_ans(request):
    if request.method == "POST":
        user = request.user
        profile = Profile.objects.get(user=user)
        question = Question.objects.get(level=profile.current_level)
        answer = request.POST['answer']
        try:
            AnswerAttempt.objects.create(
                user=request.user,
                level=profile.current_level,
                answer=answer)
        except Exception as e:
            capture_exception(e)
        try:
            profile.stats[str(question.level)] += 1
        except KeyError:
            profile.stats[str(question.level)] = 1
        except Exception as e:
            capture_exception(e)
        if match_answer(question.answer, answer):
            profile.current_level += 1
            profile.score += question.points
            profile.save()
            try:
                LevelTracking.objects.create(
                    user=request.user,
                    level=profile.current_level)
            except Exception as e:
                capture_exception(e)
            return JsonResponse({'correct': True}, status=200)
        else:
            profile.save()
            return JsonResponse({'correct': False}, status=200)


def leaderboard(request):
    staff = Profile.objects.filter(
        user__is_staff=True).order_by(
            '-score',
            'last_completed_time')
    profiles = Profile.objects.all().exclude(
        is_banned=True).exclude(
            user__is_staff=True).order_by(
                '-score',
                'last_completed_time')
    banned = Profile.objects.filter(
        is_banned=True).order_by(
            'last_completed_time')
    if request.user.is_authenticated:
        rank = get_rank(request.user)
    else:
        rank = 'unauthorised'
    return render(request, 'leaderboard.html', {
        'staff': staff,
        'players': profiles,
        'rank': rank,
        'banned': banned,
        'url_name': 'leaderboard'})


def faqs(request):
    return render(request, 'faqs.html', {'url_name': 'faqs'})


def rules(request):
    return render(request, 'rules.html', {'url_name': 'rules'})


def about(request):
    return render(request, 'about.html', {'url_name': 'about'})


@login_required
def sample_questions_play(request):
    user = request.user
    sample_questions = SampleQuestion.objects.all()
    if len(sample_questions) == 0:
        return render(
            request,
            'shortner.html',
            {
                'content': "No sample questions available",
                'urlname': "Sample"})
    for i in sample_questions:
        print(i)
        if user in i.completed_by.all():
            pass
            print("here")
        else:
            return render(
                request,
                'sample_questions.html',
                {'question': i})
        return render(
            request,
            'shortner.html',
            {
                'content': "You have completed all sample questions",
                'urlname': "Sample"})


@login_required
def sample_checkans(request):
    if request.method == "POST":
        user = request.user
        sample_question = SampleQuestion.objects.get(
            level=request.POST['level'])
        answer = request.POST['answer']
        if match_answer(sample_question.answer, answer):
            sample_question.completed_by.add(user)
            sample_question.save()
            return JsonResponse({'correct': True}, status=200)
        else:
            return JsonResponse({'correct': False}, status=400)
