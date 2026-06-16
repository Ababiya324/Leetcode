class Solution(object):
    def readBinaryWatch(self, turnedOn):
        result = []
        for h in range(12):
            # count bits in hour without modifying h
            x = h
            hb = 0
            while x > 0:
                hb += x % 2
                x //= 2

            for m in range(60):
                y = m
                mb = 0
                while y > 0:
                    mb += y % 2
                    y //= 2

                if hb + mb == turnedOn:
                    if m < 10:
                        result.append(str(h) + ":0" + str(m))
                    else:
                        result.append(str(h) + ":" + str(m))

        return result
