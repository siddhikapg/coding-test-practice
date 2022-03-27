
def main():
    print("Hello world")
    ans = isPalindrome("abcba")
    print(ans)
def isPalindrome(sequence):
    start = 0
    end = len(sequence)-1
    pali = True
    while pali:
        if sequence[start] is sequence[end]:
            if start == end:
                break
            start = start + 1
            end = end - 1
        else:
            pali = False
    return pali
if __name__ == '__main__':
    main()


