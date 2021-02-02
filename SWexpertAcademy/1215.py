# [S/W 문제해결 기본] 3일차 - 회문1

#8x8 평면 글자판에서 가로,세로를 모두 보아 제시된 길이를 가진 회문의 총 개수를 구하는 문제
#A,B,C 중 하나

def find_palindrome(str,length):
    start_point=0
    cnt=0

    while(start_point<=8-length):
        end_point = start_point + length

        if (start_point - 1 < 0):
            if (str[start_point:end_point] == str[end_point - 1::-1]):
                cnt+=1
        else:
            if (str[start_point:end_point] == str[end_point - 1:start_point - 1:-1]):
                cnt+=1
        start_point += 1
    return cnt

for temp in range(10):
    matrix=[]
    column=[]
    find_length=int(input())
    palindrome_cnt=0


    for i in range(8):
        row=input()
        matrix.append(row)
        palindrome_cnt+=find_palindrome(row,find_length)

    for col in zip(*matrix):
        result=""
        result+="".join(col)
        column.append(result)


    for col in column:
        palindrome_cnt+=find_palindrome(col,find_length)

    print("#{} {}".format(temp+1,palindrome_cnt))