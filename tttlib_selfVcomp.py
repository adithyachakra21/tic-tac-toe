def genBoard():
   return [0,0,0,0,0,0,0,0,0]

def printBoard(T):
   if len(T) != 9:
      return False
   for i in T:
      if (i != 0) and (i != 1) and (i != 2):
         return False

   msg=[]
   pos=0
   for i in T:
      if (i==1):
         msg += ["X"]
      elif (i==2):
         msg += ["O"]
      else:
         msg += list(str(pos))
      pos+=1
     
   s = " " + msg[0] + " | " + msg[1] + " | " + msg[2]
   print(s)
   print("---|---|---")
   s = " " + msg[3] + " | " + msg[4] + " | " + msg[5]
   print(s)
   print("---|---|---")
   s = " " + msg[6] + " | " + msg[7] + " | " + msg[8]
   print(s)
   print('\n')
   return True


def analyzeBoard(t):
    if t[0] == t[1] == t[2] != 0:
        return t[0]
    if t[3] == t[4] == t[5] != 0:
        return t[3]
    if t[6] == t[7] == t[8] != 0:
        return t[6]
    if t[0] == t[3] == t[6] != 0:
        return t[0]
    if t[1] == t[4] == t[7] != 0:
        return t[1]
    if t[2] == t[5] == t[8] != 0:
        return t[2]
    if t[0] == t[4] == t[8] != 0:
        return t[0]
    if t[2] == t[4] == t[6] != 0:
        return t[2]

    n_opens=0
    for i in t:
       if i==0:
          n_opens+=1
    if n_opens == 0:
        return 3
    else:
        return 0


def inputAcceptable (T, player):
    if len(T)!=9:
        return False
    for i in T:
        if (i!=0) and (i!=1) and (i!=2):
            return False
    if (player!=1) and (player!=2):
        return False
    else:
        return True


def genNonLoser (T, player):
    L = list (T)
    count = 0
    if inputAcceptable(T, player)==False:
        return -1
    else:
        for i in range (len(L)):
            if L[i]==0:
                if player==1:
                    L[i]=2
                    if analyzeBoard(L)==2:
                        count=count+1
                        return i
                    else:
                        L = list(T)
                    
                        
                if player==2:
                    L[i]=1
                    if analyzeBoard(L)==1:
                        count=count+1
                        return i
                    else:
                        L = list(T)
                    
                        
        if count==0:
            print (count)
            return -1
         

#print(genNonLoser ([1,2,0,0,1,0,0,0,0], 2))

#print(genNonLoser([2,2,2,2,1,1,1,1,1], 1))

#print(inputAcceptable([2,2,0,1,1,1,1,1,1], 1))

def genWinningMove (T, player):
    L = list (T)
    count = 0
    if inputAcceptable(T, player)==False:
        return -1
    else:
        for i in range (len(L)):
            if L[i]==0:
                if player==1:
                    L[i]=1
                    if analyzeBoard(L)==1:
                        count=count+1
                        return i
                    else:
                        L = list(T)
                    
                        
                if player==2:
                    L[i]=2
                    if analyzeBoard(L)==2:
                        count=count+1
                        return i
                    else:
                        L = list(T)
                    
                        
        if count==0:
            print (count)
            return -1
         

#print (genWinningMove ([2,2,0,1,1,1,1,1,1],1))


def RandomMoveError (T):
    count = 0
    for a in range (len(T)):
        if T[a]==0:
            count=count+1
    if count==0:
        return False


def genRandomMove (T, player):
    L=list(T)
    if inputAcceptable(T,player)==False or RandomMoveError(T)==False:
        return -1
    import random
    while True:
        rand = random.randint(0,8)
        if L[rand]==0:
            return rand
        

#print(genRandomMove ([2,2,0,1,1,1,0,1,1],1))

def genOpenMove (T, player):
    L=list(T)
    if inputAcceptable(T,player)==False or RandomMoveError(T)==False:
        return -1
    else:
        for i in range (len(L)):
            if L[i]==0:
                return i
            

#print(genOpenMove ([2,2,0,1,1,1,0,1,1],1))

#print(analyzeBoard([1,2,2,3,2,1,0,0,1]))




        

    
            


