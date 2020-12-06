input = [x for x in open('input.txt', 'r').read().split("\n\n")]


def get_unique_answers(data):
    answers = []
    persons = data.splitlines()
    for person in persons:
        for answer in person:
            if answer not in answers:
                answers.append(answer)
    return len(answers)


n = sum([get_unique_answers(x) for x in input])
print(n)
