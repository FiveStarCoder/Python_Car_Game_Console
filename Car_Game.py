name = input("Enter Your Name:\t")
started = False

while(True):
        if name == "Khan":
            choice = input("start---> To Start the Car\nstop---> To Stop the Car\nquit---> To quit the Car\n").lower()
            if choice == 'start' and not started:
                print("Car Started")
                started = True

            elif choice == 'start' and started:
                print("The car is Already Started")


            elif choice == "stop" and started:
                print("The Car Stopped")

                started = False
            elif choice =="stop" and not started:
                print("The Car is Already Stopped")
                started = False
            
            elif choice == "quit":
                print("Quited")
                break
            else:
                print("Wrong Command Entered")
        else:
            print("I don't Understand You")
            break



