class Solution:

    """
    Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward
    """


    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            new_list = [int(i) for i in str(x)]
            for i in new_list:
                if new_list[-1::-1] == new_list[0::1]:
                    return True;
                else:
                    return False

    """
Runtime 80ms
Time complexity is O(3n)=O(n) as we iterate through int to create the list as well as iterate through the list twice (forwards and backwards) to check if its a palindrome
    """
