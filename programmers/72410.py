def one(new_id):
    return new_id.lower()

def two(new_id):
    new=''
    for char in new_id:
        if char.isalnum() or char=='-' or char=='_'or char=='.':
            new+=char
        else:
            pass
    
    return new

def three(new_id):
    check=new_id[0]
    new=check
    for i in range(1,len(new_id)):
        if check=='.' and new_id[i]==check:
            new_id.replace(check,'')
        else:
            new+=new_id[i]
        check=new_id[i]
    return new

def four(new_id):
    if new_id=='': return ''
    if len(new_id)==1 and new_id[0]=='.': return ''
    while (new_id[0]=='.' or new_id[-1]=='.') and new_id:
        if new_id[0]=='.':
            new_id=new_id[1:]
        if new_id[-1]=='.':
            new_id=new_id[:-1]

    return new_id
        
def five(new_id):
    if new_id=='':
        new_id='a'
    return new_id
        
def six(new_id):
    if len(new_id)>15:
        new_id=new_id[:15]
        if (new_id[-1]=='.'):
            new_id=new_id[:-1]
    return new_id

def seven(new_id):
    while len(new_id)<3:
        new_id+=new_id[-1]
    return new_id


def solution(new_id):
    answer = seven(six(five(four(three(two(one(new_id)))))))
    
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
#print(solution("z-+.^."))
#print(solution("=.="))