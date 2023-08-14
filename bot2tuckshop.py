import random

#salutation
greeting= input("Hello I'm JA DECIDES: ")


#snacks
snacks= ("meatpie", "donut", "gala", "cake")

#moods
moods = ("happy", "sad", "angry", "tired")

# Ask the user about their mood
mood = input("How are you feeling today? ")

# Choose a food item based on the user's mood
if mood == "happy":
  snacks = random.choice(snacks)
elif mood == "sad":
  snacks = random.choice(snacks)
  
elif mood == "angry":
  snacks = random.choice(snacks)
elif mood == "tired":
  snacks = random.choice(snacks) 

# Print the food item to the user
print(f"since you are in a {mood} mood you should try {snacks}.")