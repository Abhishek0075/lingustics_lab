def check_right_plural(word):

    states = ["q0", "q1", "q2", "q4", "q5"]
    final_states = ["q3","q6"]
    vowels = "aeiou"
    
    current_state = "start"
    
    for letter in word:
        # print(f"{letter} : {current_state}")
        if current_state == "start" and letter:
            current_state = "q0"
            continue
        
        if current_state == "q0" :
            if letter in vowels:
                if letter == "i":
                    current_state = "q4"
                    continue
                else:
                    current_state = "q1"
                    continue
            
            else:
                current_state = "q0"
                continue

        elif current_state == "q1":
            if letter in vowels:
                current_state = "q1"
                continue
            elif letter == "y":
                current_state = "q2"
                continue
            else:
                current_state = "q0"
                continue
            
        elif current_state == "q2":
            if letter =="s":
                current_state = "q3"
                continue
            else:
                current_state = "q0"
                continue
            
        elif current_state == "q3":
            if letter == "y" :
                current_state = "q2"
                continue
            else:
                current_state = "q0"
                continue
            
        elif current_state == "q4":
            if letter =="e":
                current_state = "q5"
                continue
            elif letter == "i":
                continue
            else:
                current_state = "q0"
                continue
            
        elif current_state == "q5":
            if letter =="s":
                current_state = "q6"
                continue
            
            elif letter == "i":
                current_state = "q4"
                continue
            
            else:
                current_state = "q0"
                continue
               
        elif current_state == "q6":
            if letter == "i":
                current_state = "q4"
                continue
            else:
                current_state = "q0"
                continue
                
    if current_state in final_states:
        return True
    else:
        return False
    
test_words = ["boys", "toys", "ponies", "skies", "puppies", "boies", "toies", "ponys"]

for word in test_words:
    print(f"{word} : {check_right_plural(word)}")