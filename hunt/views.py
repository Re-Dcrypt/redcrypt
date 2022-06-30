from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from hunt.models import Question
from accounts.models import Profile
from hunt.utils import match_answer
# Create your views here.


def index(request):
    return render(request, 'base.html')


def offline(request):
    return render(request, 'offline.html')


@login_required
def play(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    question = Question.objects.get(level=profile.current_level)
    return render(request, 'play.html', {'question': question})


@login_required
def check_ans(request):
    if request.method == "POST":
        user = request.user
        profile = Profile.objects.get(user=user)
        question = Question.objects.get(level=profile.current_level)
        if match_answer(question.answer, request.POST['answer']):
            print("Correct")
            profile.current_level += 1
            profile.score += question.points
            profile.save()
            return JsonResponse({'correct': True}, status=200)
        else:
            return JsonResponse({'correct': False}, status=400)
