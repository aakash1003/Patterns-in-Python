def Prog03():
    
    num = int(input())

    for i in range(1,num):
        for j in range(1,(2*i-1)+1):
            print(i,end="")
        print(" ")   


if __name__ == "__main__":
    Prog03()
