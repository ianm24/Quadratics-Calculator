# -*- coding: utf-8 -*-
import math

def quad():
    #Asks for coefficients in Y = AX² + BX + C
    fA = raw_input("What is A?")
    while fA == "":
        fA = raw_input("What is A?")

    A = float(fA)

    fB = raw_input("What is B?")
    while fB == "":
        fB = raw_input("What is B?")

    B = float(fB)

    fC = raw_input("What is C?")
    while fC == "":
        fC = raw_input("What is C?")

    C = float(fC)
    
    while A == 0:
    	A = float(raw_input("A cannot be 0. Choose another number."))
    #Calculates needed values
    D = (B / (2 * A))
    E = (A * (D) ** 2 + (B * (D)) + (C))
    P = ((1 / A) / 4)
    
    #Equation in Y = AX² + BX + C form
    print(" " + '\n' + "Equation:" + '\n' + "Y = " + str(A) + "X² + " + str(B) + "X + " + str(C) + '\n')
    
    #Quadratic Equation Form
    print(" " + '\n' + "Quadratic Equation:")
    if ((B ** 2) - (4 * A * C)) < 0:
        if isinstance(math.sqrt((-1 * ((B ** 2) - (4 * A * C)))), int):
            print("     " + "-" + str(B) + " " + "±" + str(math.sqrt(-1 * ((B ** 2) - (4 * A * C)))) + "i" + '\n' + "X = " + "------------------" + '\n' + "          " + str(2 * A))
        else:
            print("     " + "-" + str(B) + " " + "±" + "√(" + str((-1 * ((B ** 2) - (4 * A * C)))) + ")" + "i" + '\n' + "X = " + "------------------" + '\n' + "          " + str(2 * A))
    elif isinstance(math.sqrt(((B ** 2) - (4 * A * C))), int):
        print("     " + "-" + str(B) + " " + "±" + str( math.sqrt((B ** 2) - (4 * A * C))) + '\n' + "X = " + "------------------" + '\n' + "          " + str(2 * A))
    else:
        print("     " + "-" + str(B) + " " + "±" + "√(" + str(((B ** 2) - (4 * A * C))) + ")" + '\n' + "X = " + "------------------" + '\n' + "          " + str(2 * A))
    
    #Standard Form Equation
    print(" " + '\n' + "Standard Form:" + '\n' + "Y = " + str(A) + "(X + " + str(B / 2 * A) + ")" + "² + " + str(C - (B ** 2 / (4 * A ))))

    #Standard Conic Equation
    print(" " + '\n' + "Standard Conic Form:" + '\n' + "(x - " + str(D) + ")² = 4*" + str(P) + "(y - " + str(E) + ")")

    #Vertex
    print(" " + '\n' + "Vertex:" + '\n' + "(" + str(D) + "," + str(E) + ")")
    
    #Focus
    print(" " + '\n' + "Focus:" + '\n' + "(" + str(D) + "," + str(E + P) + ")")

    #Y-Intercept
    print(" " + '\n' + "Y-Int:" + '\n' + "(" + "0" + "," + str(C) + ")")
    
    #Axis of Symmetry
    print(" " + '\n' + "AOS:" + '\n' + "X = " + str(D))

    #Directrix
    print(" " + '\n' + "Directrix:" + '\n' + "Y = " + str(E - P))
    
    #Relative Maximum/Minimum
    if A < 0:
        print(" " + '\n' + "Relative Maximum:" + '\n' + "Y = " + str(E))
    else:
        print(" " + '\n' + "Relative Minimum:" + '\n' + "Y = " + str(E))
 
#Runs the program   
quad()
