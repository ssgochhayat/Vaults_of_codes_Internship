#Write a program to count word frequencies in a given text.
"""
def countWord():
    text=input("Enter the text for count word frequency: ")
    w_lst=text.split()
    word=input("Enter the word to check it frequency:")
    count = 0
    for w in w_lst:
        if (w==word):
            count+=1
    print("Given '{}' word Frequency in the text is {}".format(word,count))


#Main Program
countWord()   """

def word_frequency():
    text=input("Enter a line of Text:\n").lower()
    words=text.split()
    dct=dict()
    for word in words:
        if word in dct:
            dct[word]=dct[word]+1
        else:
            dct[word]=1
    print("-"*50)
    print("\tWord Frequencies")
    print("-"*50)
    for i,j in dct.items():
        print("\t{} ---> {}".format(i,j))

word_frequency()