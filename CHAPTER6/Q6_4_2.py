import math
def gen_prime1(x=2):
    while True:
        for i in range(2, int(math.sort(x))+1):
            if x % i == 0:
                break
            else:
                yield x
            x += 1
