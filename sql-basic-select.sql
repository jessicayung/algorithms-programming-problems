/* TABLE: STATION

*/
-- Alternate form of comment.

SELECT * FROM STATION WHERE

/* The names of the columns or elements you want to select should be separated by commas. */
SELECT CITY, LEN(CITY) FROM STATION;

/* Distinct entries only */
SELECT DISTINCT CITY FROM STATION;

/* Selecting all city names with even ID */
SELECT CITY FROM STATION WHERE (ID%2) = 0;

/* Order by length of name of city, name of city in alphabetical order */
SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY), CITY LIMIT 1;
SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY) DESC, CITY LIMIT 1;

/* 
 * Suggestion: 
 * SELECT DISTINCT city from station where city LIKE '[a, e, i, o, u]%'ORDER BY city; 
 * Doesn't work for me but anyway
 */

/* Select all city names that start and end with a vowel.*/
SELECT DISTINCT CITY FROM STATION WHERE 
(UCASE(LEFT(CITY,1)) = "A" 
OR UCASE(LEFT(CITY,1)) = "E" 
OR UCASE(LEFT(CITY,1)) = "I" 
OR UCASE(LEFT(CITY,1)) = "O" 
OR UCASE(LEFT(CITY,1)) = "U") 
AND 
(UCASE(RIGHT(CITY,1)) = "A" 
OR UCASE(RIGHT(CITY,1)) = "E"
OR UCASE(RIGHT(CITY,1)) = "I"
OR UCASE(RIGHT(CITY,1)) = "O"
OR UCASE(RIGHT(CITY,1)) = "U")
ORDER BY CITY;

/*
 * Select all city names that don't end with a vowel.
 * Used: NOT()
 */
SELECT DISTINCT CITY FROM STATION WHERE NOT(UCASE(RIGHT(CITY,1)) = "A" 
OR UCASE(RIGHT(CITY,1)) = "E"
OR UCASE(RIGHT(CITY,1)) = "I"
OR UCASE(RIGHT(CITY,1)) = "O"
OR UCASE(RIGHT(CITY,1)) = "U")
ORDER BY CITY;