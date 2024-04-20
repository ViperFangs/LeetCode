""" 
Author: Aarya
Description: We are playing the Guess Game. The game is as follows:
  I pick a number from 1 to n. You have to guess which number I picked.
  Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
  You call a pre-defined API int guess(int num). Return the number that I picked.
Time Complexity: O(log(n)), This approach uses a binary search algorithm which takes log(n) time.
Space Complexity: O(1), This approach uses a few pointers to keep track of the guess. Doesn't grow with the input.
Logic: 
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# This Python class implements a binary search algorithm to guess a number within a given range.
class Solution:
    """
      This function uses binary search to guess a number within a given range by making comparisons
      with a target number.
      
      :param n: represents the upper bound of the range within which the number is to be guessed.
      The algorithm uses the `guess()` function to determine whether the guessed number
      is too high, too low or the correct guess

      :return: the number picked by the `guess()` API
      """
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            current_guess = guess(mid)

            if current_guess == 0:
                return mid
            elif current_guess == -1:
                high = mid - 1
            else:
                low = mid + 1