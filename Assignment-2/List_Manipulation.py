#Create a list of numbers, then write a program that prints the square of each number in the list.
def Square_Of_List():
    try:
        a=int(input("Enter How Many Value Do You Want in a List:"))
        lst1=[]
        print("-"*50)
        for i in range(1,a+1):
            lst1.append(int(input("Enter {}'s Value:".format(i)).format(i)))
        lst2=[]
        print("-"*50)
        for j in lst1:
            lst2.append(j**2)
        print("\tOriginal Content of List = \n\t{}".format(lst1))
        print("-"*50)
        print("\tSquare Value of List = \n\t{}".format(lst2))
    except ValueError:
        print("-"*50)
        print("Don't Enter Alphanumerics, STRS, Symbols...")


Square_Of_List()