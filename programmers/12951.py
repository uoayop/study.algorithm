def solution(s):
    answer = []
    words = s.lower()

    # print(words)

    # for i in range(words):
        

    for word in words:
        if (word[0].isalpha()):
            word = chr(ord(word[0])-32) + word[1:]
        answer.append(word)
   
    return ''.join(answer)

# print(solution(" A  sdf Fft "))
# print(solution("          t "))
# print(solution("3people unFollowed me"))
# print(solution("for the last week"))


# def solution(s):
#     answer = []
#     words = list(map(str,s.lower().split()))
#     for word in words:
#         if (word[0].isalpha()):
#             word = chr(ord(word[0])-32) + word[1:]
#         answer.append(word)
   
#     return ' '.join(answer)

# print(solution(" A  sdf Fft "))

a = None
print(type(a))