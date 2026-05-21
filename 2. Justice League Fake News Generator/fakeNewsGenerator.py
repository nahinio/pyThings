import random
 
# lists of subjects, actions, and places for headline generation 
subjects = [
    "Batman",
    "Superman",
    "Wonder Woman",
    "The Flash",
    "Aquaman",
    "Green Lantern",
    "Cyborg",
    "Shazam",
    "Hawkman",
    "Green Arrow",
    "Martian Manhunter",
    "Black Canary",
]
 
actions = [
    "accidentally filed taxes late",
    "was caught eating the last donut at a press conference",
    "lost the Batmobile in a parking garage",
    "called customer support for 3 hours about a broken cape",
    "tripped over a villain's banana peel on live TV",
    "ordered the wrong pizza for the Justice League meeting",
    "got stuck in an elevator with Lex Luthor for 45 minutes",
    "failed his driver's license test twice",
    "ghosted the Joker mid-fight to attend a yoga class",
    "went viral for a terrible TikTok dance",
    "was fined $200 for jaywalking while saving the city",
    "forgot his superpower during a bank robbery",
]
 
places = [
    "at a Walmart in Metropolis",
    "outside the Gotham DMV",
    "in the Justice League cafeteria",
    "at a Costco in Central City",
    "inside the Atlantean IKEA",
    "at Themyscira's first ever Starbucks",
    "behind the Hall of Justice",
    "on the Watchtower's 3rd floor bathroom",
    "at a Gotham open-mic night",
    "during rush hour in Metropolis",
    "at an Arkham Asylum bake sale",
    "on a Spirit Airlines flight to Coast City",
] 


# headline generation loop
while True:
    print("Generating fake news headline...")
    subject = random.choice(subjects)
    action = random.choice(actions) 
    place = random.choice(places)

    headline = f"{subject} {action} {place}!"
    print(headline)
    

# ask user if they want to generate another headline
    again = input("Generate another headline? (y/n): ").strip().lower()
    if again != 'y':
        print("\n")
        print("Thanks for using the Justice League Fake News Generator!")
        break
    else:
        print("\n")
