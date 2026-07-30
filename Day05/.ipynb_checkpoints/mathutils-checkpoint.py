def average(nums):
    if not nums :
        return 0
    return sum(nums) / len(nums)

def biggest(nums):
    if not nums :
        return None
    return max(nums)

def is_prime(n) :
    if n <= 1 :
        return False

    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0:
            return False
    return True

print(average([10, 20, 30]))
print(biggest([10, 20, 30]))
print(is_prime(12))
print(is_prime(13))