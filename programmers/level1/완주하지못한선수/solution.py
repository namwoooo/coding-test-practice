from collections import Counter

def solution(participant, completion):
  
  participant_counter = Counter(participant)
  completion_counter = Counter(completion)

  answer = ', '.join((participant_counter - completion_counter).keys())

  return answer 