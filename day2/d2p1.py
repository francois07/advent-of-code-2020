input = [x for x in open('input.txt', 'r').read().splitlines()]


def parse_policy(data):
    args = data.split(" ")
    (bounds, letter, pwd) = ((int(args[0].split("-")[0]),
                              int(args[0].split("-")[1])), args[1][:1], args[2])
    return {
        "bounds": bounds,
        "letter": letter,
        "pwd": pwd
    }


def check_pwd(data):
    policy = parse_policy(data)
    nb_occurences = policy["pwd"].count(policy["letter"])
    return policy["bounds"][0] <= nb_occurences <= policy["bounds"][1]


n = [check_pwd(pwd) for pwd in input].count(True)
print(n)
