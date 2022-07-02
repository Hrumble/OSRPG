
def StartGame():
    while True:
        playerInput = input("> ")
        try:
            eval(playerInput)
        except:
            print("[SYSTEM] Your Command Was Not Recognized")