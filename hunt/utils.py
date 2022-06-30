import re

def match_answer(actual_answer, submitted_answer):
    submitted_answer_filtered = re.sub('[\W_]+', '', submitted_answer.lower().replace(' ', '').strip())
    return submitted_answer_filtered == actual_answer