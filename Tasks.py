
HPriority = ["Go to see the dentist","Pick up lunch","Finish U00102 exercises"] #High Priority List
LPriority = ["Send invitation to party","Return books to the library"] #Low Priority List

def Menu():   #Functional Requirements 2
    print("Hello here is a list of task the program can perfom")
    print("1 Add a task to a list")
    print("2 Remove a task")
    print("3 Change Priority of a task")
    print("4 Promote a task")
    print("5 Display tasks")
    print("6 Load task from text files")
    print("7 Save task to text file")
    print("0 Exit")
    Chosen_Task = int(input("Enter the number for the task you wish to perform "))
    return Chosen_Task #Returns the chosen number from the user

def Add_Task(HighPriority, LowPriority): #Functional Requirements 3
    # Add function takes the already made list as paramaters to add to them
    print("Enter the description of the task and add @H" \
    " or @L for which list you wish for it to be in")
    Task = input()
    line = Task.split() #Splits the line into parts so everything can be look at individuallly
    data=""
    for pos in range(len(line)):
        if line[pos] == "@H":
            line[pos] = "" #Replaces the '@H' with nothing
            s = " ".join(line) #Rejoins the splitted string together
            HighPriority.append(s)#Adds the new string to HighPriority List
        elif line[pos] == "@L": 
            line[pos] = ""#Replaces the '@L' with nothing
            s = " ".join(line)
            LowPriority.append(s) #Adds the new string to LowPriority List     
    return (HighPriority, LowPriority) #Returns the new values of the HighProity and LowPriority lists

def Remove_Task(HighPriority, LowPriority): #Functional Requirements 4
    print("If you wish to remove a value on the proirty lits" \
    " enter 'High' or 'Low' and the position of the task  on the list")
    Priority = input("Priority of the task? ")
    Position = (int(input("Position on the list? "))-1)
    #Gets the Priority and Posistion from the user
    if Priority == "High":
        Chosen_List = "High"
    elif Priority == "Low": #Checks whether the user inputted High or Low
        Chosen_List = "Low"
    
    if Chosen_List == "High":
        Select_List = HighPriority 
    elif Chosen_List == "Low" :
        Select_List = LowPriority
    #Selects the list the function will removing from be user from the inputed priority from the user
        
    print(Select_List[Position],"is removed from the ",Chosen_List,"Priority List")  
    Select_List.remove(Select_List[Position]) #Removes the contents from the specified list
    return (HighPriority, LowPriority) #Returns the new values of the HighProity and LowPriority lists

def Change_Priority(HighPriority, LowPriority): #Functional Requirements 5
    print("If you wish to chage the Prority of a task enter the List"\
          " the task is on and its posistion")
    Priority = input("Priority of the task ")
    Position = (int(input("Position on the list? "))-1)
    #Gets the Priority and Posistion from the user

    if Priority == "High":
        Chosen_List = "High"
    elif Priority == "Low": #Checks whether the user inputted High or Low
        Chosen_List = "Low"
        
    if Chosen_List == "High":
        Destination = "Low"
        item = HighPriority[Position]
        #Move_to = LowPriority
        #Remove_from = HighPriority    
    elif Chosen_List == "Low":
        item = LowPriority[Position]#Store the value of whats we moving in the variable item
        Destination = "High"
        #Move_to = HighPriority
        #Remove_from = LowPriority
    #Selects the lists we are going to move the task and which we are going to remove it from

    if Chosen_List == "High": #If the chosen list was equal to "High"
        LowPriority.insert(0,item) #Inserts the into Low priority kist poisiton 0
        HighPriority.remove(item)#Removes contents of item from High Priority list
    elif Chosen_List == "Low": #If the chosen list was equal to "Low"
        HighPriority.append(item) #Adds the contents of item to the end of the High Priority list
        LowPriority.remove(item)#Removes contents of item from LowPriority list      
    print(item,"moved to the ", Destination,"Priority List")
    return (HighPriority, LowPriority) #Returns the new values of the HighProity and LowPriority lists

def Promote_Task(HighPriority, LowPriority):#Functional Requirements 6
    print("Enter the Tasks Priority and position that you wish to promote by one") 
    Priority = input("Priority of the task ")
    Position = (int(input("Position on the list? "))-1)

    if Priority == "High":
        Chosen_List = "High"
    elif Priority == "Low": #Checks whether the user inputted High or Low
        Chosen_List = "Low"

    if Chosen_List == "High":
        if (Position) == 0: #In High priority if Position - 1 is 0 then does nothing
            print("This item is top of the High Priority list")
            
        else:
            item = HighPriority[Position]
            HighPriority.remove(item) #Removes the item from its location in the list
            HighPriority.insert(Position - 1,item)#Re-adds the removed item but in one index up
            print(item,"moved to position", (Position - 1))
    elif Chosen_List == "Low":
        if (Position - 1) == - 1:
            item = LowPriority[Position]
            LowPriority.remove(item)#Removes the item from its location in the list
            HighPriority.append(item)#Adds the item to the end of Highpriority list
        else:
            item = LowPriority[Position]
            LowPriority.remove(item)#Removes the item from its location in the list
            LowPriority.insert(Position - 1,item)#Re-adds the removed item but in one index up
            print(item,"moved to position", (Position - 1))
    
    return (HighPriority, LowPriority) #Returns the new values of the HighProity and LowPriority lists

def Display_Tasks(HighPriority, LowPriority): #Functional Requirements 7
    countH = 0 #The two counters for both the Lists
    countL=0
    print("High Priority Tasks")
    for n in range(len(HighPriority)): 
        countH+=1
        print(countH,"",HighPriority[n])
    print("Low Priority Tasks")
    
    for n in range(len(LowPriority)):#The "len" makes the upper limit for the loop to the number of items in the list
        countL+=1
        print(countL,"",LowPriority[n])
    return (HighPriority, LowPriority) #Returns the new values of the HighProity and LowPriority lists
#In both loops prints every task in the list till it reaches the end of the list

def Load_Task(HighPriority, LowPriority):#Functional Requirements 8
    HFile = open("high-priority.txt","r")
    LFile = open("low-priority.txt","r")
    
    HighPriority = []
    LowPriority = []
    
    for n in HFile: #Reads all lines in HFlie then adds to the HighPriority List
        Hline = str(n.rstrip("\n"))
        #print(Hline)
        HighPriority.append(Hline)
    print(HighPriority)

    for n in LFile:#Reads all lines in LFile then adds to LowPriority List
        Lline = str(n.rstrip("\n"))
        #print(Lline)
        LowPriority.append(Lline)
    print(LowPriority)
    
    HFile.close()
    LFile.close()
    return(HighPriority, LowPriority) #Returns the new values of the HighProity and LowPriority lists

def Save_Task(HighPriority, LowPriority):#Functional Requirements 9
    HFile = open("high-priority.txt","w")
    LFile = open("low-priority.txt","w")

    for n in range(len(HighPriority)):
        Hline = HighPriority[n] + "\n"  #Goes through the list and add the content in that postiton to the line 'HLine'
        HFile.write(Hline)              #Write the line HLine to the file HFile
    for n in range(len(LowPriority)):
        Lline = LowPriority[n] + "\n"   #Goes through the list and add the content in that postiton to the line 'LLine'
        LFile.write(Lline)              #Write the line LLine to the file LFile
        
    HFile.close()
    LFile.close()
    print("High Priority and Low Priority List saved")
    return (HighPriority, LowPriority) #Returns the new values of the HighProity and LowPriority lists
  
option = "N/A"
while option != 0:
    print()
    option = Menu()
    if option == 1:
        Add_Task(HPriority, LPriority)
        #print(HPriority)
        #print(LPriority)
    elif option == 2:
        Remove_Task(HPriority, LPriority)
        #print(HPriority)
        #print(LPriority)
            
    elif option == 3:
        Change_Priority(HPriority, LPriority)
        #print(HPriority)
        #print(LPriority)
        
    elif option == 4:
        Promote_Task(HPriority, LPriority)
        #print(HPriority)
        #print(LPriority)
        
    elif option == 5:
        Display_Tasks(HPriority, LPriority)
        
    elif option == 6:
        Load_Task(HPriority, LPriority)
        #print(HPriority)
        #print(LPriority)
        
    elif option == 7:
        Save_Task(HPriority, LPriority)
        #print(HPriority)
       # print(LPriority)
    elif option == 0:
        print("Program Terminated")
        break
