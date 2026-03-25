# HI JOSIP! JUST NEED TO CLEAN UP AND FIX THE PRINT STATEMENTS,
# ESPECIALLY IF IT RETURNS FALSE...
# TO RUN: python FinalProjWarainSagusay.py
# Then input something like: !<>!


# initializing the stack and state
stack = []
stack.append("Z")

# Still have to implement reading a file
s = input()



def is_balanced():
    str_index = 0 # input pointer
    state = "q0" # initial state

    #  Using a dictionary to map opening and closing symbols.
    #  pairs.keys() to access left
    #  pairs.values() to access right
    pairs = {
        "(": ")",
        "{": "}",
        "[": "]",
        "<": ">",
        "!": "!"
    }

    print(f"Processing {s}")
    for i in s:

        print(f"ID: ({state}, {s[str_index:]}, {"".join(reversed(stack))})")

        # Checks if the string starts with a !
        if state == "q0":
            if i == "!":
                stack.append(i)
                state = "q1"
            else:
                # If string does not start with a "!", return false
                print(f"Invalid string. Failed at position {str_index}.")
                print(f"Remaining unprocessed input string: {s[str_index:]}")
                return False 
            
        elif state == "q1":
            if i == "!":
                if stack[-1] != "!":
                    print(f"Invalid string. Failed at position {str_index}.")
                    print(f"Remaining unprocessed input string: {s[str_index:]}")
                    return False
                else:
                    stack.pop()
                    state = "q2"
            elif i in pairs.keys():
                stack.append(i)
            elif i in pairs.values():
                if pairs[stack[-1]] != i:
                    print(f"Invalid string. Failed at position {str_index}.")
                    print(f"Remaining unprocessed input string: {s[str_index:]}")
                    return False
                stack.pop()
            elif i == "x":
                continue
            else:
                print(f"Invalid string. Failed at position {str_index}.")
                print(f"Remaining unprocessed input string: {s[str_index:]}")
                return False

        # If state q2 is entered early (symbols exist after the second "!"), return False
        elif state == "q2":
            print(f"Invalid string. Failed at position {str_index}.")
            print(f"Remaining unprocessed input string: {s[str_index:]}")
            return False

        str_index+= 1

    # Checks if the final state is q2
    if state == "q2":
        print(f"ID: ({state}, {s[str_index:]}, {"".join(reversed(stack))})")
        # If stack only has "Z" and the string is empty, return true. Return false if otherwise
        if stack == ["Z"] and s[str_index:] == "":
            print(f"{state} is a final state.")
            print(f"{s} is valid and has balanced brackets.")
            return True
        else:
            print(f"Invalid string. Failed at position {str_index}.")
            print(f"Remaining unprocessed input string: {s[str_index:]}")
            return False
    else:
        print(f"ID: ({state}, {s[str_index:]}, {"".join(reversed(stack))})")
        print(f"{state} is not a final state.")
        return False

# Runs the program
is_balanced()
