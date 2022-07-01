def inputLoop():
    try:
        choice = int(input("Which type of strip did you use?\n1:Bulb to Bulb\n2:Bulb to Channel\n3: Three Bulb Strip\nResponse: "));
        if(choice != 1 and choice != 2 and choice != 3):
            raise(ValueError)

        return choice
    except:
        print("Invalid input. To exit, use a keyboard interrupt.")
        choice = inputLoop()
        return choice
