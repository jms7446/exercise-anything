import sys
import random
import string


class KMP:
    def __init__(self, ptn):
        self.ptn = ptn
        self.table = self.make_partial_match_table(ptn)

    @staticmethod
    def make_partial_match_table(ptn):
        table = [0] * len(ptn)
        cnd = 0
        for pos in range(1, len(ptn)):
            while cnd > 0 and ptn[pos] != ptn[cnd]:
                cnd = table[cnd - 1]
            if ptn[pos] == ptn[cnd]:
                cnd += 1
                table[pos] = cnd
        return table

    def search(self, in_str):
        ptn = self.ptn
        table = self.table
        len_ptn_minus1 = len(ptn) - 1
        j = 0
        for i, c in enumerate(in_str):
            while j > 0 and c != ptn[j]:
                j = table[j-1]
            if c == ptn[j]:
                if j == len_ptn_minus1:
                    yield i - len(ptn) + 1
                    j = table[j]
                else:
                    j += 1


# 190ms
# forwart: 94ms
# backward: 53ms
def solve_rabin_karp_naive(txt, ptn):
    """
    N = len(txt)
    M = len(ptn)
    complexity = O(N + M)

    ptn: abcd
    txt: abcabcd
         abca
          bcab
           cabc
            abcd

    H[i] = S[i] * 2**(M-1) + S[i+1] * 2**(M-2) + ... + S[i+M-1] * 2**0
      ex)
    H[0] = ('a' * 8) + ('b' * 4) + ('c' * 2) + ('a' * 1)        # abca
    H[1] = ('b' * 8) + ('c' * 4) + ('a' * 2) + ('b' * 1)        #  bcab
         = (('b' * 4) + ('c' * 2) + ('a' * 1)) * 2 + ('b' * 1)
    """
    def l_hash(s):
        h = 0
        for i in range(len(ptn)):
            h = 2 * h + ord(s[i])
        return h

    if len(txt) < len(ptn):
        return 0
    if txt == ptn:
        return 1

    M = len(ptn)
    ptn_hash = l_hash(ptn)
    txt_hash = l_hash(txt[:M])
    h = 2 ** (M - 1)
    for i in range(M, len(txt)):
        oc = txt[i - M]
        ic = txt[i]
        txt_hash = (txt_hash - ord(oc) * h) * 2 + ord(ic)
        if ptn_hash == txt_hash and txt[i-M+1:i+1] == ptn:
            return 1
    return 0


# 40.55ms
def solve_rabin_karp(txt, ptn):
    N = len(txt)
    M = len(ptn)
    d = 256
    q = 10007
    if N < M:
        return 0

    p = t = 0
    for i in range(len(ptn)):
        p = (d * p + ord(ptn[i])) % q
        t = (d * t + ord(txt[i])) % q

    # h = d ** (M - 1)
    h = 1
    for i in range(M - 1):
        h = (h * d) % q

    if p == t and txt[:M] == ptn:
        return 1
    for i in range(N - M):
        t = (d * (t - ord(txt[i]) * h) + ord(txt[i+M])) % q
        if p == t and txt[i+1:i+M+1] == ptn:
            return 1
    return 0


# elapse time - test_big: 123ms, test_small: 119ms
def solve(S, P):
    if len(S) < len(P):
        return 0

    kmp = KMP(P)
    for _ in kmp.search(S):
        return 1
    return 0


def calculate_z(maxiter, zs, cs):
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while n < maxiter and abs(z) < 2:
            z = z * z + c
            n += 1
        output[i] = n
    return output


def func_1():
    N = 100000
    P = 100
    random.seed(2)
    in_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(N))
    ptn = ''.join(random.choice(string.ascii_lowercase) for _ in range(P))
    for i in range(100):
        solve_rabin_karp_naive(in_str, ptn)


if __name__ == "__main__":
    exec_str = f'func_{sys.argv[1]}()'
    exec(exec_str)
