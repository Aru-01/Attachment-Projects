while True:
    print(
        """ 
          <-- Welcome to Our Server --> 
          Select (1) to start the program
          Select (0) to exit the program
          """
    )
    n = int(input("Enter your choice: "))
    if n == 1:
        while True:

            print(
                """ 
                    <-- Main Menu -->
                    Select (2) to view the student list
                    Select (3) to view the mentor list
                    Select (4) to view the course list
                    Select (5) for career guidelines
                    Select (6) to return to the main menu
                    """
            )
            choice = int(input("Enter your choice: "))
            if choice == 2:
                print(
                    """
                        ---- Student List -----
                        Name          Course
                        Mr. A         React 
                        Mr. B         MERN
                        Mr. C         Django
                        Mr. D         WordPress
                        Mr. E         Laravel
                        """
                )
            elif choice == 3:
                print(
                    """
                        ----- Mentor List -----
                        Name          ID
                        Mr. X         245 
                        Mr. Y         745
                        Mr. Z         123
                        """
                )
            elif choice == 4:
                print(
                    """
                        ----- Course List -----
                        React
                        MERN
                        Django
                        WordPress
                        Laravel               
                        """
                )
            elif choice == 5:
                print("This service is currently unavailable.")
            elif choice == 6:
                print("Returning to the main menu...")
                break
            else:
                print("Please select a valid option.")
    elif n == 0:
        print("Thank you for visiting our mini project. Goodbye!")
        break
    else:
        print("Please select a valid option.")
