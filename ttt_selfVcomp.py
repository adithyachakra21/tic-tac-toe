from tttlib import *

T = genBoard()
while True:
    printBoard(T)
    moveX = int(input ("X move?\n"))
    if moveX >= 0 and moveX < 9 and T[moveX]==0:
        T[int(moveX)]=1
    state=analyzeBoard(T)
    if state==1:
        print ("X won!")
        break
        
    elif state==3:
        print ("Draw!")
        break
        

    printBoard (T)
    if genNonLoser(T,2)==-1:
        
        if genWinningMove(T,2)==-1:
            
            if genOpenMove(T,2)==-1:
                
                if genRandomMove (T,2)==-1:
                    moveX=moveX
                else:
                    
                    moveO = genRandomMove (T,2)
                    T[int(moveO)]=2
                    state = analyzeBoard(T)    
                    if state==2:
                        print ("O won!")
                        break
                    elif state==3:
                        print ("Draw!")
                        break
                         
            else:
                
                moveO = genOpenMove (T,2)
                T[int(moveO)]=2
                state = analyzeBoard(T)    
                if state==2:
                    print ("O won!")
                    break
                     
                elif state==3:
                    print ("Draw!")
                    break
                         
        else:
            
            moveO = genWinningMove (T,2)
            T[int(moveO)]=2
            state = analyzeBoard(T)    
            if state==2:
                print ("O won!")
                break
                 
            elif state==3:
                print ("Draw!")
                break
                 
    else:
        
        moveO = genNonLoser (T,2)
        T[int(moveO)]=2
        state = analyzeBoard(T)    
        if state==2:
            print ("O won!")
            break
             
        elif state==3:
            print ("Draw!")
            break
             


    
               


        
