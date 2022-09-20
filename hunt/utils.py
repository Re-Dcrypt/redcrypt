import re
import pyminizip
import os
from accounts.models import Profile
from discord_webhook import DiscordWebhook

def simplify(text):
	import unicodedata
	text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
	return str(text)

def match_answer(actual_answer, submitted_answer):
    submitted_answer = simplify(submitted_answer)
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


def update_rank_all():
    for profile in Profile.objects.all():
        profile.rank = get_rank(profile.user)
        profile.save()


def update_rank(user):
    user_profile = Profile.objects.get(user=user)
    user_profile.rank = get_rank(user)
    user_profile.save()


def backup_db():
	inpt = "db.sqlite3"
	oupt = "db.zip"
	pwd = os.getenv('PWD_zip')
	webhook_url = os.getenv('Discord_backup_webhook')
	pyminizip.compress(
		inpt,
		None,
		oupt,
        pwd,1)
	webhook = DiscordWebhook(url=webhook_url, rate_limit_retry=True)
	with open("db.zip", "rb") as f:
	    webhook.add_file(file=f.read(), filename='db.zip')	
	webhook.execute()
