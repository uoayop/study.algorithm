#전화번호 목록

def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    print(phoneBook)

    for p1, p2 in zip(phoneBook[:-1], phoneBook[1:]):
        print("phoneBook[:-1]",phoneBook[:-1])
        print("phoneBook[1:]",phoneBook[1:])

        print(len(p1),len(p2))
        print(p1,p2)
        if p2.startswith(p1):
            return False
    return True

print(solution(["111213", "12", "1112"]))
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))

# def solution(phone_book):
#     answer = True
    
#     while len(phone_book)!=1:
#         #print(phone_book)
#         freqs={}
#         min_length=len(phone_book[0])
#         min_phone=phone_book[0]
#         for phone in phone_book:
#             if (len(phone)<min_length):
#                 min_length=len(phone)
#                 min_phone=phone
#         #print("min_length",min_length,"min_phone",min_phone)
                
#         for phone in phone_book:
#             edit_phone = phone[0:min_length]
#             #print("edit_phone",edit_phone)
#             if edit_phone not in freqs:
#                 freqs[edit_phone] = 1
#             else:
#                 freqs[edit_phone] += 1
#             #print("edit_phone",phone_book)

#         phone_book.remove(min_phone)
#         #print("remove",phone_book)
            
#         for result in freqs:
#             if freqs[result]>1:
#                 answer=False
#                 break
        
#     return answer

