"""
811. Subdomain Visit Count

URL: https://leetcode.com/problems/subdomain-visit-count/
Level: Easy
"""
from typing import List
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}
        ans = []

        for d in cpdomains:
            count, domain = d.split(' ')
            count = int(count)

            subdomains = domain.split('.')
            for i in range(len(subdomains)):
                tmp = '.'.join(subdomains[i:])
                if tmp in counts:
                    counts[tmp] += count
                else:
                    counts[tmp] = count
        
        for d, c in counts.items():
            ans.append('{} {}'.format(c, d))
        return ans

if __name__ == '__main__':
    solution = Solution()
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(solution.subdomainVisits(cpdomains))