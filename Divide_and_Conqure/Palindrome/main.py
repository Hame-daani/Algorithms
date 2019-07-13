def isPalindrome(s):
    """
    Recursive algorithm.\n
    T(n) = O(n)
    """
    def toChars(s):
        s = s.lower()
        r = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                r = r + c
        return r

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    # main func
    return isPal(toChars(s))

if __name__ == "__main__":
    print("Does 'abcba' Palindrome?",isPalindrome("abcba"))
    print("Does 'abcdba' Palindrome?",isPalindrome("abcdba"))