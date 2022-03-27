
def main():
    print("Hello world")
    ans = isPalindrome("ada")
    print(ans)
def isPalindrome(sequence):
    start = 0
    end = len(sequence)-1
    pali = True
    while pali:
        if not sequence[start].isalnum():
            start = start + 1
            continue
        if not sequence[end].isalnum():
            end = end - 1
            continue
        if sequence[start].lower() == sequence[end].lower():
            if start == end:
                break
            start = start + 1
            end = end - 1
        else:
            pali = False
    return pali
if __name__ == '__main__':
    main()


