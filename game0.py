 # set player to 1
player=1

# set number of coins
coinsnum=21
print(coinsnum)
while True:
    # get vaild move
    while True:
        print("player",player)
        move=int(input("what is your move?"))
        if move in [1,2,3] and move<coinsnum:
            break
        print("error,enter your move again")
        
    # update number of coins
    coinsnum=coinsnum-move
    
    # show the number of coins
    print(coinsnum)
    
    # check the win
    if coinsnum==1:
        print("player",player,"wins")
        break
    
    # switch players 2->1 , 1->2 go back to the vaild move
    if player==1:
        player=2
    else:
        player=1
print("game over")
