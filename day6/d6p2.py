input = [x for x in open('input.txt', 'r').read().strip().split("\n\n")]


def get_common_answers(data):
    answers = set()
    persons = data.splitlines()
    for person in persons:
        for answer in person:
            if data.count(answer) == len(persons):
                answers.add(answer)
    return len(answers)


n = sum([get_common_answers(x) for x in input])
print(n)
