def ReadDataFiles():

    i=(int)(len(open('user.txt').read().split())/4+1)
    print("Total users: ", i)

    k=(int)(len(open('friend.txt').read().split())/3+1)
    print("Total friendship records:",k)

    j=(int)(len(open('word.txt').read().split())/4+1)
    print("Total tweets: ",j)

def Statistics():

    f1=open("user.txt","r")
    f2=open("friend.txt","r")
    
    i=(int)(len(open('user.txt').read().split()))
    k=(int)(len(open('friend.txt').read().split()))
    
    
    for j in range(0,i):
        line=f1.readline()
        str[user]=line
        ++user

    for j in range(0,i):
        
        
            
    
    print("Average number of friends: ")
    print("Minumum friends: ")
    print("Maximum number of friends: ")
    print("\n")
    print("Average tweets per user: ")
    print("Minimum tweets per user: ")
    print("Maximum tweets per user: ")
