#!/usr/bin/env python3
import random
import sys
import subprocess

#This function was copy / pasted from StackOverflow and I'm fine with it.
def getInput(prompt):
    sys.stdin = open("/dev/tty", "r")
    command = f"read -p \"{prompt}\" ret && echo \"$ret\""
    userInput = subprocess.check_output(command, shell=True, stdin=sys.stdin).rstrip().decode("utf-8")
    return userInput

quizzData = {
    'How many unicast IPv4 addresses are possible?': '2^32',
    'What is the name of the concept that describes a system\'s ability to adapt to varying workloads or evolve over time?': 'Scalability',
    'What is the maximum value of a byte in hexadecimal notation?': 'FF'
}

wrongAnswer = (
    'Sorry, you dont have the brain to make this commit',
    'Wrong answer, a process has been launched to rm -rf * the project and force push in 1 minute',
    'Maybe one day you will commit...',
    'Good answ.. Oh sorry my bad ! No commit for monkeys',
    'Can I get some burger ? With some peanut butter...'
)

question, answer = random.choice(list(quizzData.items()))
wrongAnswerStr = random.choice(wrongAnswer)

userAnswer = getInput(question + ' : ')

if userAnswer.lower() != answer.lower():
    print(wrongAnswerStr)
    exit(1)

exit(0)