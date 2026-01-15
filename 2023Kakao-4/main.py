def decimalToBinary(number):
    ret = ""
    while number:
        ret += f"{number % 2}"
        number //= 2
    return ret[::-1]

def makeBinaryToTree(b):
    c = len(b)
    for i in range(2, 100):
        l = 2 ** (i - 1) - 1
        if c <= l:
            return ("0" * l + b)[-l:]

def check(binaryTree, mustZero):
    if len(binaryTree) == 1:
        if binaryTree[0] == "1" and mustZero: return 0
        return 1

    root = binaryTree[len(binaryTree) // 2]

    if root == "1" and mustZero:
        return 0

    if root == "1":
        return min(
            check(binaryTree[:len(binaryTree) // 2], False),
            check(binaryTree[len(binaryTree) // 2 + 1:], False)
        )
    else:
        return min(
            check(binaryTree[:len(binaryTree) // 2], True),
            check(binaryTree[len(binaryTree) // 2 + 1:], True)
        )

def solution(numbers):
    answer = []
    binary = [
        check(
            makeBinaryToTree(
                decimalToBinary(number)
            ),
        False)
        for number in numbers
    ]

    return binary



print(solution(
    [63, 111, 95]
))