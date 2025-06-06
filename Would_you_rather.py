import random

# List of "Would You Rather" questions
questions = [
    {
        "question": "Would you rather be able to fly or be invisible?",
        "A": "Fly",
        "B": "Be invisible"
    },
    {
        "question": "Would you rather never have to sleep or never have to eat?",
        "A": "Never sleep",
        "B": "Never eat"
    },
    {
        "question": "Would you rather live on the moon or under the sea?",
        "A": "Live on the moon",
        "B": "Live under the sea"
    },
    {
        "question": "Would you rather have super strength or super speed?",
        "A": "Super strength",
        "B": "Super speed"
    },
    {
        "question": "Would you rather be able to talk to animals or speak all human languages?",
        "A": "Talk to animals",
        "B": "Speak all languages"
    },
    {
        "question": "Would you rather always know when someone is lying or be able to lie undetectably?",
        "A": "Always know when someone's lying",
        "B": "Be able to lie undetectably"
    },
    {
        "question": "Would you rather have free travel for life or free food forever?",
        "A": "Free travel",
        "B": "Free food"
    },
    {
        "question": "Would you rather be the funniest person in the room or the smartest?",
        "A": "Funniest",
        "B": "Smartest"
    },
    {
        "question": "Would you rather live 100 years in the past or 100 years in the future?",
        "A": "100 years in the past",
        "B": "100 years in the future"
    },
    {
        "question": "Would you rather have a rewind button in life or a pause button?",
        "A": "Rewind button",
        "B": "Pause button"
    },
    {
        "question": "Would you rather be able to breathe underwater or walk through walls?",
        "A": "Breathe underwater",
        "B": "Walk through walls"
    },
    {
        "question": "Would you rather be famous and poor or unknown and rich?",
        "A": "Famous and poor",
        "B": "Unknown and rich"
    },
    {
        "question": "Would you rather live without music or live without movies?",
        "A": "No music",
        "B": "No movies"
    },
    {
        "question": "Would you rather only be able to whisper or only be able to shout?",
        "A": "Whisper",
        "B": "Shout"
    },
    {
        "question": "Would you rather time travel to the past or the future?",
        "A": "Past",
        "B": "Future"
    },
    {
        "question": "Would you rather explore space or the deep ocean?",
        "A": "Space",
        "B": "Ocean"
    },
    {
        "question": "Would you rather always be 10 minutes late or always be 20 minutes early?",
        "A": "10 minutes late",
        "B": "20 minutes early"
    },
    {
        "question": "Would you rather be able to teleport anywhere or be able to read minds?",
        "A": "Teleport",
        "B": "Read minds"
    },
    {
        "question": "Would you rather never use social media again or never watch TV again?",
        "A": "No social media",
        "B": "No TV"
    },
    {
        "question": "Would you rather be stuck in a room with 100 spiders or one angry lion?",
        "A": "100 spiders",
        "B": "One angry lion"
    },
    {
        "question": "Would you rather have unlimited battery life or unlimited Wi-Fi?",
        "A": "Unlimited battery",
        "B": "Unlimited Wi-Fi"
    },
    {
        "question": "Would you rather never be able to laugh again or never cry again?",
        "A": "Never laugh",
        "B": "Never cry"
    },
    {
        "question": "Would you rather have a photographic memory or be able to forget anything instantly?",
        "A": "Photographic memory",
        "B": "Forget instantly"
    },
    {
        "question": "Would you rather only be able to eat sweet food or salty food forever?",
        "A": "Sweet food",
        "B": "Salty food"
    },
    {
        "question": "Would you rather always get stuck in traffic or always have a slow internet connection?",
        "A": "Stuck in traffic",
        "B": "Slow internet"
    },
    {
        "question": "Would you rather always know the time or always have exact change?",
        "A": "Know the time",
        "B": "Exact change"
    },
    {
        "question": "Would you rather have a pet dragon or be a dragon?",
        "A": "Have a dragon",
        "B": "Be a dragon"
    },
    {
        "question": "Would you rather be feared by all or loved by all?",
        "A": "Feared",
        "B": "Loved"
    },
    {
        "question": "Would you rather never get sick again or never feel tired again?",
        "A": "Never get sick",
        "B": "Never feel tired"
    },
    {
        "question": "Would you rather have to always sing instead of speaking or dance everywhere you go?",
        "A": "Sing instead of speak",
        "B": "Dance everywhere"
    },
    {
        "question": "Would you rather be able to control fire or water?",
        "A": "Control fire",
        "B": "Control water"
    },
    {
        "question": "Would you rather live in a world with no crime or no poverty?",
        "A": "No crime",
        "B": "No poverty"
    },
    {
        "question": "Would you rather have a flying car or a robot butler?",
        "A": "Flying car",
        "B": "Robot butler"
    },
    {
        "question": "Would you rather be able to stop time for 10 seconds or rewind it by 10 seconds?",
        "A": "Stop time",
        "B": "Rewind time"
    },
    {
        "question": "Would you rather live without books or without video games?",
        "A": "No books",
        "B": "No video games"
    }
]

import random

# Shuffle questions first
random.shuffle(questions)

# Counters for choices
count_A = 0
count_B = 0

amount = int(input("How many questions do you want to answer: "))

# Ask 5 random questions
for i in range(amount):
    q = questions[i]
    print("\n" + q["question"])
    print("A:", q["A"])
    print("B:", q["B"])

    choice = input("Choose A or B: ").strip().upper()
    while choice not in ["A", "B"]:
        choice = input("Invalid. Please choose A or B: ").strip().upper()

    if choice == "A":
        count_A += 1
    else:
        count_B += 1

# Summary
print("\nGame Over!")
print("You chose A", count_A, "times.")
print("You chose B", count_B, "times.")
