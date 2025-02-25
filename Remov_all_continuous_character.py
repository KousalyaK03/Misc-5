# Approach:
# - We use a **stack** to efficiently track character sequences and their counts.
# - As we iterate through the string, we maintain a **stack of (char, count)**.
# - If the current character matches the top of the stack, we increment its count.
# - If a character’s count exceeds 2, we remove it completely from the stack.
# - At the end, we reconstruct the modified string from the stack.

# Time Complexity: O(N) - Each character is processed once.
# Space Complexity: O(N) - Stack stores characters in the worst case.

class Solution:
    def removeContinuousChars(self, s: str) -> str:
        stack = []  # Stack to store (char, count) tuples

        for char in s:
            # If the stack is not empty and the top character matches the current character
            if stack and stack[-1][0] == char:
                stack[-1] = (char, stack[-1][1] + 1)  # Increment count
                if stack[-1][1] > 2:  
                    stack.pop()  # Remove completely if count exceeds 2
            else:
                stack.append((char, 1))  # Add new character to stack

        # Reconstruct the result string
        return ''.join(char * count for char, count in stack)

# Example cases
solution = Solution()
print(solution.removeContinuousChars("abba"))       # Output: "abba"
print(solution.removeContinuousChars("abbb"))       # Output: "a"
print(solution.removeContinuousChars("abbbaa"))     # Output: ""
print(solution.removeContinuousChars("abbacccaa"))  # Output: "abb"
