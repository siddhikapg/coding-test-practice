def main():
    print("Hello worldss")
    ans = isPermutation("google","eooggl")
    print(ans)
    ans = isPermutation("not", "top")
    print(ans)
# Time Complexity: O(n)
# Space Complexity: O(n)
def isPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = s1.lower()
    s2 = s2.lower()

    letters = dict()

    for l in s1:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    for l in s2:
        if l in letters:
            letters[l] -= 1
        else:
            return False
    return True
if __name__ == '__main__':
    main()