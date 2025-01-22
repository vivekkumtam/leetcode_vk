class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub(r'[^a-zA-Z0-9]', '', s)
        string = string.lower()

        if (string == string[::-1]):
            return True
        else:
            return False