class Solution:
    def isValid(self, s: str) -> bool:
        # we are considering two types of parentheisis openers and closers
        # if we encounter an opener, we push to the stack, if we encounter
        # a closer we pop from the stack and compare if it is equal to closer
        # we also return fasle if stack has items left, at the end of traversal.
        stack = []
        type1 = ["(", "{", "["]
        adjList = {"}": "{", "]":"[", ")":"("}
        for i in s:
            if i in type1:
                stack.append(i)
            else:
                if len(stack) == 0 or stack.pop() != adjList[i]:
                    return False
        if stack:
            return False
        return True
        
        # type2 = {")" : 0, "}": 1, "]": 2}

        # if len(s) % 2 != 0:
        #     return False
    
        # for i in s:
        #     if i in type1:
        #         stack.append(i)
        #     else:
        #         if stack:
        #             itemPopped = stack.pop()
        #             if type1[type2[i]] != itemPopped:
        #                 return False
        #         else:
        #             return False

        # if stack != []:
        #     return False
        # return True


        