#타겟 넘버
#https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    def dfs(index,total):
        if len(numbers)==index:
            if total==target:
                return 1
            return 0
        
        ret = 0

        #뺄셈
        ret += dfs(index+1,total+numbers[index])
        #덧셈
        ret += dfs(index+1,total-numbers[index])
        return ret
    
    return dfs(0,0)