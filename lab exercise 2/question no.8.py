#car game
#help
#start-to start the car   stop-to stop the car  quit-to exit
#asd    #i dont understand thisio
#start   #car started....ready to go!!
#stop  #car swtopped...
#quit


command=" "
started=False
while True:
    command= input(">").lower()
    if command =="start":
        if started:
            print("the car is already started")
        else:
            started=True
            print("car started....")
        print("car started")
    elif command =="stop":
        if not started:
            print("car is already stopped..")
        else:
            started= False
            print("car stopped")
    elif command== "help":
        print("""
start-stat the car
stop-stop the car
quit-to exit""")
    elif command=="quit":
        break
    else:
        print("sorry i dont understand this")