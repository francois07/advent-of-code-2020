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
    return (policy["pwd"][policy["positions"][0]] == policy["letter"]) ^ (policy["pwd"][policy["positions"][1]] == policy["letter"])


n = [check_pwd(pwd) for pwd in input].count(True)
print(n)
