import time
import random

import difflib
sentences = [
    "Student name"
    "Student Age"
    "Where they Live"
    "Student Gender"
    "Previous Schools"
    "Past Record"
    "Welcome to this school"
    "Teacher Gender"
    "Teacher Classes"
    "Teacher Record"
    "School fees"
    "School Location"
    "School Creation"
]

def Ola():
    print("Welcome to this school!/n")
    sentence = random.choice(sentences)
    print("Where do you live:")
    print(f"/n>>>{sentence}/n")
    input("Answer the question to determine whether you require bussing")
    start_time = time.time()
    typed = input ("|n Address:/n>>>")
    end_time=time.time

    words = len(sentence.split())
    wpm = round((words / time_taken) * 60)
    matcher = difflib.SequenceMatcher(None, sentence, typed)
    accuracy = round(matcher.ratio()*100, 2)

    print("\n--- final Results ---")
    print("Time taken: {} seconds".format(round(time_taken, 2)))
    print(f"Your speed: {wpm} WPM")
    print(f"Accuracy: {accuracy}%")
Ola()
