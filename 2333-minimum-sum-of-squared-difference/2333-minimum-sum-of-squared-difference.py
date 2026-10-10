class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        total = sum(diff)

        if total <= k:
            return 0

        diff.sort(reverse=True)
        diff.append(0)

        for i in range(len(diff) - 1):
            cost = (i + 1) * (diff[i] - diff[i + 1])

            if k >= cost:
                k -= cost
            else:
                level, remainder = divmod(k, i + 1)
                target = diff[i] - level
                return (
                    remainder * (target - 1) ** 2
                    + (i + 1 - remainder) * target ** 2
                    + sum(x * x for x in diff[i + 1:])
                )

        return 0