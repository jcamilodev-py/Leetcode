from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            match i:
                case "+":
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n1 + n2)
                case "-":
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n2 - n1)
                
                case "/":
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(int(n2 / n1))
                
                case "*":
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n1 * n2)
                
                case _:
                    stack.append(int(i))

        return stack[0]


s = Solution()
print(s.evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]))