def main():
    print("Hello worldss")
    ans = isUnique("abcdefgh")
    print(ans)
    ans = isUnique("notnotnot")
    print(ans)
# Time Complexity: O(n)
# Space Complexity: O(n)
def isUnique(input):
    #Assumption: The string contains alphabets or space
    input = input.replace(" ","")
    input = input.lower()
    letters = dict()
    for l in input:
        if l in letters:
            return False
        else:
            letters[l] = 1
    return True
if __name__ == '__main__':
    main()