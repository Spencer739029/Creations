import random
import time

characters = ["robot", "alien", "zombie", "vampire", "ghost", "witch", "werewolf", "mummy", "skeleton", "demon", "viking", "pirate", "samurai", "knight", "ninja", "cowboy", "superhero", "supervillain", "monster", "dragon", "superhero", "supervillain", "mutant", "cyborg", "android", "genie", "fairy", "elf", "orc", "troll", "goblin", "dwarf", "angel", "devil"]
setting = ["futuristic city", "haunted house", "space station", "ancient castle", "post-apocalyptic wasteland", "enchanted forest", "underwater kingdom", "deserted island", "cyberpunk metropolis", "steampunk village", "medieval town", "alien planet", "mythical realm", "superhero city", "supervillain lair", "monster-infested city", "dragon's lair", "superhero academy", "supervillain hideout"]
adjectives = ["scary", "mysterious", "dangerous", "frightening", "monstrous", "fierce", "powerful", "evil", "vicious", "mad", "cruel", "hideous", "hideous", "hideous", "hideous", "hideous", "hideous", "hideous", "hideous", "hideous", "hideous", "hideous", "hideous", "hideous", "hideous", "hideous", "hideous", "hideous", "hideous", "hideous"]
objectives = ["defeat the villain", "rescue the princess", "find the treasure", "stop the invasion", "save the world", "uncover the secret", "escape the trap", "solve the mystery", "protect the innocent", "avenge a fallen comrade", "stop a mad scientist", "prevent a disaster", "stop a monster attack", "save a city from destruction", "stop an evil plan", "rescue a kidnapped friend", "find a lost artifact",
              "stop a curse", "save a loved one", "stop a war", "prevent an apocalypse", "stop a time traveler", "stop an alien invasion", "stop a zombie outbreak", "stop a vampire attack", "stop a ghost haunting", "stop a witch's curse", "stop a werewolf attack", "stop a mummy's curse", "stop a skeleton uprising", "stop a demon's wrath", "stop a viking raid", "stop a pirate attack", "stop a samurai duel", "stop a ninja assassination", "stop a cowboy showdown"]
conflicts = ["a battle against a powerful enemy", "a monster attack", "an invasion by aliens", "a zombie outbreak", "a vampire attack", "a ghost haunting", "a witch's curse", "a werewolf attack", "a mummy's curse", "a skeleton uprising", "a demon's wrath", "a viking raid", "a pirate attack", "a samurai duel", "a ninja assassination", "a cowboy showdown", "a superhero vs supervillain fight",
             "a monster hunt", "a dragon battle", "a superhero training session gone wrong", "a supervillain's evil plan", "a mutant uprising", "a cyborg rebellion", "an android malfunction", "a genie granting wishes with a twist", "a fairy's mischief", "an elf's quest", "an orc invasion", "a troll bridge challenge", "a goblin heist", "a dwarf's treasure hunt", "an angel's fall from grace", "a devil's temptation"]
def generate_story():
    character = random.choice(characters)
    setting_choice = random.choice(setting)
    adjective = random.choice(adjectives)
    objective = random.choice(objectives)
    conflict = random.choice(conflicts)

    print("Welcome to the Story Prompt Generator!")
    time.sleep(2)
    print("Your randomly generated story prompt is:")
    time.sleep(2)
    print(f"A {adjective} {setting_choice}, a {character} must {objective}. The story unfolds with {conflict}.")
    time.sleep(1)
    restart = input("Would you like to generate another story? (yes/no): ")
    if restart.lower() == "yes":
        time.sleep(0.5)
        print("\nGenerating a new story...\n")
        time.sleep(1)
        generate_story()
    else:
        print("Thank you for using the story prompt generator!")

generate_story()

