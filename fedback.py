def feedback():
    print("think number between 1 to 100")

    low=0
    high=100

    while low<=high:
        guess=(low+high)//2

        print("Agent guesse" ,guess)

        feedbackk= input("PLease give feedback to guess : " )
        feedbackk=feedbackk.lower()

        if feedbackk=='h':
            low=guess+1

        elif feedbackk=='l':
            high=guess-1
        elif feedbackk=='c':
            print("Your guessing number is " ,guess)
            break
        else:
            print("give answer in range ")

        if low>high:
            print("give proper feedback" )

feedback()

        