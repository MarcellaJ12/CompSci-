information = [ ]

#
print("Loading...")
#
print("Welcome, user.")
username = input("Please type in a username of your choice \n")
print(username)
information.append(username)
random = input("Is this you username? \n")

if random == "No" or "no":
    information.remove(username)
    username = input("change for the username \n")
    print(f"Your new username is {username}")
    information.append(username)
else:
    print("Alright. thank you.")


password = input("great choice. Please also set a password to protect your account \n")
print(password)
information.append(password)
random1 = input("Is this you password? \n")

if random1 == "No" or "no":
    information.remove(password)
    password = input("change for the password \n")
    print(f"Your new username is {password}")
    information.append(password)
else:
    print("Alright. thank you.")


#Loading screen (supposedly)
print("Registering...")
print(f"\n Hello, {username}. Glad to meet you.") 

insignificant = input("Can I ask you some questions to further get to know you more?\n")

if insignificant == "yes":
    print("Great. Let's begin.\n")
elif insignificant == "no":
    print(f"Apologies, but these questions are asked to get a better knowledge of you, {username}. \n")

eyesight = input("First of all, do you have normal eyesight? or are you Hyperopia or Myopia? \n")

#most glasses users have eyesight problem
if eyesight == "Normal":
    print("Ah, I see. Thank you for telling me that. That makes my job much easier.\n")
elif eyesight == "Hyperopia":
    print("I see. I will turn on a filter just for you, so you won't be needing your normal glasses. You should thank me for being so kind. :D. \n")
elif eyesight == "Myopia":
    print("I see. I will turn on a filter just for you, so you won't be needing your normal glasses. You should thank me for being so kind. :D. \n")
else:
    print("Ah, my apologies, I forgot that some people don't use these medical terms when refering to it. Let me give a lighter definition. \n")
    print("Hyperopia means farsightedness. Myopia means nearsightedness")
    eyesight = input("So, what is your eyesight? \n")

information.append(eyesight)

print("Alright, thank you for your answer. Moving on to the next one.")
#good for filtering color that might hurt your eye
colorcoating = input("Would you like any eye lens color coating? We have the colors black, brown and blue. \n")

if colorcoating == "Blue" or "Black" or "Brown":
    print("Good choice. Thank you for following my suggestion :D\n")
elif coating == "None" or "none":
    print("Noted.")
else:
    #judging the user
    print("Umm. Weird choice but we do have that color. Alright I'll set tour lenses to that color now. \n")

information.append(colorcoating)

#some users may desire these features
coating = input("We also offer some other features like anti-reflective, scratch-resistant and ultraviolet protection. Would you like to implement any of them? \n")

if coating == "anti-reflective" or "Anti-reflective" or "Anti-Reflective" or "scratch-resistant" or "Scratch-resistant" or "Scratch-Resistant" or "ultraviolet protection" or "Ultraviolet protection" or "Ultraviolet Protection":
    #happy because the AI is able to help the user
    print("Alright thank you for choosing a feature :D")
elif coating == "None" or "none":
    #AI learning about the user
    print("Noted. You don't like these kinda of features?")
else:
    #AI feeling sorry for not being able to help
    print("Sorry we don't provide that features. I'll still put it in so that it can be updated to your choice once the upgrade comes up \n")

information.append(coating)

frame = input("Any changes to the frame shape that you prefer?")

#curiosity
print("Ooh, nice choice, but I do wonder if your choice have a reflection of your personality.")

information.append(frame)
#change of color might reflect user personality
frame_color = input("Any changes to the color of the frame that you prefer?")

#judging
print(f"Noted. {frame} and {frame}, huh. What an interesting combination")

information.append(frame_color)

print("Alright, enough of the boring questions. Let's ask something mroe interesting. \n")
#scenery also reflect personality sometimes. mostly to be able to display the scenery though
scenery = input("What kind of sceneries do you like? Here are some examples to help you :")

#to show that the AI is curious
print("Interesting choice. I am curious as to why you choose that but we'll save that question for another time")

information.append(scenery)

timeofday = input("I see, I see. Then at what time of the day would you like " + scenery + " to be in?")

print("Alright then. Thank you for answering all the questions.")

information.append(timeofday)

print("Unfortunately, we'll have to shut down for a moment to implement all the changes. Apologies for the inconvenience")

print("Here are the changes you have made. In total there are about " +len.information+ " changes made.")
print(information)
#I wanted to use a chinese name
print("Thank you for using 智能眼镜 (Zhìnéng yǎnjìng). I hope we meet again soon")