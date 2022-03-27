
def main():
    print("Hello world")
    ans = isPalindrome("ada")
    print(ans)
def isPalindrome(sequence):
    start = 0
    end = len(sequence)-1
    pali = True
    while pali:
        #ignore special characters at start
        if not sequence[start].isalnum():
            start = start + 1
            continue
        # ignore special characters at end
        if not sequence[end].isalnum():
            end = end - 1
            continue
        #Check if the character matches
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


