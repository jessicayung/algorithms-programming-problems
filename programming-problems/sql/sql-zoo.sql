/*
 * Reference: http://sqlzoo.net/wiki/The_JOIN_operation
 */

/*
 * JOIN
 * ON: how you combine rows from different tables
 */

 SELECT DISTINCT player
  FROM game JOIN goal ON matchid = id 
    WHERE (team1='GER' OR team2='GER') AND teamid!='GER'


/*
 * If two tables have the same column name, use a dot to indicate which
 * table the column is from.
 */

SELECT mdate, teamname
	FROM game JOIN eteam ON (team1=eteam.id)
		WHERE coach=('Fernando Santos')

/*
 * Find the number of orders sent by each shipper.
 * From w3schools
 */

SELECT Shippers.ShipperName,COUNT(Orders.OrderID) AS NumberOfOrders FROM Orders
LEFT JOIN Shippers
ON Orders.ShipperID=Shippers.ShipperID
GROUP BY ShipperName;

SELECT teamname, COUNT(matchid) AS Goals FROM goal
JOIN eteam 
ON eteam.id=goal.teamid
GROUP BY teamname;

/*
 * For every match involving 'POL', show the matchid, date and the number of goals scored.
 * Code: ...GROUP BY game.id; threw an error. 
 * Explanation: Need full GROUP BY:
 * SQL92 requires that all columns (except aggregates) in the select clause is part of the group by clause. SQL99 loosens this restriction a bit and states that all columns in the select clause must be functionally dependent of the group by clause. 
 * See http://stackoverflow.com/questions/25800411/mysql-isnt-in-group-by
 */

SELECT matchid,mdate, count(gtime)
FROM game JOIN goal ON matchid = id 
WHERE (team1 = 'POL' OR team2 = 'POL')
GROUP BY game.id, goal.matchid, mdate;

/*
 * Creating a new column:
 * Code below gives a col `score1` with value 0 or 1
 */

SELECT mdate,
  team1,
  CASE WHEN teamid=team1 THEN 1 ELSE 0 END score1
  FROM game JOIN goal ON matchid = id

/*
 * This misses out the rows where score1 = score2 = 0.
 * You need LEFT JOIN. You need all rows from the first table,
 * but they don't necessarily match all the rows int he second.
 */

SELECT mdate,
  team1,
  SUM(CASE WHEN teamid=team1 THEN 1 ELSE 0 END) as score1,
team2,
SUM(CASE WHEN teamid=team2 THEN 1 ELSE 0 END) as score2
  FROM game JOIN goal ON (matchid = id)
GROUP BY id, mdate, team1, team2
ORDER BY mdate, matchid, team1, team2

/*
 * Subqueries.
 * List the film title and the leading actor for all of the films 'Julie Andrews' played in.
 */

SELECT movie.title, actor.name
FROM casting JOIN movie ON movie.id = casting.movieid
JOIN actor on casting.actorid = actor.id
WHERE casting.ord = 1 AND movie.id IN 
(SELECT movieid FROM casting
WHERE actorid IN (
  SELECT id FROM actor
  WHERE name='Julie Andrews')
)

/*
 * HAVING
 * Obtain a list, in alphabetical order, of actors who've had at least 30 starring roles.
 * Q: I didn't have to order it. To the contrary, when I added the line
 * 'ORDER BY actor.name'
 * in the penultimate line, it threw a syntax error.
 */

SELECT actor.name 
FROM actor JOIN casting ON actor.id = casting.actorid
WHERE casting.ord = 1
GROUP BY actor.name
HAVING COUNT(casting.ord) >= 30

/*
 * My query returned the same results as the displayed answer but was marked as wrong.
 * Q16 on More_JOIN_operations
 */

SELECT DISTINCT actor.name FROM actor
JOIN casting ON actor.id = casting.actorid
WHERE casting.movieid IN 
(SELECT casting.movieid FROM casting 
JOIN actor ON actor.id = casting.actorid
WHERE actor.name = 'Art Garfunkel')


/*
 * Q: How do you join n tables?
 * Q: What's the difference between LEFT JOIN and JOIN and RIGHT JOIN?
 * Q: How do you decide what column to use in COUNT, since tit probably doesn't matter?
 */


