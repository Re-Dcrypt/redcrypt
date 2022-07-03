import re
from accounts.models import Profile


def match_answer(actual_answer, submitted_answer):
    submitted_answer_filtered = re.sub('[\W_]+', '', submitted_answer.lower().replace(' ', '').strip())
    return submitted_answer_filtered == actual_answer


def get_rank(user):
    user_profile = Profile.objects.get(user=user)
    if user_profile.is_banned:
        return '☠'
    elif user_profile.user.is_staff:
        return '🛡'
    else:
        above_players = Profile.objects.filter(score__gt=user_profile.score).exclude(is_banned=True).exclude(user__is_staff=True) | Profile.objects.filter(score=user_profile.score, last_completed_time__lt=user_profile.last_completed_time).exclude(is_banned=True).exclude(user__is_staff=True)
        above = above_players.count()
        return above+1
