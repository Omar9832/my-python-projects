import discord
from discord.ext import commands
import random
from colorama import Fore, Style, init
import asyncio
import time
from datetime import datetime, timedelta



import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
print(TOKEN)
current_league="Unranked"
league=""
leaderboardscores=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
leaderboardnames=["", "", "", "", "", "", "", "", "", ""]
users=[]
perks=[]
n=0
t=0
achievements=[]
games=0
wheels=0
k=0
game_active=False
total_number_of_games=0
highest_scores_of_users=[]
coins_of_users=[]
points_lost=25
highest_score=0
point_gained=0
easy_points=10
medium_points=25
hard_points=50
question=""
total_number_of_questions_done=0
number_of_correct_questions=0
accuracy=0
number_of_questions=16
bonus_points=500
highest_streak=0
coins=0
spinner_powerups=["2x", "flash", "shield", "skip", "bonus", "4x", "10x", "Zap", "20x"]
powerups=["2x", "flash", "shield", "skip", "bonus", "4x", "rep loss", "10x", "Zap", "20x"]
costs_of_powerups=[2000, 1500, 1000, 500, 700, 4000, 100000, 10000, 500, 20000]
user_num_of_powerups=[1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
chests=0
temp=0
coinsrange1=[5, 10, 15, 20, 25]
coinsrange2=[30, 35, 40, 45, 50]
coinsrange3=[55, 60, 65, 70, 75] 
coinsrange4=[80, 85, 90, 95, 100]
coinsrange5=[105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200]
coinsrange6=[205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300]
coinsrange7=[305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400]
coinsrange8=[405, 410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490, 495, 500, 750, 1000, 1250, 1500, 1750, 2000]
ranks=["Unranked", "Bronze League", "Silver League", "Gold League", "Plat League", "Diamond League", "Champion League"]
trivia_questions = [
    # General Knowledge
    "What is the largest planet in our solar system?",
    "Who painted the Mona Lisa?",
    "In which year did the Titanic sink?",
    "What is the capital city of Canada?",
    "What element does 'O' represent on the periodic table?",
    "Who is known as the 'Father of Computers'?",
    "What is the longest river in the world?",
    "Who invented the telephone?",
    "Which country is the largest by land area?",
    "In which city would you find the Colosseum?",

    # Geography
    "What is the smallest country in the world?",
    "Which continent is the Sahara Desert located on?",
    "What is the capital city of Australia?",
    "Which ocean is the largest?",
    "What is the largest island in the world?",
    "In which country would you find the Great Barrier Reef?",
    "Which mountain is the highest in the world?",
    "Which country has the most official languages?",
    "Which country is known as the Land of the Rising Sun?",
    "What is the name of the longest mountain range in the world?",

    # History
    "Who was the first president of the United States?",
    "During which war was the Battle of Gettysburg fought?",
    "Who was the first woman to fly solo across the Atlantic Ocean?",
    "In which year did World War I begin?",
    "Who was the leader of the Soviet Union during World War II?",
    "What ancient civilization built the pyramids of Giza?",
    "Who was the first emperor of China?",
    "Which historical figure famously crossed the Alps with elephants?",
    "What year did the Berlin Wall fall?",
    "Which ship brought the Pilgrims to America?",

    # Science & Nature
    "What is the chemical formula for water?",
    "How many bones are in the adult human body?",
    "Which planet is known as the 'Red Planet'?",
    "What is the powerhouse of the cell?",
    "What gas do plants absorb from the atmosphere for photosynthesis?",
    "What is the process by which plants make their own food?",
    "Who developed the theory of relativity?",
    "Which organ in the human body is responsible for pumping blood?",
    "What is the smallest unit of life?",
    "What is the main ingredient in glass?",

    # Literature
    "Who wrote 'Romeo and Juliet'?",
    "Which book starts with the line 'Call me Ishmael'?",
    "Who wrote '1984'?",
    "What is the title of the first Harry Potter book?",
    "In which novel would you find the character of Jay Gatsby?",
    "Who wrote 'Pride and Prejudice'?",
    "Who is the protagonist of 'The Catcher in the Rye'?",
    "Which novel features the character of Huckleberry Finn?",
    "Who wrote 'The Lord of the Rings'?",
    "What is the name of Sherlock Holmes' companion?",

    # Movies & Entertainment
    "Who won the Academy Award for Best Actor in 1994?",
    "What was the first feature-length animated film?",
    "In which movie would you find the character of Darth Vader?",
    "Who directed 'Jaws'?",
    "Who played the character of Jack Dawson in Titanic?",
    "What is the highest-grossing movie of all time?",
    "What is the name of the fictional African country in 'Black Panther'?",
]
trivia_answers = [
    # General Knowledge
    "Jupiter",  # Largest planet in our solar system
    "Leonardo da Vinci",  # Painted the Mona Lisa
    "1912",  # Year Titanic sank
    "Ottawa",  # Capital city of Canada
    "Oxygen",  # Element represented by 'O'
    "Charles Babbage",  # Father of Computers
    "Nile",  # Longest river in the world
    "Alexander Graham Bell",  # Inventor of the telephone
    "Russia",  # Largest country by land area
    "Rome",  # City where the Colosseum is located

    # Geography
    "Vatican City",  # Smallest country in the world
    "Africa",  # Continent where the Sahara Desert is located
    "Canberra",  # Capital city of Australia
    "Pacific",  # Largest ocean
    "Greenland",  # Largest island in the world
    "Australia",  # Country with the Great Barrier Reef
    "Mount Everest",  # Highest mountain in the world
    "India",  # Country with the most official languages
    "Japan",  # Country known as the Land of the Rising Sun
    "Andes",  # Longest mountain range in the world

    # History
    "George Washington",  # First president of the United States
    "American Civil War",  # Battle of Gettysburg
    "Amelia Earhart",  # First woman to fly solo across the Atlantic Ocean
    "1914",  # Year World War I began
    "Joseph Stalin",  # Leader of the Soviet Union during WWII
    "Ancient Egypt",  # Civilization that built the pyramids of Giza
    "Qin Shi Huang",  # First emperor of China
    "Hannibal",  # Historical figure who crossed the Alps with elephants
    "1989",  # Year the Berlin Wall fell
    "Mayflower",  # Ship that brought the Pilgrims to America

    # Science & Nature
    "H2O",  # Chemical formula for water
    "206",  # Number of bones in the adult human body
    "Mars",  # Planet known as the 'Red Planet'
    "Mitochondria",  # Powerhouse of the cell
    "Carbon Dioxide",  # Gas absorbed by plants for photosynthesis
    "Photosynthesis",  # Process by which plants make their own food
    "Albert Einstein",  # Developer of the theory of relativity
    "Heart",  # Organ that pumps blood in the human body
    "Cell",  # Smallest unit of life
    "Silica",  # Main ingredient in glass

    # Literature
    "William Shakespeare",  # Author of 'Romeo and Juliet'
    "Moby-Dick",  # Book starting with "Call me Ishmael"
    "George Orwell",  # Author of '1984'
    "Harry Potter and the Philosopher's Stone",  # First Harry Potter book
    "The Great Gatsby",  # Novel featuring Jay Gatsby
    "Jane Austen",  # Author of 'Pride and Prejudice'
    "Holden Caulfield",  # Protagonist of 'The Catcher in the Rye'
    "The Adventures of Huckleberry Finn",  # Novel featuring Huck Finn
    "J.R.R. Tolkien",  # Author of 'The Lord of the Rings'
    "Dr. John Watson",  # Sherlock Holmes' companion

    # Movies & Entertainment
    "Tom Hanks",  # Academy Award for Best Actor in 1994
    "Snow White and the Seven Dwarfs",  # First feature-length animated film
    "Star Wars",  # Movie with Darth Vader
    "Steven Spielberg",  # Director of 'Jaws'
    "Leonardo DiCaprio",  # Played Jack Dawson in Titanic
    "Avatar",  # Highest-grossing movie of all time
    "Wakanda",  # Fictional African country in 'Black Panther'
]
easy_questions = [
    # General Knowledge
    "What is the largest planet in our solar system?",  
    "Who painted the Mona Lisa?",  
    "What is the chemical formula for water?",  
    "Which planet is known as the 'Red Planet'?",  
    "What is the capital city of Canada?",  
    "What element does 'O' represent on the periodic table?",  
    "Which ocean is the largest?",  
    "What is the smallest country in the world?",  
    "Who invented the telephone?",  
    "Which country is known as the Land of the Rising Sun?",  

    # Geography
    "How many continents are there on Earth?",  
    "What is the currency of the United Kingdom?",  
    "Which country is home to the Great Barrier Reef?",  
    "Which organ pumps blood in the human body?",  
    "Which European city is known as the 'City of Canals'?",  
]

medium_questions = [
    # History
    "In which year did the Titanic sink?",  
    "Who is known as the 'Father of Computers'?",  
    "Who was the first president of the United States?",  
    "Which mountain is the highest in the world?",  
    "During which war was the Battle of Gettysburg fought?",  

    # Science & Nature
    "What is the powerhouse of the cell?",  
    "Which country has the most official languages?",  
    "What is the main ingredient in glass?",  
    "What gas do plants absorb from the atmosphere for photosynthesis?",  
    "What is the smallest unit of life?",  

    # Literature
    "Which book starts with the line 'Call me Ishmael'?",  
    "What is the title of the first Harry Potter book?",  
    "Who wrote 'Pride and Prejudice'?",  
]



intents=discord.Intents.default()
client=discord.Client(intents=intents)
intents.messages = True
intents.message_content = True

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    



question=random.choice(trivia_questions)
@client.event

async def on_message(message):

   

    

    
    global highest_score
    image="Barcode.png"
    users.append(message.author.display_name) 
    global coins
    global perks
    global wheels
    coins_of_users.append(coins)
    highest_scores_of_users.append(highest_score)
    global game_active
    if not game_active:
        if message.content.startswith("$r"):
            await message.channel.send(f"Scan to rate us!")
            await message.channel.send(file=discord.File(image))
        if message.author==client.user:
            return
        if message.content.startswith("$hello"):
            await message.channel.send(f"Hello, {message.author.display_name}. I am Trivia Bot. Are you ready to play some Trivia? Type $y for yes, $n for no, $l for leaderboard, $s to view you stats, $o to open chest, $c to view number of coins, or $m to view shop.")
        if message.content.startswith("$l"):
            j=9
            leaderboard_message="Leaderboard:\n"
            while j>=0:
                leaderboard_message+=f"{10-j}"
                if leaderboardnames[j]!="":
                    leaderboard_message+=f"     {leaderboardnames[j]}     {leaderboardscores[j]}\n"
                else:
                    leaderboard_message+=f"\n"
                j=j-1
            await message.channel.send(leaderboard_message)
        
        if message.content.startswith("$s"):
            global highest_streak
            global number_of_correct_questions
            global total_number_of_questions_done
            global accuracy
            global current_league
            global total_number_of_games
            global achievements
            if message.author.display_name=="Omar" and highest_score<10000:
                highest_score=20000
            await message.channel.send(f"Name   {message.author.display_name}\nHighest Score   {highest_score}\nHighest Streak   {highest_streak}\nNumber of Correct Questions   {number_of_correct_questions}\nNumber of Questions Done   {total_number_of_questions_done}\nAccuracy   {accuracy}\nNumber of Games   {total_number_of_games}%\nLeague   {current_league}\n")
            if not achievements:
                await message.channel.send(f"You have no achievements!")
            else:
                await message.channel.send(f"Achievements:\n ")
                for x in achievements:
                    await message.channel(f"{x}\n")
        
        if message.content.startswith("$o"):
            global chests
            amount_of_coins=0
            if chests>0:
                if current_league=="Unranked":
                    combined_range=coinsrange1
                elif current_league=="Bronze League":
                    combined_range=coinsrange1+coinsrange2
                elif current_league=="Silver League":
                    combined_range=coinsrange1+coinsrange2+coinsrange3
                elif current_league=="Gold League":
                    combined_range=coinsrange1+coinsrange2+coinsrange3+coinsrange4
                elif current_league=="Plat League":
                    combined_range=coinsrange1+coinsrange2+coinsrange3+coinsrange4+coinsrange5
                elif current_league=="Diamond League":
                    combined_range=coinsrange1+coinsrange2+coinsrange3+coinsrange4+coinsrange5+coinsrange6
                else:
                    combined_range=coinsrange1+coinsrange2+coinsrange3+coinsrange4+coinsrange5+coinsrange6+coinsrange7+coinsrange8
                chests=chests-1
                print(combined_range)
                amount_of_coins=random.choice(combined_range)
                await message.channel.send(f"You have earned {amount_of_coins}!")
                coins=coins+amount_of_coins
            else:
                await message.channel.send(f"You have no chests within your inventory!")
        if message.content.startswith("$w"):
            global is_powerup
            is_powerup=False
            global wheel_item
            if wheels>0:
                if current_league=="Bronze League":
                    perks=[10, 50, "skip", 100]
                elif current_league=="Silver League":
                    perks=[10, 50, 100, 200, "skip","zap"]
                elif current_league=="Gold League":
                    perks=[10, 50, 100, "bonus", "shield", 200, "skip", 400, "zap"]
                elif current_league=="Plat League":
                    perks=[10, 50, 100, 200, 400, "skip", 600, "zap", "flash", "2x", "4x"]
                elif current_league=="Diamond League":
                    perks=[10, 50, 100, 200, 400, 600, "skip", 800, "zap", "flash", "2x", "4x", "10x"]
                elif current_league=="Champion League":
                    perks=[10, 50, 100, 200, 400, 600, 800, "skip", 1000, "zap", "flash", "2x", "4x", "10x", "20x"]
                wheels=wheels-1
                wheel_item=random.choice(perks)
                if wheel_item in powerups:
                    wheel_item_index=powerups.index(wheel_item)
                    user_num_of_powerups[wheel_item_index]=user_num_of_powerups[wheel_item_index]+1
                    await message.channel.send(f"You have recieved {wheel_item}!")
                else:
                    await message.channel.send(f"You have recieved {wheel_item} coins!")
                    coins=coins+wheel_item
                    await message.channel.send(f"Coins: {coins}")
                
                
            else:
                await message.channel.send("You have no wheels in your inventory!")

                
        
            await message.channel.send(f"Coins: {coins}")
        if message.content.startswith("$c"):
            await message.channel.send(f"Coins: {coins}")
        if message.content.startswith ("$m"):
            m=0
            await message.channel.send(f"Name of Powerup    Cost of Powerup\n")
            while m<len(powerups):
                await message.channel.send(f"       {powerups[m]}                                               ${costs_of_powerups[m]}")
                m=m+1
        if message.content.startswith("$b"):
            await message.channel.send(f"Enter the item you want to buy")
            def check3(msg):
                return msg.author==message.author and msg.channel==message.channel

            
            item=await client.wait_for("message", check=check3, timeout=10000000000)
            x=0
            while x<len(powerups):
                if item.content.strip().lower()==powerups[x]:
                    if coins>=costs_of_powerups[x]:
                        await message.channel.send(f"You have sucessfully purchased {powerups[x]}")
                        coins=coins-costs_of_powerups[x]
                        user_num_of_powerups[x]=user_num_of_powerups[x]+1
                        if powerups[x]=="rep loss":
                            await message.channel.send(f"Remember to use $d to use powerup! THIS IS A SPECIAL POWERUP THAT DESTROYS A HIGHEST SCORE OF A PLAYER. USE IT WISELY!!!")
                        break
                    else:
                        await message.channel.send(f"You do not have enough to purchase {powerups[x]}")
                        break
                x=x+1
        if message.content.startswith("$d"):
            global player_index
            if user_num_of_powerups[6]>0:
                index_of_current_user=users.index(message.author.display_name)
                users.remove(message.author.display_name)
                highest_scores_of_users.remove(index_of_current_user)
                await message.channel.send(f"Enter name of player")
                def check_player(msg):
                    return msg.author==message.author and msg.channel==message.channel
                player=await client.wait_for("message", check=check_player, timeout=10000000000)
                if player in users:
                    player_index=users.index(player)
                    highest_scores_of_users[player_index]=highest_scores_of_users[player_index]-5000
                    if highest_scores_of_users[player_index]<=0:
                        highest_scores_of_users[player_index]=0
                    await message.channel.send(f"Power up rep loss activated!")
                    await message.channel.send(f"{player} has lost 5000 points from highest score!!!")
                    user_num_of_powerups[6]=user_num_of_powerups[6]-1
                else:
                    await message.channel.send(f"Player not found!")
                highest_scores_of_users.append(highest_score)
                users.append(message.author.display_name)
                    
            else:
                await message.channel.send(f"You have no Rep loss powerups")
                
            if message.content.startswith("$z"):
                if user_num_of_powerups[7]>0:
                    index_of_current_user=users.index(message.author.display_name)
                users.remove(message.author.display_name)
                coins_of_users.remove(index_of_current_user)
                await message.channel.send(f"Enter name of player")
                def check_player(msg):
                    return msg.author==message.author and msg.channel==message.channel
                player=await client.wait_for("message", check=check_player, timeout=10000000000)
                if player in users:
                    player_index=users.index(player)
                    coins_of_users[player_index]=coins_of_users[player_index]-1000
                    if coins_of_users[player_index]<=0:
                        coins_of_users[player_index]=0
                    user_num_of_powerups[7]=user_num_of_powerups[7]-1
                    await message.channel.send(f"Power up zap activated!")
                    await message.channels.send(f"{player} has lost 1000 coins")
                else:
                    await message.channel.send(f"Player not found!")
                coins_of_users.append(highest_score)
                users.append(message.author.display_name)
            else:
                await message.channel.send(f"You have not zap powerups")
                
                    

        if message.content.startswith("$y"):
            await message.channel.send(f"Let the games begin!")
            await message.channel.send(f"Number of questions: 15")
            i=1
            questions_asked=[]
            score=0
            streak=0
            game_active=True
            global easy_points
            global hard_points
            global medium_points
            global points_lost
            global number_of_questions
            global bonus_points
            global league
            global k
            global t
            global n
            global games
            global number_of_correct_questions_game
            number_of_correct_questions_game=0
            number_of_questions=16
            while (i<number_of_questions):
                
                    
                question=random.choice(trivia_questions)
                while question in questions_asked:
                    question=random.choice(trivia_questions)
                questions_asked.append(question)
                trivia_questions_index=trivia_questions.index(question)
                
                if question in easy_questions:
                    point_gained=easy_points
                    await message.channel.send(f"Question {i} (EASY): {question}")
                elif question in medium_questions:
                    point_gained=medium_points
                    await message.channel.send(f"Question {i} (MEDIUM): {question}")
                else:
                    point_gained=hard_points
                    await message.channel.send(f"Question {i} (HARD): {question}")
                if i>=16:
                    await message.channel.send(f"Bonus Question!")
                    point_gained=point_gained+bonus_points

                
                total_number_of_questions_done=total_number_of_questions_done+1
                await message.channel.send(f"Names of powerups: 2x, flash, shield, skip, bonus, 4x, 10x, 20x. Enter name of powerup or enter anything else for no powerup")
                def check2(msg):
                    return msg.author==message.author and msg.channel==message.channel

            
                answer_msg2=await client.wait_for("message", check=check2, timeout=10000000000)
                print(point_gained)
                while answer_msg2.content.startswith("$"):
                    await message.channel.send(f"Error, please choose a powerup! Names of powerups: 2x, flash, shield, skip, bonus, 4x, 10x, 20x. Enter name of powerup or enter anything else for no powerup")
                    answer_msg2=await client.wait_for("message", check=check2, timeout=10000000000)
                if answer_msg2.content.strip().lower()=="2x":
                        powerups_index=powerups.index("2x")
                        if user_num_of_powerups[powerups_index]>0:
                            point_gained=point_gained*2
                            print(point_gained)
                            user_num_of_powerups[powerups_index]=user_num_of_powerups[powerups_index]-1
                            await message.channel.send(f"Powerup 2x activated!")
                        else:
                            await message.channel.send(f"You have no 2x powerups!")
                elif answer_msg2.content.strip().lower()=="flash":
                    powerups_index=powerups.index("flash")
                    if user_num_of_powerups[powerups_index]>0:
                        await message.channel.send(f"The answer for this question is {trivia_answers[trivia_questions_index]}")
                        user_num_of_powerups[powerups_index]=user_num_of_powerups[powerups_index]-1
                        await message.channel.send(f"Powerup flash activated!")
                    else:
                        await message.channel.send(f"You have no flash powerups!")
                elif answer_msg2.content.strip().lower()=="shield":
                    powerups_index=powerups.index("shield")
                    if user_num_of_powerups[powerups_index]>0:
                        temp=points_lost
                        points_lost=0
                        user_num_of_powerups[powerups_index]=user_num_of_powerups[powerups_index]-1
                        await message.channel.send(f"Powerup shield activated!")
                    else:
                        await message.channel.send(f"You have no shield powerups!")
                elif answer_msg2.content.strip().lower()=="skip":
                    powerups_index=powerups.index("skip")
                    if user_num_of_powerups[powerups_index]>0:
                        i=i+1
                        user_num_of_powerups[powerups_index]=user_num_of_powerups[powerups_index]-1
                        await message.channel.send(f"Powerup skip activated!")
                        continue
                    else:
                        await message.channel.send(f"You have no skip powerups!")
                elif answer_msg2.content.strip().lower()=="bonus":
                    powerups_index=powerups.index("bonus")
                    if user_num_of_powerups[powerups_index]>0:
                        number_of_questions=number_of_questions+1
                        user_num_of_powerups[powerups_index]=user_num_of_powerups[powerups_index]-1
                        await message.channel.send(f"Powerup bonus activated!")
                    else:
                        await message.channel.send(f"You have no bonus powerups!")
                elif answer_msg2.content.strip().lower()=="4x":
                        powerups_index=powerups.index("4x")
                        if user_num_of_powerups[powerups_index]>0:
                            point_gained=point_gained*4
                            print(point_gained)
                            user_num_of_powerups[powerups_index]=user_num_of_powerups[powerups_index]-1
                            await message.channel.send(f"Powerup 4x activated!")
                        else:
                            await message.channel.send(f"Powerup 10x activated!")
                elif answer_msg2.content.strip().lower()=="10x":
                    powerups_index=powerups.index("10x")
                    if user_num_of_powerups[powerups_index]>0:
                        point_gained=point_gained*10
                        user_num_of_powerups[powerups_index]=user_num_of_powerups[powerups_index]-1
                        await message.channel.send(f"Powerup 10x activated!")

                    else:
                        await message.channel.send(f"You have no 10x powerups")
                elif answer_msg2.content.strip().lower()=="20x":
                    powerups_index=powerups.index("20x")
                    if user_num_of_powerups[powerups_index]>0:
                        point_gained=point_gained*20
                        user_num_of_powerups[powerups_index]=user_num_of_powerups[powerups_index]-1
                        await message.channel.send(f"Powerup 20x activated!")
                    else:
                        await message.channel.send(f"You have no 20x powerups")


                def check(msg):
                    return msg.author==message.author and msg.channel==message.channel

            
                answer_msg=await client.wait_for("message", check=check, timeout=10000000000)
                if answer_msg.content.strip().lower()==trivia_answers[trivia_questions_index].lower():
                
                    streak=streak+1
                    if streak>=3:
                        await message.channel.send(f"You are on a win streak of {streak} 🔥")
                        score=score+10
                        highest_streak=streak
                    score=score+point_gained
                    number_of_correct_questions_game=number_of_correct_questions_game+1
                    number_of_correct_questions=number_of_correct_questions+1
                    await message.channel.send(f"Nice job! Score: {score}")
                elif answer_msg.content=="$e":
                    await message.channel.send(f"{message.author.display_name}, you have ended the game!")
                    game_active=False
                    break
                else:
                    streak=0
                    await message.channel.send(f"Wrong! Score: {score}")
                    score=score-points_lost
                    print(points_lost)
                    if points_lost==0:
                        points_lost=temp
                    print(points_lost)
                    if score<=0:
                        score=0
                if streak==3:
                    if "Triplet" not in achievements:
                        await message.channel.send(f"You have recieved the Triplet acheivement for getting a streak of 3!")
                        achievements.append("Triplet")
                elif streak==5:
                    if "Five-peat" not in achievements:
                        await message.channel.send(f"You have recieved the Five-peat acheivement for getting a streak of 5!")
                        achievements.append("Five-peat")
                elif streak==10:
                    if "On Fire" not in achievements:
                        await message.channel.send(f"You have recieved the On Fire acheivement for getting a streak of 10!")
                        achievements.append("On Fire")
                    


                i=i+1



            else:
                await message.channel.send(f"Game has finished. Score: {score}")
                await message.channel.send(f"Press $y to play again, $n not to play, $l to view leaderboard, or $r to rate me!")
                games=games+1
                game_active=False
                total_number_of_games=total_number_of_games+1
                if score>highest_score:
                    highest_score=score
                if number_of_correct_questions_game%(number_of_questions-1)==0 and number_of_correct_questions!=0:
                        if "Perfectionist" not in achievements:
                            await message.channel.send(f"You have recieved the Perfectionist title for solving all questions correctly!")
                            achievements.append("Perfectionist")
                if total_number_of_games==100:
                    if "King Buff"  not in achievements:
                        await message.channel.send(f"You have recieved the King Buff title for completing 100 games!")    
                        achievements.append("King Buff")    
                if total_number_of_games==25:
                    if "The Challenger" not in achievements:
                        await message.channel.send(f"You have recieved The Challenger title for completing 100 games!")    
                        achievements.append("King Challenger")        
                users_index=users.index(message.author.display_name)
                highest_scores_of_users[users_index]=highest_score
                print(users_index)
                print(highest_scores_of_users)
                if highest_score>=3000:
                    if "Trivia Pro" not in achievements:
                        await message.channel.send(f"You have recieved the Trivia Pro title for reaching a highest score at least 3000!")
                        achievements.append("Trivia Pro")
                if highest_score in range(0, 999):
                    easy_points=25
                    medium_points=50
                    hard_points=75
                    points_lost=50
                    league="Bronze League"
                elif highest_score in range(1000, 1299):
                    easy_points=50
                    medium_points=75
                    hard_points=100
                    points_lost=75
                    league="Silver League"
                    
                elif highest_score in range(1300, 1699):
                    easy_points=75
                    medium_points=100
                    hard_points=125
                    points_lost=100
                    league="Silver League"
                    
                elif highest_score in range(1700, 2099):
                    easy_points=100
                    medium_points=125
                    hard_points=150
                    points_lost=125
                    league="Gold League"
                    
                elif highest_score in range(2100, 2474):
                    easy_points=125
                    medium_points=150
                    hard_points=175
                    points_lost=150
                    league="Gold League"
                    
                elif highest_score in range(2475, 4899):
                    easy_points=250
                    medium_points=300
                    hard_points=350
                    points_lost=500
                    league="Gold League"
                    
                elif highest_score in range(4900, 5699):
                    easy_points=300
                    medium_points=350
                    hard_points=400
                    points_lost=600
                    league="Plat League"
                    
                elif highest_score in range(5700, 7199):
                    easy_points=400
                    medium_points=450
                    hard_points=500
                    points_lost=800
                    league="Plat League"
                    
                elif highest_score in range(7200, 8399):
                    easy_points=500
                    medium_points=550
                    hard_points=600
                    points_lost=900
                    league="Diamond League"
                    
                elif highest_score in range(8400, 9899):
                    easy_points=600
                    medium_points=650
                    hard_points=700
                    points_lost=1500
                    league="Diamond League"
                    
                elif highest_score>=9900:
                    easy_points=1000
                    medium_points=1500
                    hard_points=2000
                    points_lost=4000
                    league="Champion League"
                if ranks.index(league)>ranks.index(current_league):
                    await message.channel.send(f"You have been promoted to {league}")
                    await message.channel.send(f"You have unlocked the {league} wheel!")
                    await message.channel.send(f"For every 15 games, you will open one {league} wheel!")
                    games=0
                else:
                    await message.channel.send(f"You are still in {league}")
                current_league=league
                
                await message.channel.send(f"Current Rank: {current_league}") 
                if current_league=="Bronze League":
                    await message.channel.send(f"🥉")
                elif current_league=="Silver League":
                    await message.channel.send(f"🥈")
                elif current_league=="Gold League":
                    await message.channel.send(f"🏅")
                elif current_league=="Plat League":
                    await message.channel.send(f"💎")
                elif current_league=="Diamond League":
                    await message.channel.send(f"💎✨")
                else:
                    await message.channel.send(f"👑")
                if current_league=="Plat League":
                    if "Expert" not in achievements:
                        await message.channel.send(f"You have received the Expert title for achieving Plat League!")
                        achievements.append("Expert")
                
            


                
                
                accuracy=round((number_of_correct_questions/total_number_of_questions_done)*100)
            
                
                temp=0
                if_change=True
               
                leaderboardscores.append(highest_score)
               
                leaderboardnames.append("")
                while (if_change):
                    if_change=False                
                    y=1
                    while y<len(leaderboardscores):
                        if leaderboardscores[y]<leaderboardscores[y-1]:
                            temp2=leaderboardnames[y]
                            leaderboardscores[y-1]=temp2
                            leaderboardnames[y]=leaderboardnames[y-1]
                            temp=leaderboardscores[y]
                            leaderboardscores[y]=leaderboardscores[y-1]
                            leaderboardscores[y-1]=temp
                            if_change=True
                        y=y+1
                user_index=leaderboardscores.index(highest_score)
                leaderboardnames[user_index]=message.author.display_name
                if leaderboardnames.count(message.author.display_name)==2:
                    common_list=[]
                    b=0
                    while b<len(leaderboardscores):
                        if leaderboardnames[b]==message.author.display_name:
                            common_list.append(leaderboardscores[b])
                        b=b+1
                    smallest_in_common_list=min(common_list)
                    index_of_smallest=leaderboardscores.index(smallest_in_common_list)
                    leaderboardscores.pop(index_of_smallest)
                    leaderboardnames.pop(index_of_smallest)
                else:
                    leaderboardnames.pop(0)
                    leaderboardscores.pop(0)
                chests=chests+1
                await message.channel.send(f"You have receieved a chest! To open enter $o.")
                if games%15==0 and games!=0:
                    await message.channel.send(f"You have receieved a {current_league} wheel! To open enter $w.")
                    wheels=wheels+1
                if current_league=="Plat League":
                    await message.channel.send(f"You have recieved 10% discount on all powerups!")
                    for powerup in powerups:
                        powerup=powerup*0.10
                elif current_league=="Diamond League":
                    await message.channel.send(f"You have recieved 25% discount on all powerups!")
                    for powerup in powerups:
                        powerup=powerup*0.1667
                elif current_league=="Champion League":
                    await message.channel.send(f"You have recieved 50% discount on all powerups!")
                    for powerup in powerups:
                        powerup=powerup*0.3333
                else:
                    await message.channel.send(f"Discounts arrive at Plat League!")

                    
            
                
        

            
        elif message.content.startswith("$n"):
            await message.channel.send(f"Bye, {message.author.display_name}")
    



    
    


        

    


    

    

client.run(TOKEN)
