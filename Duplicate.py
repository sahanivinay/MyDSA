# Define your function containsDuplicate
def containsDuplicate(nums):
    hashmap = set()
    for n in nums:
        if n in hashmap:
            return True
        hashmap.add(n)
    return False

# Main code
if __name__ == "__main__":
    # Test cases
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, 2, 3, 4, 5, 1]

    # Test the function
    print("nums1 contains duplicate:", containsDuplicate(nums1))
    print("nums2 contains duplicate:", containsDuplicate(nums2))
