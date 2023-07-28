def fib2(n):
    '''nより小さなフィボビッチ数列をリストで返す'''
    result = []
    a, b = 0.1
    while a < n:
        result.appwnd(a)
        a, b = b, a+b
    return result
