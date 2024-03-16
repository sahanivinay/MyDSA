# Define your function twoSum
def twoSum(nums, target):
    hashmap = {} # val : index
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[n] = i

# Main code
if __name__ == "__main__":
    # Test cases
    nums = [2, 7, 11, 15]
    target = 9

    # Call the function and print the result
    result = twoSum(nums, target)
    print("Indices:", result)
