#!/usr/bin/python3
# This Python file uses the following encoding: utf-8

import string
import sys

# prompt asking user for preferred game difficulty level. play_game()
# runs based off user's decision.
def user_input():
    print("""Welcome to my zoology quiz! Please choose a level:
    \nEASY, \nMEDIUM, \nHARD?""")
    decision = raw_input(" ")
    decision = decision.upper()
    if decision == "EASY":
        print "You've chosen easy! Guess the correct answer"
        "to fill in the blank: "
        print easy
        print play_game(easy, game_words, easy_answers)
    if decision == "MEDIUM":
        print "You've chosen medium! Guess the correct answer"
        "to fill in the blank: "
        print medium
        print play_game(medium, game_words, medium_answers)
    if decision == "HARD":
        print "You've chosen hard! Guess the correct answer"
        "to fill in the blank: "
        print hard
        print play_game(hard, game_words, hard_answers)
    return decision

# A list of replacement words to be passed in to the play game function.
game_words = ["__1__", "__2__", "__3__", "__4__"]

# Paragraph to pass in to the play_game function.
# User will fill in correct answer.
easy = (
    "This Peruvian animal is about six feet tall. "
    "It’s called a __1__. This animal is closely linked to the __2__, "
    "which lives in the Central, South Asia and the Middle East. "
    "This animal's closest cousin is an __3__."
    "This animal __4__ when its mad.")

medium = (
    "This animal, called an __1__ has a leathery banded shell. "
    "The smallest species is called the pink fairy __1__. "
    " The largest species is called the __2__ __1__. This animal's ancestors "
    "are __3__ and sloths, and it originated in South __4__.")

hard = (
    "This spiny nocturnal mammal, called a __1__, lives all over Europe, "
    "Africa, and Asia. This animal shares distant ancestry with another "
    "long-nosed rodent: the __2__. The collective group of this animal "
    "is relevant to programming, and is called an __3__. When the scared, "
    "this animal turns into a tight __4__.")

# Answers for each level
easy_answers = ["llama", "camel", "alpaca", "spits"]
medium_answers = ["armadillo", "giant", "anteaters", "Africa"]
hard_answers = ["hedgehog", "shrew", "array", "ball"]


# Checks to see if user input (i.e. guess) matches the answer
def test(guess, word_to_replace, level_answers):
# Inputs:
#   guess: guess user supplied in play_game() as user_input
#   word_to_replace: the word in the string (i.e. __1__) to be replaced
#   level_answers: the correct answers, based on chosen level
# Behavior:
#   Compares user_input against correct answer for chosen level
# Output:
#   True for success, False otherwise.
    word_no_punctuation = word_to_replace.translate(None, string.punctuation)
    replacement_word = int(word_no_punctuation) - 1
    count = 0
    while (count < 1):
        if guess == level_answers[replacement_word]:
            print "correct answer! Your answer so far: "
            return True
        else:
            print "your answer was incorrect! Try again."
            "You have one more guess."
            return False
        count = count + 1


# If user guesses incorrectly, gives user one more try
def incorrect_answer(guess, word_to_replace, level_answers):
    word_no_punctuation = word_to_replace.translate(None, string.punctuation)
    replacement_word = int(word_no_punctuation) - 1
    if guess == level_answers[replacement_word]:
        print "correct answer! Your answer so far: "
        return True
    else:
        print "I'm sorry, your answer was incorrect! Game Over."
        sys.exit(0)


# A player is prompted to replace words in mad_lib with their own words.
def play_game(mad_lib, parts_of_speech, answers):
    current_answer = mad_lib
    mad_lib = mad_lib.split()
    for game_word in game_words:
        user_input = raw_input(
            "What should be substituted in for:"
            " " + game_word + " ")
        guess = user_input
        result = test(guess, game_word, answers)
        if result is False:
            guess = raw_input(
                "What should be substituted in for:"
                " " + game_word + " ")
            result = incorrect_answer(guess, game_word, answers)
        current_answer = current_answer.replace(game_word, guess)
        print current_answer
    print 'Congrats! Your result: '
    return current_answer

user_input()
