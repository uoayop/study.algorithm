#주식 가격

from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    while (prices):
        count = 0
        #가장 앞에 있는 주식가격 pop
        price = prices.popleft()

        #이외의 나머지 주식들과 가격 비교
        for compare in prices:
            # 비교했을 때 pop했던 주식보다 가격이 높으면
            if compare >= price : 
                #가격이 떨어지지 않았으니까 +1
                count += 1
            # 비교했을 때 pop했던 주식보다 가격이 낮으면
            else: 
                #가격이 떨어졌으니까 +1 해주고 break
                count += 1
                break

        answer.append(count)
            
    return answer

# def solution(prices):
#     answer = []
#     prices = deque(prices)

#     while (prices):
#         min_price = min(prices)
#         #min()은 O(n)이라 while문 안에 함께 쓰면 O(n^2)으로 시간 초과 발생
#         price = prices.popleft()

#         if (price == min_price):
#             answer.append(len(prices))
#         else:
#             if (prices):
#                 n_price = prices.popleft()
#                 if (price > n_price):
#                     answer.append(1)
#                     prices.appendleft(n_price)
#                 else:
#                     prices.appendleft(n_price)
#                     answer.append(len(prices))
        
#     return answer


print(solution([1,2,3,2,3]))
print(solution([1, 2, 3, 2, 3, 1])) #5 4 1 2 1 0