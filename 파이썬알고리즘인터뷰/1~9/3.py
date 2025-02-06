#p3 : sort Log according to given rules.

# using string.split()
# using string.isdigit()
# using list.sort(lambda)
# 2 conditions in lambda

def reorderLogFile(logs:list[str])->list[str]:
    letters = []
    digits = []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits

