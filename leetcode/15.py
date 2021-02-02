#09.세 수의 합

def sum(nums):
    result = []
    length = len(nums)
    nums.sort()

    for i in range(length - 2):
        # 중복된 값은 건너뛰게 함
        if (i > 0) and (nums[i] == nums[i - 1]):
            continue

        left, right = i + 1, length - 1

        while (left < right):
            sum = nums[i] + nums[left] + nums[right]

            if (sum < 0):
                left += 1

            elif (sum > 0):
                right -= 1

            else:
                result.append([nums[i], nums[left], nums[right]])

                # 합이 0이지만 중복을 가지면 스킵
                while (left < right and nums[left] == nums[left + 1]):
                    left += 1
                while (left < right and nums[right] == nums[right - 1]):
                    right -= 1

                left += 1
                right -= 1

    return result

print(sum([0]))