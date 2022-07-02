from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from hunt.decorators import hunt_status
from hunt.models import AdditionalHint, Question, LevelTracking, AnswerAttempt
from accounts.models import Profile
from hunt.utils import match_answer
# Create your views here.


def index(request):
    return render(request, 'base.html')


def offline(request):
    return render(request, 'offline.html')


@login_required
@hunt_status
def play(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    question = Question.objects.get(level=profile.current_level)
    additionalhints = AdditionalHint.objects.filter(question=question)
    return render(request, 'play.html', {
        'question': question,
        'additionalhints': additionalhints})


@login_required
@hunt_status
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
            print('answer attempt error', e)
        if match_answer(question.answer, answer):
            profile.current_level += 1
            profile.score += question.points
            profile.save()
            try:
                LevelTracking.objects.create(
                    user=request.user,
                    level=profile.current_level)
            except Exception as e:
                print('Level completion tracking exception', e)
            return JsonResponse({'correct': True}, status=200)
        else:
            return JsonResponse({'correct': False}, status=400)


def leaderboard(request):
    profiles = Profile.objects.all().order_by('-score', 'last_completed_time')
    return render(request, 'leaderboard.html', {'players': profiles})
