'''Challenge Stylish Bio Generator for Instagram/Twitter'''

import textwrap

name = input("Enter your name").strip()
profession = input("Plz Enter your profession").strip()
emoji = input("Enter your favourite emoji").strip()
passion = input("Enter your passion in one line").strip()
website = input("Enter your website").strip()

print("\n Choose your Style :")
print("1. Simple lines")
print("2. Vertical flair")
print("3. Emoji Sandwich")

style =input("Enter 1,2 or 3: ").strip()

#function in python 
def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n 💡{passion}\n {website}"
    elif style == "2":
        return f"{emoji} {name}\n {profession}🔥\n {passion} \n {website}🔥"
    elif style == "3":
        return f"{emoji * 3} \n {name} - {profession}\n {passion }\n {website}\n {emoji}"
    

bio = generate_bio(style)

print("\n Your stylish bio:\n")
print ("*" * 50)
print(textwrap.dedent(bio))
print ("*" * 50)

save = input("Do you want to save this file yes or no ?").lower()

if save =='y':
    filename = f"{name.lower().replace('','_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print("file saved")    