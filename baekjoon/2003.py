# 수들의 합2
# 투포인터
# https://www.acmicpc.net/problem/2003

# i번째 수부터 j번째 수까지의 합이 m이 되는 경우의 수를 구해라

n, m = map(int,input().rsplit())
nums = list(map(int,input().rsplit()))

l, r = 0, 0
answer, hap = 0, 0

# l을 차례대로 증가시키며 반복
for l in range(n):
    # r을 가능한만큼 움직이기
    while hap < m and r < n:
        hap += nums[r]
        r += 1
    # 부분 합이 m일 때 카운트 증가
    if hap == m:
        answer += 1
    # m보다 hap이 크거나 같으므로 l 한칸 이동 
    hap -= nums[l]

print(answer)