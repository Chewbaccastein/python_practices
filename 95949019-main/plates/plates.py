def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if len(s) < 3 or len(s) > 6: # check min and max characters
        return False
    elif s[0].isdigit() or s[1].isdigit(): # check first 2 are letters
        return False

    numbers = ""
    letters = ""
    for _ in s:
        if _.isdigit():
            numbers += _
        elif _.isalpha():
            letters += _
    while numbers != "":   # if numbers exist->
        if letters == "": # see if letters exist
            return False
        elif numbers[0] == "0": # check if number starts with zero
            return False
        elif s[-1].isalpha(): # check if number is in the middle.
            return False
        elif numbers not in s: # also see if number in the middle but letter after as well
            return False
        else:
            break

    new_string = letters + numbers
    for _ in s:          # check if all are letters and numbers NOT special char or space
        if _ not in new_string:
            return False


    return True # if all passed, return True


main()
