# Approach:
# - We use the **sliding window (two-pointer)** technique to find the longest subarray containing at most `k` flipped zeros.
# - The **left pointer** moves only when we have flipped more than `k` zeros.
# - The **right pointer** expands the window while counting zeros.
# - The goal is to maximize the window size while ensuring the number of flipped zeros does not exceed `k`.

# Time Complexity: O(N) - Each element is processed at most twice (once by left and once by right).
# Space Complexity: O(1) - We use a few extra variables.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0  # Left pointer of the sliding window
        max_length = 0  # Stores the maximum number of consecutive 1s
        zero_count = 0  # Tracks the number of flipped zeros

        for right in range(len(nums)):  # Expand the right pointer
            if nums[right] == 0:
                zero_count += 1  # Count zero to flip

            # If zeros exceed k, move the left pointer to reduce zero count
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1  # Reduce zero count when moving left
                left += 1  # Shrink the window from the left

            max_length = max(max_length, right - left + 1)  # Update max length

        return max_length  # Return the longest subarray found

# Example cases
solution = Solution()
print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # Output: 6
print(solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))  # Output: 10
