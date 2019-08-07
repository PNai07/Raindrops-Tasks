# Raindrops-Tasks

Write a function that takes as its input a number (n) and converts it to a string, the contents of which depend on the numbers factors

- if the number has a factor of 3, output 'Pling'

- if the number has a factor of 5, output 'Plang'

- if the number has a factor of 7, output 'Plong'

- if the number does not have any of the above as a factor simply return the numbers digits

# Examples

- 28's factors are 1, 2, 4, 7, 14 and 28: this would be a simple 'Plong'

- 30's factors are 1, 2, 3, 5, 6, 10, 15, 30: this would be a 'PlingPlang'

- 34 has four factors: 1, 2, 17, and 34: this would be '34'

# Solution

So for this task, I've used IF functions, which help determine if the integer value entered by the user is divisible by 3, 5 or 7. 
The program starts by asking the user to enter a value, mostly an integer. The program will then go through to ensure if the value entered is divisble by 3,5 or 7, and output the raindrops Pling, Plang, Plong according to the conditions. 

For the testing method, I've used pytest as a testing type. This is beneficial for complex programs and helps to detect code better. Therefore, this was used for better efficiency than using Unit Testing and found pytest more up to date. I've installed pytest to the project and within the terminal I ran pytest. For the testing, I've derived a series of test cases which would help with the testing. 
