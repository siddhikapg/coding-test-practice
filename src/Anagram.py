def main():
    print("Hello worldss")
    ans = isAnagram("fairy tales", "rail safety")
    print(ans)

def isAnagram(s1,s2):
    if len(s1) != len(s2):
        return False
    letters = dict()

    #Parse s1
    for l in s1:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1

    #Parse s2
    for l in s2:
        if l in letters:
            letters[l] -= 1
        else:
            letters[l] = 1
    #Check dictionary for dicrepancies
    for l in letters:
        if letters[l] != 0:
            return False
    return True
if __name__ == '__main__':
    main()