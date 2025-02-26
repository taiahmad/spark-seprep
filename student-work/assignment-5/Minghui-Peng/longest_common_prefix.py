def longest_common_prefix(strs):
    """
    Finds the longest common prefix string among an array of strings.
    If there is no common prefix, returns an empty string "".
    """
    if not strs:
        return ""
    
    # Start with the first string as the prefix.
    prefix = strs[0]
    
    # Compare with each subsequent string.
    for s in strs[1:]:
        # Reduce the prefix until it matches the start of s.
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Test cases
if __name__ == "__main__":
    input_list = ["flower", "flow", "flight"]
    result = longest_common_prefix(input_list)
    print(f"Longest common prefix for {input_list}: '{result}'")
