import time
import random
import difflib

sentences = [
    "I love learning Oranges"
    "I like cows and goats"
    "I like basketball"
    "I go to School"
    "I do coding"
    "I do not like blueberries"
    "Python is a type of code",
]

print("Welcome to the typing tutor!/n")
sentence = random.choice(sentences)
print("Type this sentence:")
print(f"/n>>>{sentence}/n")
input("Press enter when you are ready to start the typing game")
start_time = time.time()
typed = input ("|n begin typing:/n>>>")
end_time = time.time

words = len(sentence.split())    
wpm = round((words / time_taken) * 60)
matcher = difflib.SequenceMatcher(None, sentence, typed)
accuracy = round(matcher.ratio()*100, 2)

print("\n--- final Results ---")
print("Time taken: {} seconds".format(round(time_taken, 2)))
print(f"Your speed: {wpm} WPM")
print(f"Accuracy: {accuracy}%")
