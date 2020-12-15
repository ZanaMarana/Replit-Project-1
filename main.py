#Program name: U2,M2,Project
#Program purpose: Practicing with List-o-Matic program
#Created/Revised: J. Singh on 11/4/20

#Step 5
print("Step 5")
print()

birdList = ["robin", "eagle", "hawk", "finch", "crow"] #defines list

def listomatic(bird=""): #defines function with a parameter
  while birdList!=[]: #loops as long as list is not empty
    print()
    print("Look at the birds:",birdList) #shows user the list
    bird=input("Enter the name of a bird: ") #gets user input
    if bird.lower()=="quit": #checks if user wants to quit
      break #quits the loop
    elif bird.lower() in birdList: #checks if a bird entere is in the list
      birdList.remove(bird) #removes entered bird
      print("1 instance of",bird,"removed from list") #tells user what was removed
    elif bird=="": #if the user just hits 'enter'
      print(birdList.pop(-1),"popped from list") #pops last item from list and shows it to user
    else: #else in this case checks if an item is not in the list
      birdList.append(bird) #adds item to the list
  return "Goodbye!" #if user enters quit or the list is empty, it will return a 'goodbye' message
print(listomatic()) #calls the function

print()
print("End of code")