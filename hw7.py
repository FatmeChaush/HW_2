def count_substrings(haystack, needle):
    count = 0
    needle_length = len(needle)
    haystack_length = len(haystack)
    i = 0

    for i in range ( haystack_length - needle_length + 1):
        if haystack[i:i + needle_length] == needle:
            count += 1
            i += needle_length
        else:
            i += 1

    return count
print(count_substrings("This is a test string", "is"))
