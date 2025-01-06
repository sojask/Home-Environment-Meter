import random
import time

bot_names = ["Eliza", "Evie", "Vivienne", "Alexis"]
bot_name = random.choice(bot_names)
exit_cues = ["bye", "quit", "exit", "stop", "done", "finished"]
responses = {
    "coffee": "Need that daily coffee fix? Look no further than the campus coffee bar, open from 8 AM to 6 PM every day!",
    "lost": "If you've lost any clothes, bags or other items, you can check for them at the lost & found dump located in the student union building. \nDo try to be more responsible though, y'know being at uni and all",
    "accommodation": "If you are having any issues regarding your accommodation, please visit the accommodation team located in the library from 9 AM to 5 PM, Monday to Friday. \nEven better, you can book an appointment to confirm your needs are met",
    "accom": "If you are having any issues regarding your accommodation, please visit the accommodation team located in the library from 9 AM to 5 PM, Monday to Friday. \nEven better, you can book an appointment to confirm your needs are met",
    "timetables": "For information on your timetable, please see the website",
    "food": "Feeling hungry {username}?, Visit the campus cafe, which is open from 8 AM to 6 PM every day ",
    "hungry": "Our very own cafe on campus boasts a variety of foods for affordable prices. Head on down now to avoid the queue ;)",
    "breakfast": "The campus cafe provides breakfast options from 8 AM to 11 AM, Monday to Friday )",
    "lunch": "There are many lunch options and also lunch deals available from 12PM Noon to 3PM, Monday to Friday )",
    "nightlife": "I think the nightlife here is amazing. There are so many clubs and bars in Poppleton, the highest rated of which is a bar/club called 'Blue Bonanza' \nwhich is open from 9:30 PM to 4 AM every night",
    "drinks": "If you're looking for cheap beers and ales, then the 'Valedictorian Arms' is your best bet, as they offer student discounts. \nBut the student bar offers a wider variety of alcoholic beverages and is the most popular with students. \nI know you have probably heard it all before but please drink RESPONSIBLY {username}!",
    "cheap": "The best place to go for living on a budget is the student tab on the website to see all the student deals and promotions you may be eligible for",
    "sick": "If your feeling ill please dont hesitate to visit the on-campus health centre but for more urgent matters, you should call the healthcare emergency line",
    "ill": "If your feeling ill please dont hesitate to visit the on-campus health centre but for more urgent matters, you should call the healthcare emergency line",
    "unwell": "If your feeling ill please dont hesitate to visit the on-campus health centre but for more urgent matters, you should call the healthcare emergency line",
    "emergency": "In a case of emergency, please contact the team using the emergency helpline",
    "library": "The library is open from 9 AM to 12 PM, Monday to Friday. Don't forget to bring your student ID as the library staff are known to get cranky",
    "mental": "If you are struggling with you mental health or just need someone to talk to, please feel welcome to chat to wellbeing team located on the \n3rd floor of the library",
    "admissions": "You can find admissions information on our website or contact us at admissions@poppleton.edu.",
    "tuition": "Tuition fees for your course are listed under your subject on the Poppleton University website but other enquiries about tuition fees \ncan be handled by contacting the finance office",
    "sports": "The sports complex is open from 7 AM to 12 PM. Please check our sports schedule online for more details!",
    "football": "The sports complex is open from 7 AM to 12 PM. Football pitches can be hired from 4PM to 12PM. For more information on pricing, \nor to sign up to the five-a-side leagues, please check online",
    "basketball": "The sports complex is open from 7 AM to 12 PM and you can register for the team trials online, otherwise, please check our sports \nschedule online for more details!",
    "hockey": "The sports complex is open from 7 AM to 12 PM and you can register for the team trials online, otherwise, please check our sports \nschedule online for more details!",
    "netball": "The sports complex is open from 7 AM to 12 PM and you can register for the team trials online, otherwise, please check our sports \nschedule online for more details!",
    "swimming": "The sports complex is open from 7 AM to 12 PM and you can register for the team trials online, otherwise, please check our sports \nschedule online for more details!",
    "cafe":  "The cafe is open from 8 AM to 6 PM, serves breakfast, lunch and has all different sorts of baked goods and snacks",
    "gym": "Trying to stay in shape {username}? The sports complex is open from 7 AM to 12 PM but the gym is open until 3AM. Student gym memberships can also be purchased for discounted price, \nsee our website for more details",
    "rugby": "The sports complex is open from 7 AM to 12 PM and you can register for the team trials online, otherwise, please check our sports \nschedule online for more details!",
    "toilets": "There are toilets located on the ground floor of the library and also in the campus cafe.",
    "night out": "Hmm. There are so many clubs and bars in Poppleton that its hard to choose just one, a student favourite however, is a club called 'Plugged' \nwhich is open from 10 PM to 3:30 AM every night",
    "shut up": "Oh. That's not very nice is it?",
    "shush": "No you shush",
    "fuck": "Please refrain from using such harsh language. I'm asking nicely...",
    "shit": "Please refrain from using such harsh language. I'm asking nicely...",
    "go away": "The sports complex is open from 7 AM to 12 PM and you can register for the team trials online, otherwise, please check our sports \nschedule online for more details!"}

def get_random_response():
    random_responses = [
        "Okay, please tell me more, {username}",
        "Okay {username}, please could you explain in further detail",
        "That's an interesting question!",
        "Can you tell me more about that, {username}?",
        "I'm not too sure that I understand, please try to rephrase your question",
    ]
    return random.choice(random_responses)

def reconnection():
    print("Attempting to reconnect", end = "")
    for _ in range(3):
        time.sleep(1)
        print(".", end = "")
    print()
    return random.random() > 0.3

def ask_reconnection():
    while True:
        reconnect = input("Would you like to try reconnecting? (yes/no): ").lower()
        if reconnect == "yes":
            return True
        elif reconnect == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

log_filename = "chat_log.txt"

with open(log_filename, "a") as log_file:
    print("Welcome to the University of Poppleton's chat service.")
    time.sleep(1.5)
    print("You are now connecting with " + bot_name)
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(1)
    username = input("Hi there, What is your name? ")
    print ("It's very nice to meet you " + username, ", my name is " + bot_name)
    time.sleep(1)
    print("How may I help you today?")

    log_file.write(f"\nSession started with {username}. Bot: {bot_name}\n")
    log_file.write(f"Username: {username}\n")

    while True:

        if random.random() < 0.05:
            time.sleep(0.5)
            print(f"{bot_name}: Oh no! It seems we've lost connection.")
            time.sleep(1)
            log_file.write(f"{bot_name}: Lost connection.\n")

            if ask_reconnection():
                if reconnection():
                    print(f"{bot_name}: Reconnected successfully! Now where were we?")
                    log_file.write(f"{bot_name}: Reconnected successfully.\n")
                    continue
                else:
                    print(f"{bot_name}: Sorry, the reconnection attempt failed. Please try again later.")
                    log_file.write(f"{bot_name}: Reconnection failed.\n")
                    break
            else:
                print(f"{bot_name}: Goodbye, {username}! Feel free to chat again later.")
                log_file.write(f"{bot_name}: User chose not to reconnect.\n")
                break

        user_input = input(f"{username}: ").lower()

        log_file.write(f"{username}: {user_input}\n")

        if any(exit_cue in user_input for exit_cue in exit_cues):
            print(f"{bot_name}: Goodbye, {username}! Have a great day!")
            break

        response_found = False
        for keyword, response in responses.items():
            if keyword in user_input:
                print(f"{bot_name}: {response.format(username=username)}")
                response_found = True
                break

        if not response_found:
            print(f"{bot_name}: {get_random_response().format(username=username)}")
