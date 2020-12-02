input = [x for x in open('input.txt', 'r').read().splitlines()]


def parse_policy(data):
    args = data.split(" ")
    (bounds, letter, pwd) = ((int(args[0].split("-")[0])-1,
                              int(args[0].split("-")[1])-1), args[1][:1], args[2])
    return {
        "positions": bounds,
        "letter": letter,
        "pwd": pwd
    }


def check_pwd(data):
    policy = parse_policy(data)
    if(policy["pwd"][policy["positions"][0]] == policy["letter"]) ^ (policy["pwd"][policy["positions"][1]] == policy["letter"]):
        return True
    else:
        return False


i = 0
for pwd in input:
    if check_pwd(pwd):
        i += 1
print(i)
