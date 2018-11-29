def genBoard():
    return [0,0,0,0,0,0,0,0,0] 

def printBoard(T):
    board=T
    num=["0","1","2","3","4","5","6","7","8"]
    answer = False
    
    for l in range (0,len(board),1): 
        if (type(T)==list and len(board) == 9 and board[l]>=0 and board[l]<3 and type(board[1])==int):
            answer=True
            i = 0
             
            while i < len(board):
                if board[i]==1:
                    num[i]="X"
                elif board[i]==2:
                    num[i]="O"
                i=i+1
                        
        else:
            answer=False
            break
            break         
            

               
    print (" " + num[0] + " | " + num[1] + " | " + num[2] + " ") 
    print ("---|---|---")  
    print (" " + num[3] + " | " + num[4] + " | " + num[5] + " ")
    print ("---|---|---")
    print (" " + num[6] + " | " + num[7] + " | " + num[8] + " ")
    print ('\n')
        
    return answer
        
    
#print(printBoard([0,1,2,2,2,1,1,3,0]))  

def analyzeBoard (T):
    board = T
    result = 0
    
    if (board[0]==1 and board[1]==1 and board[2]==1) or (board[0]==1 and board[3]==1 and board[6]==1) or (board[3]==1 and board[4]==1 and board[5]==1) or (board[1]==1 and board[4]==1 and board [7]==1) or (board[6]==1 and board[7]==1 and board[8]==1) or (board[2]==1 and board[5]==1 and board[8]==1) or (board[0]==1 and board[4]==1 and board[8]==1) or (board[2]==1 and board[4]==1 and board[6]==1): 
        result = 1   # X wins    

    elif (board[0]==2 and board[1]==2 and board[2]==2) or (board[0]==2 and board[3]==2 and board[6]==2) or (board[3]==2 and board[4]==2 and board[5]==2) or (board[1]==2 and board[4]==2 and board [7]==2) or (board[6]==2 and board[7]==2 and board[8]==2) or (board[2]==2 and board[5]==2 and board[8]==2) or (board[0]==2 and board[4]==2 and board[8]==2) or (board[2]==2 and board[4]==2 and board[6]==2): 
        result = 2   # O wins 

    elif (board[0]==0 or board[1]==0 or board[2]==0 or board[3]==0 or board[4]==0 or board[5]==0 or board[6]==0 or board[7]==0 or board[8]==0):
        result = 0    # still in play
    
    else:
        result = 3   # draw

    return result

#print (analyzeBoard([1,2,1,2,2,1,0,2,1]))

