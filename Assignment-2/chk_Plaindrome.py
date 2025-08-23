# Write a program that checks if a given word is a palindrome.
def checkPalindrome():
    word=input("\tEnter a Word to Check Palindrome or Not:")
    b=word.lower()
    print("-"*50)
    if b==b[::-1]:
        print("\t'{}' is a Palindrome.".format(word))
    else:
        print("\t'{}' is Not a Palindrome Word.".format(word))

#Main Program
checkPalindrome()