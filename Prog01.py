def Prog01():

    num = int(input())

    for i in range(1,num):
        for j in range(1,i+1):
            print(j,end="")
        print(" ")   


if __name__ == "__main__":
    Prog01()
