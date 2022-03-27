def main():
    print("Hello worldss")
    ans = isPalindromePermutation("taco cat")
    print(ans)
    ans = isPalindromePermutation("this is not permutation palindrome")
    print(ans)


def isPalindromePermutation(input):
    #get rid of spaces if any
    input = input.replace(" ", "")
    #bring the sequence to lower case
    input = input.lower()

    letters = dict()

    for i in input:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    odd_letter = 0
    for key,val in letters.items():
        if val%2 != 0 and odd_letter == 0:
            odd_letter += 1
        elif val%2 !=0 and odd_letter == 1:
            return False
    return True


if __name__ == '__main__':
    main()