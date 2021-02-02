def solution(s):
    strings = list(map(str,s.split(" ")))
    answer = []

    for string in strings:
        # for i in range(len(string)):
        #     print(i,"before",string[i],end=" ")
        string = "".join([x.upper() if j % 2 == 0 else x.lower() for j, x in enumerate(string)])
        answer.append(string)

    return " ".join(answer)
            # if (i%2==0):
            #     string[i].upper()
            #     print(i,"upper after",string[i])
            # else:
            #     string[i].lower()
            #     print(i,"lower after",string[i])
    


print(solution("try hello world"))