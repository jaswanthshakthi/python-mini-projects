import random as rd
def roll():
    min_value=2
    max_value=6
    roll=rd.randint(min_value,max_value)
    return roll
while True:
    players=input("enter the number of players(2-4):")
    if players.isdigit():
        players=int(players)
        if  2 <= players <= 4:
            print("number between 2-4")
            break
        else:
          print("must be players between 2-4")

    else:
        print("invalid try")


max_score=50
player_score=[0 for _ in  range(players)]
print(player_score)

while max(player_score)< max_score:
    for i in range(players):
       print("\nplayer",i+1,"turn has just started\n")
       curren_score=0
       while True:
           s_roll=input("would you like to roll (y)")
           if s_roll!='y':
               break
           value=roll()
           if value==1:
               print("you rolled a 1! turned done")
               curren_score = 0
           else:
               curren_score+=value
               print("you rolled a",value)
           print("your current score is:",value)
           player_score[i]+=value
           print("your total score is",player_score[i])
    """
        while True:
         s_roll=input("would you like to roll (y)")
         if s_roll.lower()!="y":
          break
   
     
         value=roll()
    if value==1:
        print("yup!you rolled 1!")
        curren_score=0
        break
    else:
        curren_score=value
        print("you rolled a",value)
    print("your current score is",curren_score)

    
    player_score[i]==curren_score
    print("your total score is",player_score[i])
  

"""

