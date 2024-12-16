
def transducer(word):
    states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11"]
    vowels = "aeiou"
    
    current_state = "start"
    final_string = ""
    epsilon = ""
    
    for letter in word:
        # State start
        if current_state == "start" and letter:
            final_string += letter
            current_state = "q0"
            continue
        
        
        # State q0
        elif current_state == "q0":
            if letter in vowels:
                final_string += letter
                current_state = "q1"
                continue
            
            elif letter == "y":
                final_string += epsilon
                current_state = "q5"
                continue
            
            elif letter in "xzs" :
                final_string += letter
                current_state = "q8"
                continue
            elif letter == "^":
                final_string += epsilon
                current_state = "q11"
                continue
            else:
                final_string += letter
                current_state = "q0"
                continue
            
            
        # State q1
        elif current_state == "q1":
            if letter == "y":
                final_string += "y"
                current_state = "q2"
                continue
            elif letter in "xsz":
                final_string += letter
                current_state = "q8"
                continue
            else:
                current_state = "q0"
                final_string += letter
                continue
        
        
        # State q2
        elif current_state == "q2":
            if letter == "^":
                final_string += epsilon
                current_state = "q3"
                continue
            else:
                final_string += letter
                current_state = "q0"
                continue
            

        # State q3
        elif current_state == "q3":
            if letter == "s":
                final_string += epsilon
                current_state = "q4"
                continue
            else:
                
                return
        
        # State q4
        elif current_state == "q4":
            if letter == "#":
                final_string += "s"
                
                # print("Accepted")
                return final_string
            else:
                
                return
        # State q5    
        elif current_state == "q5":
            if letter == "^":
                final_string += epsilon
                current_state = "q6"
                continue
            else:
                final_string += "y"
                current_state = "temp"
                final_string += letter
                current_state = "q0"
                continue
            
        
        # State q6
        elif current_state == "q6":
            if letter == "s":
                final_string += epsilon
                current_state = "q7"
                continue
            else:
                
                return
          
        
        # State q7 
        elif current_state == "q7":
            if letter == "#":
                final_string += "i"
                current_state = "temp1"
                final_string += "e"
                current_state = "temp2"
                final_string += "s"
                
                # print("Accepted")
                return final_string
            
            else:
                
                return
            
        
        # State q8
        elif current_state == "q8":
            if letter == "^":
                final_string += epsilon
                current_state = "q9"
                continue
            elif letter in "xsz":
                final_string += letter
                current_state = "q8"
                continue
            else:
                final_string += letter
                current_state = "q0"
                continue
            
        # State q9
        elif current_state == "q9":
            if letter == "s":
                final_string += epsilon
                current_state = "q10"
                continue
            else:
                
                return
            
        
        # State q10
        elif current_state == "q10":
            if letter == "#":
                final_string += "e"
                current_state = "temp"
                final_string += "s"
                
                # print("Accepted")
                return final_string
            
            else:
                
                return
            
            
        elif current_state == "q11":
            if letter == "s":
                final_string += epsilon
                current_state = "q12"
                continue
            else:
                
                return
            
        
        elif current_state == "q12":
            if letter == "#":
                final_string += "s"
                # print("Accepted")
                return final_string
            else:
                
                return
            
            
            
if __name__ == "__main__":
    words = ["fact^s#", "fry^s#", "spy^s#", "box^s#", "buzz^s#", "fly^s#", "toy^s#", "boy^s#", "sky^s#", "puppy^s#", "pony^s#", "w^#s", "^s#"]
    

    for word in words:
        print(f"{word} : {transducer(word)}") 