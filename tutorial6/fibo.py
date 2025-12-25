# フィボナッチ数のモジュール

def fib(n):
    """nまでのフィボナッチ数を出力する"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """nまでのフィボナッチ数を返す"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
