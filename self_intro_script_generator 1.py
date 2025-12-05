"""Self Intro script Generator"""

import datetime

name = input('What is your name ?').strip()
age = input("How old are you").strip()
city = input("Which city do you live in ?").strip()
profession = input("What is your profession ?").strip()
hobby = input("What is your Hobby ?").strip()

#strip function removes the space fron the both last an the first
# line of the word but not the betweeen them . 

intro_message = (
    f"Hello! my name is {name}, I'm {age} years old and live in {city}"
    f"I work as a {profession} and I love enjoying {hobby} in my free time "
    f"Nice to meet you!\n"
)

current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on: {current_date}"

border = "*" * 80
final_output = f"{border}\n{intro_message}\n{border}"

print("\n" + final_output)