class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        count_ones = s.count('1')

        t = "1" + s + "1"

        runs = []

        for ch in t:
            if not runs or runs[-1][0] != ch:
                runs.append([ch, 1])
            else:
                runs[-1][1] += 1

        max_gain = 0

        for i in range(1, len(runs) - 1):
            if (runs[i][0] == '1' and
                runs[i - 1][0] == '0' and
                runs[i + 1][0] == '0'):

                max_gain = max(max_gain,
                               runs[i - 1][1] + runs[i + 1][1])

        return count_ones + max_gain
        