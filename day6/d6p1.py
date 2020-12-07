input = [x for x in open('input.txt', 'r').read().strip().split("\n\n")]


def get_unique_answers(data):
    answers = set()
    persons = data.splitlines()
    for person in persons:
        for answer in person:
            answers.add(answer)
    return len(answers)


n = sum([get_unique_answers(x) for x in input])
print(n)
