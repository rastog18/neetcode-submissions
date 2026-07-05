class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        numbers = []
        for i in tokens:
            print(numbers)
            if i in ["+", "-", "/", "*"]:
                i1 = numbers.pop()
                i2 = numbers.pop()
                if i == "+":
                    i2 += i1
                elif i == "-":
                    i2 -= i1
                elif i == "/":
                    i2 /= i1
                    if i2 < 0:
                        i2 = math.ceil(i2)
                    else:
                        i2 = math.floor(i2)
                else:
                    i2 *= i1
                numbers.append(i2)
            else:
                numbers.append(int(i))

        return numbers[-1]