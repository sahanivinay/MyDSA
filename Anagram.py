def isAnagram(s: str, t: str) -> bool:
    # If lengths are different, they can't be anagrams
    if len(s) != len(t):
        return False
    
    # Sort both strings
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    
    # Compare sorted strings
    return sorted_s == sorted_t

# Test cases
print(isAnagram("listen", "silent"))  # Output: True
print(isAnagram("hello", "world"))    # Output: False
