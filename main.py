"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45
PROFFESSOR_PER_SEMESTER = 5

# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    monthly_cost = annual_cost / MONTHS_PER_YEAR
    return monthly_cost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    daily_cost = annual_cost / (CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR)
    return daily_cost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    semester_cost = cost_per_semester(annual_cost)
    credit_cost = semester_cost / credits
    return credit_cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    credit_cost = cost_per_credit(annual_cost, credits)
    class_cost = credit_cost * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return class_cost


def cost_per_professor(annual_cost):
    """Give back what one professor costs."""
    semester_cost = cost_per_semester(annual_cost)
    professor_cost = semester_cost / PROFFESSOR_PER_SEMESTER
    return professor_cost


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = float(input("Enter the total cost for one year: "))
    credits = int(input("Enter the number of credits for this semester: "))
    while True:
        # Show your menu here.
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per class day")
        print("4. Cost per credit")
        print("5. Cost per class meeting")
        print("6. Cost per professor")
        print("Q. Quit")
        choice = input("Choose an option: ")

        if choice == "Q":
            break

        if choice == "1":
            semester_cost = cost_per_semester(annual_cost)
            print(f"One semester costs: ${semester_cost:,.2f}")
        elif choice == "2":
            monthly_cost = cost_per_month(annual_cost)
            print(f"One month costs: ${monthly_cost:,.2f}")
        elif choice == "3":
            daily_cost = cost_per_day(annual_cost)
            print(f"One class day costs: ${daily_cost:.2f}")
        elif choice == "4":
            credit_cost = cost_per_credit(annual_cost, credits)
            print(f"One credit costs: ${credit_cost:.2f}")
        elif choice == "5":
            class_cost = cost_per_class(annual_cost, credits)
            print(f"One class meeting costs: ${class_cost:.2f}")
        elif choice == "6":
            professor_cost = cost_per_professor(annual_cost)
            print(f"One professor costs: ${professor_cost:,.2f}")

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
    
