def solution(participant, completion):
    for p in range(len(participant)):
        for c in range(len(completion)):
            if participant[p] == completion[c]:
                participant[p] = 1
                completion[c] = None

    for i in range(len(completion)):
        participant.remove(1)

    answer = '' + str(participant)
    return answer


print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))

