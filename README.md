# ASN-DSAT5-IP
ASN DSA T5: Introduction to Python classes

## Class 01 (2025-02-24)
Beginners guide on python with some exercises.

### Class codes:
- 01_hello_world.py
- 02_hello_name.py
- 03_story.py
- 04_variables.py
- 05_input.py

### Class exercises:
1. Create a code that wishes good morning.
    - ex_01.py

2. Create a code that wishes good morning, asks the person's name and answers that it is a pleasure to meet her, mentioning the person's name.
    - ex_02.py

3. Create a simple story. Add this story to a program. At each paragraph, the story should wait for the user to press "enter" to continue.
    - ex_03.py

4. Create a program that receives an integer and calculates its square root and displays the result.
    - ex_04.py

5. Create a program that displays twice a number entered by the user.
    - ex_05.py

6. Create a program that displays the following chocolate cake recipe (PT-BR). Display one item at a time, as the person presses "enter".
    - ex_06.py



## Class 02 (2025-02-26)
Conditional clauses: IF, ELIF, ELSE

### Class codes:
- 01_calculations.py
- 02_bool.py
- 03_drinking.py

### Class exercises:
1. Create a program that sells a bottle of water:
    a. If the customer chooses natural mineral water, it will be charged `R$1.50` 
    b. If the customer chooses mineral water with gas, it will be charged `R$2.50`
    - ex_01.py

2. Change the previos code considering the quantity of water bottles.
    - ex_01.py

3. Create a code of a Ice-Cream Store, where the user can choose:
    a. Type of ice-cream: cone (`R$1.00`), large cone (`R$2,50`), basket (`R$4,00`)
    b. Flavor of ice-cream: strawberry, vanilla, chocolate
    c. Syrup: caramel (`R$1,50`), strawberry (`R$1,50`), chocolate (`R$1,50`), no syrup (`R$0,00`)
    d. Present the total to be paid.
    - ex_03.py

4. Create a code that checks if a person belongs to the "calvo" family.
    - ex_04.py

5. Create a code that checks if a persons belongs to the "calvo" or "silva" family.
    - ex_05.py

6. Create a code that checks if the item that a person selected to buy at the store is one of the following: orange, beer, instant noodles, coal, rump steak.
    - ex_06.py

## Class 03 (2025-03-10)
Loops: WHILE, FOR

### Class codes:
- 01_loops.py
- 02_while.py
- 03_for.py

### Class Exercise
1. Create a script that counts how many times the letter "a" appears in the word.
    - ex_01.py

2. Write a program that receives 4 height values using a loop and calculates their sum.
    - ex_02.py

3. Write a program that receives an indefinite number of values corresponding to "account balance." However, when the user presses "Enter" without entering any value, the program stops receiving inputs and displays the sum of all previously entered values.
    - ex_03.py

# Class 04 (2025-03-12)
LIST, SLICE, DICTIONARY

# Class codes:
- 01_lists.py
- 02_slice.py
- 03_methods.py
- 04_dictionaries.py
- 05_loops.py

### Class Exercise
- ex_01.py

## Homework

### Part 1
#### 1.1 Write a program that receives a person's name and displays a greeting.
` "Hello [name]! Welcome!" `
- ex_P1-01.py

#### 1.2 Write a program that receives a person's name and age. Then, display the message:
` "Hello [name], good to know you are [x] years old. Welcome!" `
- ex_P1-02.py

#### 1.3 Write a program that receives the radius of a circle in centimeters. Return to the user the area and perimeter of this circle in the following format:
` Area:  x.xx `
` Perimeter:  y.yy `
- ex_P1-03.py

#### 1.4 Write a program that receives two values, A and B. Calculate the sum of these two values and return the result:
` Sum:  x.xx `
- ex_P1-04.py

#### 1.5 Write a program that receives two values, A and B. Calculate the power of these two values and return the result:
` a ^ b = z `
- ex_P1-05.py

#### 1.6 Write a program that receives a number in seconds, converts this number to hours, minutes, and seconds. Examples:
` Input: 556 `
` Output: 0:9:16 `

` Input: 140153 `
` Output: 38:55:53 `
- ex_P1-06.py

### Part 2
#### 2.1 Write a program that receives a person's name and age.
If the person is under 18 years old, display the message:
` "John, you cannot drive or drink." `
For people between 18 and 65 years old, display:
` "John, drinking is allowed! Just don’t drive!" `
For people over 65 years old, display:
` "John, drink with great moderation!" `
- ex_P2-01.py

#### 2.2 Write a program that receives a number. Check if the given number is even or odd. Display the result as follows:
` "The number x is odd." `
` "The number x is even." `
- ex_P2-02.py

#### 2.3 Write a program that asks the user for a name and age and creates a dictionary with this information. Then, display the dictionary.
- ex_P2-03.py

#### 2.4 Write a program that receives 4 student grades. Return the average of these grades, the lowest, and the highest grade:
` Average: x `
` Lowest: y ` 
` Highest: z ` 
- ex_P2-04.py

#### 2.5 Consider the following list:
` [120, “Python”, 120.01, “asw”, False, [10,20]] `
Write a program that returns the following information:
- The element at position -1 in the list
- The element in the first position of the list
- The last character of the second element in the list

` Element -1: x `
` First element: y `
` Last character of the second element: z `
- ex_P2-05.py

#### 2.6 Write a program that asks the user for two strings and concatenates them into a single string. Then, display the resulting string.
- ex_P2-06.py

#### 2.7 Ask the user for the name of a fruit and display the corresponding price.
- Apple: R$1.50
- Banana: R$2.75
- Grape: R$1.90
- Pear: R$1.25
- Orange: R$0.65
- Lemon: R$1.25
- Guava: R$2.15
- Pineapple: R$3.20
- Jackfruit: R$5.80

- ex_P2-07.py

#### 2.8 Redo exercise 2.4, but use a for loop and lists to receive the student’s grades.
- ex_P2-08.py

#### 2.9 Write a program that receives a number. Check whether this number is prime or not and return the result:
` "The number x is prime." ` or ` "The number x is not prime." `

#### 2.10 Write a program that receives a number. This number corresponds to a position in the Fibonacci sequence: 1, 1, 2, 3, 5, ...
Display the Fibonacci number that corresponds to the given position:
` “Position x corresponds to the number y.” `

#### 2.11 Write a program with a function that receives a sentence. For each word in the sentence, reverse the order of the letters. Display the result:
` This is the original sentence. `
` sihT si eht lanigiro ecnetnes. `

#### 2.12 Write a program that displays numbers from 1 to 100.
- If the number is divisible by 3, display "**Fizz**". 
- If the number is divisible by 5, display "**Buzz**". 
- If the number is divisible by both, display "**FizzBuzz**".

#### 2.13 Write a program that receives a number and displays its factorial.

#### 2.14 Consider the following list:
[123, 435, 987, 1984, 2, 19, 423, -178, 320]
Write a program that returns the **position** of the smallest and largest values in the list:
` The highest value is at position x. `
` The lowest value is at position y. `

#### 2.15 Write a program that receives a list of numbers from the user and counts how many times a specific number appears in the list. Ask the user for a number and display the count.

#### 2.16 Write a program that asks the user for a number and displays its multiplication table from 1 to 10.

#### 2.17 Write a program that asks the user for a word and checks whether it is a palindrome (i.e., the same word when read backward).

#### 2.18 Write a program that asks the user for sentences. To stop, the user can simply press "Enter" without typing anything.
Your program should display each sentence and how many times it was repeated.



### Challenge
1. Babylon Lottery
Build a program that randomly draws a number between 1 and 15.
The user has 3 chances to guess the number.
After each attempt, inform whether the guess is higher or lower than the drawn number.
If the user guesses correctly, congratulate them!

2. Babylon Lottery v2
Modify the previous challenge to use Streamlit for the interface.
