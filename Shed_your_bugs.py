import os 

# forbidden words list 
Forbidden_words =["print" , "eval" , "exec"]

#limiting maximum length of the line 
Max_length = 80 

# #function to check if the given line of the code is comment 
# def if_comment(line):
#   return line.strips().startswith("#") #strips to remove whitespaces at start or end 

#function to check for the unclosed quote
def unclosed_quotes(line):
  one_time = line.count("'")
  if one_time % 2 != 0:
    return True 
  else:
    return False 

#function for checking one file at a time 
def Checking_file(Filename):
    with open(Filename , "r") as f:
        lines = f.readlines()
    
        #initialising the errors
        violations    = 0
        forbidd_words = False
    
        for line in lines:
           if len(line) >Max_length:
            violations += 1

    #skip the lines that are not comments 
           if line.strip().startswith("#") == False:
              if "#" in line :
                parts = line.split("#")
                line = parts[0] # use only the first part of the line w/o comments 
    #for checkinng the forbbiden keyword
              for word in forbidd_words:
                 if word in line:
                  forbidd_words =True

     #check for an unclosed string 
    if unclosed_quotes(line):
      violations +=1

    #printing our result
    if forbidd_words or violations > 5:
        print(Filename + ": HIGH RISK")
    elif violations > 0:
        print(Filename + ": LOW RISK")
    else:
        print(Filename + ": CLEAN")

        


