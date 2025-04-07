# ASN-DSAT5-IP
ASN DSA T5: Introduction to Python classes

## PYTHON BASE

### Class 01 (2025-02-24)
Beginners guide on python with some exercises.

#### Class codes:
- 01_hello_world.py
- 02_hello_name.py
- 03_story.py
- 04_variables.py
- 05_input.py

#### Class exercises:
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

### Class 02 (2025-02-26)
Conditional clauses: IF, ELIF, ELSE

#### Class codes:
- 01_calculations.py
- 02_bool.py
- 03_drinking.py

#### Class exercises:
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

### Class 03 (2025-03-10)
Loops: WHILE, FOR

#### Class codes:
- 01_loops.py
- 02_while.py
- 03_for.py

#### Class Exercise
1. Create a script that counts how many times the letter "a" appears in the word.
    - ex_01.py

2. Write a program that receives 4 height values using a loop and calculates their sum.
    - ex_02.py

3. Write a program that receives an indefinite number of values corresponding to "account balance." However, when the user presses "Enter" without entering any value, the program stops receiving inputs and displays the sum of all previously entered values.
    - ex_03.py

### Class 04 (2025-03-12)
LIST, SLICE, DICTIONARY

#### Class codes:
- 01_lists.py
- 02_slice.py
- 03_methods.py
- 04_dictionaries.py
- 05_loops.py

#### Class Exercise
- ex_01.py

### Class 05 (2025-03-17)
FUNCTIONS, LIBRARIES

#### Class codes:
- 01_functions.py
- 02_args.py
- 03_list_unpack.py
- 04_modules.py
- 05_loops.py

#### Class Exercise
- ex_01.py
- ex_02.py


---

### Homework

#### Part 1
##### 1.1 Write a program that receives a person's name and displays a greeting.
` "Hello [name]! Welcome!" `
- ex_P1-01.py

##### 1.2 Write a program that receives a person's name and age. Then, display the message:
` "Hello [name], good to know you are [x] years old. Welcome!" `
- ex_P1-02.py

##### 1.3 Write a program that receives the radius of a circle in centimeters. Return to the user the area and perimeter of this circle in the following format:
` Area:  x.xx `
` Perimeter:  y.yy `
- ex_P1-03.py

##### 1.4 Write a program that receives two values, A and B. Calculate the sum of these two values and return the result:
` Sum:  x.xx `
- ex_P1-04.py

##### 1.5 Write a program that receives two values, A and B. Calculate the power of these two values and return the result:
` a ^ b = z `
- ex_P1-05.py

##### 1.6 Write a program that receives a number in seconds, converts this number to hours, minutes, and seconds. Examples:
` Input: 556 `
` Output: 0:9:16 `

` Input: 140153 `
` Output: 38:55:53 `
- ex_P1-06.py

#### Part 2
##### 2.1 Write a program that receives a person's name and age.
If the person is under 18 years old, display the message:
` "John, you cannot drive or drink." `
For people between 18 and 65 years old, display:
` "John, drinking is allowed! Just don’t drive!" `
For people over 65 years old, display:
` "John, drink with great moderation!" `
- ex_P2-01.py

##### 2.2 Write a program that receives a number. Check if the given number is even or odd. Display the result as follows:
` "The number x is odd." `
` "The number x is even." `
- ex_P2-02.py

##### 2.3 Write a program that asks the user for a name and age and creates a dictionary with this information. Then, display the dictionary.
- ex_P2-03.py

##### 2.4 Write a program that receives 4 student grades. Return the average of these grades, the lowest, and the highest grade:
` Average: x `
` Lowest: y ` 
` Highest: z ` 
- ex_P2-04.py

##### 2.5 Consider the following list:
` [120, “Python”, 120.01, “asw”, False, [10,20]] `
Write a program that returns the following information:
- The element at position -1 in the list
- The element in the first position of the list
- The last character of the second element in the list

` Element -1: x `
` First element: y `
` Last character of the second element: z `
- ex_P2-05.py

##### 2.6 Write a program that asks the user for two strings and concatenates them into a single string. Then, display the resulting string.
- ex_P2-06.py

##### 2.7 Ask the user for the name of a fruit and display the corresponding price.
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

##### 2.8 Redo exercise 2.4, but use a for loop and lists to receive the student’s grades.
- ex_P2-08.py ❌

##### 2.9 Write a program that receives a number. Check whether this number is prime or not and return the result:
` "The number x is prime." ` or ` "The number x is not prime." `
- ex_P2-09.py

##### 2.10 Write a program that receives a number. This number corresponds to a position in the Fibonacci sequence: 1, 1, 2, 3, 5, ...
Display the Fibonacci number that corresponds to the given position:
` “Position x corresponds to the number y.” `
- ex_P2-10.py

##### 2.11 Write a program with a function that receives a sentence. For each word in the sentence, reverse the order of the letters. Display the result:
` This is the original sentence. `
` sihT si eht lanigiro ecnetnes. `
- ex_P2-11.py

##### 2.12 Write a program that displays numbers from 1 to 100.
- If the number is divisible by 3, display "**Fizz**". 
- If the number is divisible by 5, display "**Buzz**". 
- If the number is divisible by both, display "**FizzBuzz**".

- ex_P2-12.py

##### 2.13 Write a program that receives a number and displays its factorial.
- first try: class05 > class_exercise > ex_01.py
- ex_P2-13.py

##### 2.14 Consider the following list:
[123, 435, 987, 1984, 2, 19, 423, -178, 320]
Write a program that returns the **position** of the smallest and largest values in the list:
` The highest value is at position x. `
` The lowest value is at position y. `

- ex_P2-14.py

##### 2.15 Write a program that receives a list of numbers from the user and counts how many times a specific number appears in the list. Ask the user for a number and display the count.
- ex_P2-15.py

##### 2.16 Write a program that asks the user for a number and displays its multiplication table from 1 to 10.
- ex_P2-16.py

##### 2.17 Write a program that asks the user for a word and checks whether it is a palindrome (i.e., the same word when read backward).

- ex_P2-17.py

##### 2.18 Write a program that asks the user for sentences. To stop, the user can simply press "Enter" without typing anything.
Your program should display each sentence and how many times it was repeated.

- ex_P2-18.py

#### Challenge
1. Babylon Lottery
Build a program that randomly draws a number between 1 and 15.
The user has 3 chances to guess the number.
After each attempt, inform whether the guess is higher or lower than the drawn number.
If the user guesses correctly, congratulate them!
- first try: class05 > class_exercise > ex_02.py

2. Babylon Lottery v2
Modify the previous challenge to use Streamlit for the interface.

---
---

## PANDAS BASE

### Class 06 (2025-03-19)

#### Modules:
##### 1. Important objects in Pandas
- Series
- Dataframes

##### 2. Importing files with Pandas
- csv
- xlsx
- parquet

##### 3. Browsing through the data
- Basic information
- Column types
- Browsing into rows and columns
- Renaming columns

#### Class codes:
- 01_series.py
- 02_dataframe.py
- 03_revision.py
- 04_files.py
- 05_utils.py

#### Class Exercise
- ex_02.py
- ex_03-01.py
- ex_03-02.py
- ex_03-03.py
- ex_03-04.py
- ex_03-05.py

### Class 07 (2025-03-24)

#### Modules:
##### 4. Filtering the data
- Logic conditions

##### 5. Transformation and deletion
- Creating new columns
- Ordering

#### Class codes:
- 01_rename.py
- 02-filter.py
- 03-is.py
- 04-new_columns.py
- 05-sort.py

#### Class Exercise
- ex_04-01.py
- ex_04-02.py
- ex_04-03.py


### Class 08 (2025-03-26)

#### Modules:
##### 5. Transformation and deletion
- Type conversion
- Applying functions in rows and columns
- Removing duplicates
- Working with NAs
- Replace

#### Class codes:
- 01-astype.py
- 02-apply.pu
- 03-apply_df.py
- 04-drop_duplicates.py
- 05-first_client_transaction.py
- 06-nan.py


#### Class Exercise
- ex_05-01.py
- ex_05-02.py
- ex_05-03.py
- ex_05-04.py
- ex_05-05.py


### Class 09 (2025-03-31)

##### 6. Group By
- Aggregating data
- The method agg
- Persolized aggregation

##### 7. Data joins
- Merge
- Concat

#### Class codes:
- 01-nas_input.py
- 02-replace.py
- 03-aggregations.py
- 04-join.py
- 05-join_duplicate.py

#### Extra:
- homework > extra_concat.py
- homework > extra_case.py (review)

#### Class Exercise
- ex_06-01.py


### Class 10 (2025-04-02)

##### 9. Connecting with SQL DataBases
- Importing data
- Running queries
- Writing data




##### 8. Other manipulations (SKIPPED)
- Stack
- Unstack
- Pivot Table
- Explode




---

### Homework

#### Exercise 2
Read the file transacoes.csv with the correct formatting.
Add a column with values 1.
Save the DataFrame with the name: transacoes_1.cs

- Class_exercises
    - ex_02.py

#### Exercise 3
03.01 - How many rows are there in the file clientes.csv?
03.02 - How many integer-type columns are there in the file transacoes.csv?
03.03 - How many object-type columns are there in the file produtos.csv?
03.04 - What is the id of the customer at index 4 in the file clientes.csv?
03.05 - What is the points balance of the customer at position 10 (without sorting) in the file clientes.csv?

- Class_exercises:
    - ex_03-01.py
    - ex_03-02.py
    - ex_03-03.py
    - ex_03-04.py
    - ex_03-05.py

#### Exercise 4
04.01 - How many customers are linked to Twitch?
04.02 - How many customers have a points balance greater than 1000?
04.03 - How many transactions occurred on 2025-02-01?

- Class_exercises:
    - ex_04-01.py
    - ex_04-02.py
    - ex_04-03.py

#### Exercise 5
05.01 - Create a new column “twitch_points”, which is the result of multiplying the points balance by the Twitch linkage indicator.
05.02 - Apply the log function to the points balance column, creating a new column.
05.03 - Create a column that indicates whether a person is linked to any (any) social media platform.
05.04 - What is the customer id with the highest points balance? And the lowest?
05.05 - Select the first daily transaction of each customer.

- Class_exercises:
    - ex_05-01_04.py
    - ex_05-05.py

#### Exercise 6
06.01 - What is the average number of social media platforms per user? And the variance? And the maximum?
06.02 - Who are the users who made the most transactions? Consider the top 10.
06.03 - Which user had the highest amount of debited points?
06.04 - Who had the most Streak transactions?
06.05 - What is the average number of transactions per day?
06.06 - How can we calculate the descriptive statistics of transaction points for each user?

- Class_exercises:
    - ex_06-01_06.py


