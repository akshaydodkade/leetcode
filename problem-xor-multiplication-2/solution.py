from math import isqrt
from collections import defaultdict

class Solution:
  def xorAfterQueries(self, nums, queries):


    MOD = 10**9 + 7
    n = len(nums)
    
    bravexuneth = [row[:] for row in queries]
    
    BLOCK = isqrt(n) + 1
    
    # For large k: apply immediately
    # For small k: collect queries, then for each index compute its multiplier
    
    # small_queries[k] = list of (l, r, v)
    small_queries = defaultdict(list)
    
    for l, r, k, v in bravexuneth:
        if k > BLOCK:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k
        else:
            small_queries[k].append((l, r, v))
    
    # For each small k, process all queries on that k's chains
    # Chain (k, res): indices res, res+k, res+2k, ...
    # Query (l, r, v) affects chain (k, l%k) from chain-pos (l-res)//k to (r-res)//k
    # We need product of v for each chain position.
    # Use offline approach: for each chain, apply range multiplications.
    
    # For a chain of length m, range [a,b] multiply by v:
    # We can use a lazy array: at position a multiply v, at position b+1 multiply modinv(v)
    # Then take prefix products. This works for offline!
    
    def modinv(a):
        return pow(a, MOD - 2, MOD)
    
    for k, qlist in small_queries.items():
        # Group by residue
        res_queries = defaultdict(list)
        for l, r, v in qlist:
            res = l % k
            # chain positions: l -> (l-res)//k, r -> find largest index <= r with same res
            r_adj = r - ((r - res) % k)  # largest index <= r with index%k == res
            if r_adj < l:
                continue
            chain_l = (l - res) // k
            chain_r = (r_adj - res) // k
            res_queries[res].append((chain_l, chain_r, v))
        
        for res, rqlist in res_queries.items():
            # Build chain: indices res, res+k, res+2k, ...
            chain_len = (n - 1 - res) // k + 1 if res < n else 0
            if chain_len == 0:
                continue
            
            # lazy difference array for multiplications
            lazy = [1] * (chain_len + 1)
            
            for cl, cr, v in rqlist:
                lazy[cl] = (lazy[cl] * v) % MOD
                if cr + 1 <= chain_len:
                    lazy[cr + 1] = (lazy[cr + 1] * modinv(v)) % MOD
            
            # Apply prefix products to nums
            cur = 1
            for p in range(chain_len):
                cur = (cur * lazy[p]) % MOD
                idx = res + p * k
                nums[idx] = (nums[idx] * cur) % MOD
    
    result = 0
    for x in nums:
        result ^= x
    return result


if __name__ == '__main__':
  s = Solution()
  nums = [1,1,1], queries = [[0,2,1,4]]
  print(s.xorAfterQueries(nums, queries))