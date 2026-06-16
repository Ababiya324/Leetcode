class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        cnt = [0]*26

        for ch in magazine:
            cnt[ord(ch)-97] += 1

        for ch in ransomNote:
            i = ord(ch)-97
            cnt[i] -= 1
            if cnt[i] < 0:
                return False

        return True

        