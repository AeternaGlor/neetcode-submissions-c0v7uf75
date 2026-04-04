class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # s1_dict = defaultdict(int)
        s1_list = [0]*26
        s2_list = [0]*26

        # сначала разделял, это тупо
        # for char in s1:
        #     s1_list[ord(char) - ord('a')] += 1
        
        for i in range(len(s1)):
            s1_list[ord(s1[i]) - ord('a')] += 1
            s2_list[ord(s2[i]) - ord('a')] += 1

        # if s1_list == s2_list:
        #     return True

        for i in range(1, len(s2) - len(s1) + 1):
            if s1_list == s2_list:
                return True
            j = i + len(s1) - 1
            s2_list[ord(s2[j]) - ord('a')] += 1
            s2_list[ord(s2[i-1]) - ord('a')] -= 1
            # if s1_list == s2_list:
            #     return True
        # return False
        return s1_list == s2_list



