# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Simple Calculator
--------------------------------------------------------------------------
License:
Copyright 2018 FRANCISCO MONTANO

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    
1.  Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2.  Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

3.  Neither the name of the copyright holder nor the names of its contributors
may be used to endorse or promote products derived from this software without
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Simple calculator that will
    -  Take in two numbers from the user
    -  Take in an operator from the user
    -  Perform the mathematical operation and provide the number to the user
    -  Repeat

Operations:
    -  addition
    -  subtraction
    -  multiplication
    -  division

Error conditions:
    -  Invalid operator --> Program should exit
    -  Invalid number   --> Program should exit

--------------------------------------------------------------------------
"""

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------

# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

# This function shifts a binary number to the right by y
def right_shift(x, y):
    return x >> y

# This function shifts a binary number to the left by y
def left_shift(x, y):
    return x << y

# This function calculates the modulo of two numbers
def modulo(x, y):
    return x % y

# This function calculates an exponential 
def exponentiate(x, y):
    return x ** y

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Right Shift")
print("6.Left Shift")
print("7.Modulo")
print("8.Exponentiate")
print("Q.Close Calculator")

# Take input from the user 
while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8/Q):")
    
    if choice == 'Q':
        break

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))
        
    elif choice == '2':
        print(num1,"-",num2,"=", subtract(num1,num2))
            
    elif choice == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))
                    
    elif choice == '4':
        print(num1,"/",num2,"=", divide(num1,num2))

    elif choice == '5':
        print(num1,">>",num2,"=", right_shift(num1,num2))

    elif choice == '6':
        print(num1,"<<",num2,"=", left_shift(num1,num2))

    elif choice == '7':
        print(num1,"%",num2,"=", modulo(num1,num2))

    elif choice == '8':
        print(num1,"^",num2,"=", exponentiate(num1,num2))

    else:
       print("Invalid input")
       break

#if __name__ == "__main__":pass
