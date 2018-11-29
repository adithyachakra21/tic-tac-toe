from tttlib import *
T = genBoard()
while True:
   printBoard(T)
   moveX = int(input("X move?\n"))
   if (int(moveX) in range (0,9) and T[moveX]==0):
      T[int(moveX)] = 1
      state = analyzeBoard(T)
      #print (state)
      
      if state == 1:
         print("X won!")
         printBoard(T)
         break
      
      if state == 3:
         print("Draw!")
         printBoard(T)
         break

   printBoard(T)
   moveO = int(input("O move?\n"))
   if (int(moveO) in range(0,9) and T[moveO]==0):
      T[int(moveO)] = 2
      state = analyzeBoard(T)
      #print (state)

   if state == 2:
      print("O won!")
      printBoard(T)
      break

   if state == 3:
      print("Draw!")
      printBoard(T)
      break
    
      
