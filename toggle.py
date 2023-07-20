class LongestPalindromeString:
    @staticmethod
    def intermediate_palindrome(n, left, right):
        if left > right:
            return None
        while left >= 0 and right < len(n) and n[left] == n[right]:
            left -= 1
            right += 1
        return n[left + 1:right]

    @staticmethod
    def longest_palindrome_string(n):
        longest = n[0]
        for i in range(len(n) - 1):
            palindrome = LongestPalindromeString.intermediate_palindrome(n, i, i)
            if len(palindrome) > len(longest):
                longest = palindrome
            palindrome = LongestPalindromeString.intermediate_palindrome(n, i, i + 1)
            if len(palindrome) > len(longest):
                longest = palindrome
        return longest

print(LongestPalindromeString.longest_palindrome_string("aaaabaaa"))
print(LongestPalindromeString.longest_palindrome_string("abba"))
