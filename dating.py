#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: March 31st, 2025
# This program asks the user's age and it checks
# if the user is 25 years old and above and less
# 40 years old.

def main():

    user_age_as_string = input("Enter your age: ")
    print("")

    try:
        maximum_age = 40
        minimum_age = 25

        user_age = int(user_age_as_string)

        if user_age >= minimum_age and user_age <= maximum_age:
            print("You can date my grandchild.")

        else:
            print("You cannot date my grandchild.")

    except ValueError:
        print(f"{user_age_as_string} is not a valid age")
        print("")
        print("Please try again!")

    finally:
        print("Thank you for playing!")


if __name__ == "__main__":
    main()
