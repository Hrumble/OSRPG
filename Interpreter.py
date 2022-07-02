
def StartGame():
    while True:
        playerInput = input("> ").split()
        func = playerInput[0]
        command = func + "("
        if not len(playerInput) < 1:
            args = playerInput[1:]
            for i in range(len(args)):
                if i == 0:
                    command += args[i]
                else:
                    command += ", " + args[i]
        command += ")"
        print(command)

        try:
            eval(command)
        except:
            print("[SYSTEM] Your Command Was Not Recognized")

