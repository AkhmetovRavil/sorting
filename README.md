# Data sorting task

A series of integers is given, obtained as a result of processing the symbols of the student’s Last Name, First Name, Patronymic, as well as his ID. It is necessary to sort the data set in two ways, and also perform some arithmetic calculations.

Full name and ID are prepared in advance in a text file named source_data.txt in Unicode encoding. Each word that makes up the full name must be capitalized. Words must be separated by a space.

## Required to write a program in Python that performs the following tasks:

1. Read the source data from the text file source_data.txt

2. Calculate the integer value obtained by dividing the ID by the number of characters that make up the full name (the number of characters is counted without taking into account spaces).

3. Determine the sorting direction depending on the number obtained in step 2:

- sort in ascending order if the number is even;

- sort in descending order if the number is odd.

4. Generate a data set (list) from the Unicode codes of each character of the full name (excluding spaces between words), converted to decimal form.

5. Sort the data set in descending or ascending order. Sorting should be done in two different ways. The program code should contain comments indicating one or another sorting algorithm.

6. Calculate the arithmetic mean of the dataset. If necessary, round the result to the third decimal place.

7. Calculate the root mean square of the dataset. If necessary, round the result to the third decimal place.
