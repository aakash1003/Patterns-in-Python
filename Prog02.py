def Prog02():
    
    num = int(input())

    for i in range(1,num):
        for j in range(1,i+1):
            print(i,end="")
        print(" ")   


if __name__ == "__main__":
    Prog02()
