# =================================================================================
#
# Script used for experimenting with code without interfering with project scripts
#
# =================================================================================


def tahmid(*args):
    total = 0
    for a in args:
        total += a
    return total


print(tahmid(1, "string"))
print(tahmid(10, 20, 30, 50))
