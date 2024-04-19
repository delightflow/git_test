def chech_available():
    return 'It works'

def remov_odd(nums = [1,2,3,4]):
    return [num for num in nums if num%2 == 0]

if __name__ == '__main__':
    print(remov_odd())



