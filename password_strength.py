from zxcvbn import zxcvbn

password = input("Enter a password: ")

result = zxcvbn(password)

score = result['score']

if score <= 1:
    print("Password Strength: Weak")
elif score <= 3:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")

print("\nSuggestions:")
for suggestion in result['feedback']['suggestions']:
    print("-", suggestion)

name = input("\nEnter your name: ")
birth_year = input("Enter your birth year: ")
pet_name = input("Enter your pet name: ")
fav_num = input("Enter your favourite number: ")

wordlist = [
    name + birth_year,
    name + fav_num,
    pet_name + birth_year,
    name + "@" + fav_num,
    pet_name + fav_num
]

with open("wordlist.txt", "w") as file:
    for word in wordlist:
        file.write(word + "\n")

print("\nWordlist generated successfully!")