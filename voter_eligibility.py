

print("=" * 45)
print("      VOTER ELIGIBILITY CHECKER")
print("=" * 45)

voting_age = {
    "india": 18,
    "usa": 18,
    "united states": 18,
    "uk": 18,
    "united kingdom": 18,
    "canada": 18,
    "australia": 18,
    "japan": 18,
    "brazil": 16,
    "indonesia": 17,
    "singapore": 21
}

name = input("Enter your name: ").strip()
country = input("Enter your country: ").strip().lower()

if country not in voting_age:
    print("\nSorry!")
    print("Voting age information is not available for your country.")
    print("Please check with your local election authority.")
else:
        age = int(input("Enter your age: "))

        required_age = voting_age[country]

        print("\n-----------Our Output-----------")

        if age >= required_age:
            print(f"Congratulations, {name}!")
            print("You are ELIGIBLE to vote.")
            print(f"Minimum voting age in {country.title()} is {required_age}.")
            print("You can proceed with voter registration or voting if registered.")
        else:
            years_left = required_age - age
            print(f"Sorry, {name}.")
            print("You are NOT eligible to vote yet.")
            print(f"Minimum voting age in {country.title()} is {required_age}.")
            print(f"You need to wait {years_left} more year(s).")
            print("Please register when you become eligible.")