# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different
# word or phrase, typically using all the original letters exactly once.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#
#
#
# Constraints:
#
#     1 <= s.length, t.length <= 5 * 104
#     s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
def first_attempt(s, t):
    return s == t[::-1]


def second_attempt(s, t):
    for i, char in enumerate(s):
        if char != t[len(t) - 1 - i]:
            return False
    return True


s = "cat"
t = "tac"

one = "tar"
two = "car"

print("First True: ", first_attempt(s, t))
print("First False: ", first_attempt(one, two))

print("Second True: ", second_attempt(s, t))
print("Second False: ", second_attempt(one, two))
