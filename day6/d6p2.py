input = [x for x in open('input.txt', 'r').read().split("\n\n")]


def get_common_answers(data):
    answers = []
    persons = data.splitlines()
    for person in persons:
        for answer in person:
            if answer not in answers and data.count(answer) == len(persons):
                answers.append(answer)
    return len(answers)


n = sum([get_common_answers(x) for x in input])
print(n)
