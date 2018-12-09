
#lab 15: Python Standard Library
#problem 1:Craps Game
#use a function from the random library to simulate rolling dice
#write a function that rolls a single die
#uses that function to build a program that lets the user play craps

##rules of craps##
#player rolls two sided dice and adds the numbers rolled together
#on the first roll: a 7 or 11 automatically wins
#on the first roll: a 2,3, or 12 automatically loses.
#on the first roll: a 4,5,6,8,9,or 10 become a point.
#The player rolls the two dice again until they get the point again
#or the player rolls a 7 and they lose.

import random

#use a function from the random library to simulate rolling dice
#write a function that rolls a single die
def roll_die():
  """
  rolls a die between 1 and 6
  """
  min=1
  max=6
  roll_1=random.randint(min,max)
  roll_2=random.randint(min,max)  
  totalroll=roll_1+roll_2
  print "total dice roll is: ",totalroll
  
  rollnum=0
  point=0
  if rollnum<=1:
    if totalroll==7 or totalroll==11:
      print "Player Wins"
    elif totalroll==2 or totalroll==3 or totalroll==12:
      print "Player Loses"
    else:
      point=totalroll
    rollnum=rollnum+1
  if rollnum>1:
    if point==7:
      print "You Lose"
    elif totalroll==point:
      print "You Win"
    
#player rolls two 6 sided dice and adds the numbers rolled together

def main():
  print roll_die()