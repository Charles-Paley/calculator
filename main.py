from math import *
import math


question = input("Enter Sine, Cosine, Tangent, Square Root, Type 1 for 4 operations: ")

if question == "sine":
    sine_num = input("put the number you want to sine here: ")
    sine_num = float(int(sine_num))
    result_sine = (math.sin(float(int(sine_num))))
    print(result_sine)

if question == "cosine":
    cosine_num = input("put the number you want to cosine here: ")
    cosine_num = float(int(cosine_num))
    result_cosine = (math.cos(float(int(cosine_num))))
    print(result_cosine)

if question == "tangent":
    tangent_num = input("put the number you want to Tangent here: ")
    tangent_num = float(int(tangent_num))
    result_tangent = (math.tan(float(int(tangent_num))))
    print(result_tangent)

if question == "Square Root":
    squareroot_num = input("put the number you want to get the Square Root of here: ")
    squareroot_num = float(int(squareroot_num))
    result_squareroot = (math.sqrt(float(int(squareroot_num))))
    print(result_squareroot)





toehead = input("Your First Number Here: ")
operation = input("Put the operation here: ")
toehead2 = input("Put Your Second Number Here: ")

if operation == "+":
    answer_1 = float(toehead) + float(toehead2)
    print(answer_1)

if operation == "-":
    answer_2 = float(toehead) - float(toehead2)
    print(answer_2)

if operation == "*":
    answer_3 = float(toehead) * float(toehead2)
    print(answer_3)

if operation == "/":
    answer_4 = float(toehead) / float(toehead2)
    print(answer_4)








