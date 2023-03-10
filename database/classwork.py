#my_db=# insert into makers (mentor_id, name, position, birthdate, salary) values (15, 'Tofik', 'Scrum', 1998, 5700);

#----------------------------------------------------------------

# my_db=# select * from makers;
#  mentor_id |    name     | position | birthdate | salary 
# -----------+-------------+----------+-----------+--------
#          2 | Sanzhar     | Mentor   |      2002 |  40000
#          1 | Sultan      | Mentor   |      2003 |   6000
#          3 | Aigerim     | Mentor   |      2002 |   7000
#          4 | Erkayim     | Tracker  |      2001 |   6500
#          5 | Ertay       | Scrum    |      2003 |   5000
#          6 | Iskhak      | Mentor   |      1998 |   5500
#          7 | Aktan       | Scrum    |      2001 |   6700
#          8 | Sharshanbek | Mentor   |      1999 |   6800
#          9 | Kalicha     | Mentor   |      2000 |   7100
#         10 | Shabdanbek  | Mentor   |      2002 |   7200
#         11 | Vladislav   | Mentor   |      2001 |   5900
#         12 | Anastasia   | Mentor   |      2002 |   9000
#         13 | Maksatbek   | Mentor   |      2000 |   7700
#         14 | Jannatbek   | Tracker  |      1999 |   6600
#         15 | Tofik       | Scrum    |      1998 |   5700


#-------------------------------------------------------------------

#my_db=# SELECT name || ' -> ' || position as mentors  FROM makers; 

#         mentors        
# -----------------------
#  Sanzhar -> Mentor
#  Sultan -> Mentor
#  Aigerim -> Mentor
#  Erkayim -> Tracker
#  Ertay -> Scrum
#  Iskhak -> Mentor
#  Aktan -> Scrum
#  Sharshanbek -> Mentor
#  Kalicha -> Mentor
#  Shabdanbek -> Mentor
#  Vladislav -> Mentor
#  Anastasia -> Mentor
#  Maksatbek -> Mentor
#  Jannatbek -> Tracker
#  Tofik -> Scrum


#---------------------------------------------------------------------
# my_db=# SELECT birthdate FROM makers ORDER BY birthdate ASC;


#  birthdate 
# -----------
#       1998
#       1998
#       1999
#       1999
#       2000
#       2000
#       2001
#       2001
#       2001
#       2002
#       2002
#       2002
#       2002
#       2003
#       2003


#------------------------------------------------------------

# my_db=# SELECT * FROM makers WHERE name LIKE 'A%' or name LIKE 'S%' and position = 'Mentor' or  position = 'Tracker';

#------------------------------------------------------------

# my_db=# SELECT * FROM makers WHERE salary BETWEEN 5000 and 8000;
#  mentor_id |    name     | position | birthdate | salary 
# -----------+-------------+----------+-----------+--------
#          1 | Sultan      | Mentor   |      2003 |   6000
#          3 | Aigerim     | Mentor   |      2002 |   7000
#          4 | Erkayim     | Tracker  |      2001 |   6500
#          5 | Ertay       | Scrum    |      2003 |   5000
#          6 | Iskhak      | Mentor   |      1998 |   5500
#          7 | Aktan       | Scrum    |      2001 |   6700
#          8 | Sharshanbek | Mentor   |      1999 |   6800
#          9 | Kalicha     | Mentor   |      2000 |   7100
#         10 | Shabdanbek  | Mentor   |      2002 |   7200
#         11 | Vladislav   | Mentor   |      2001 |   5900
#         13 | Maksatbek   | Mentor   |      2000 |   7700
#         14 | Jannatbek   | Tracker  |      1999 |   6600
#         15 | Tofik       | Scrum    |      1998 |   5700

#-----------------------------------------------------------------


# my_db=# SELECT salary FROM makers ORDER BY salary DESC LIMIT 3;
#  salary 
# --------
#   40000
#    9000
#    7700


#------------------------------------------------------------------

# my_db=# SELECT COUNT (*) FROM makers as QU WHERE position = 'Mentor';
#  count 
# -------
#     10

#--------

# my_db=# SELECT COUNT (*) FROM makers as QU WHERE position = 'Scrum';
#  count 
# -------
#      3

#--------

# my_db=# SELECT COUNT (*) FROM makers as QU WHERE position = 'Tracker';
#  count 
# -------
#      2

#------------------------------------------------------------------------


# my_db=# SELECT sum(salary)/ COUNT(salary) as AVERAGE FROM makers WHERE position = 'Scrum';
#  average 
# ---------
#     5800

#----------------------------------------------------------------------------

#my_db=# SELECT name, length(name) FROM makers ORDER BY length(name) DESC;
#     name     | length 
# -------------+--------
#  Sharshanbek |     11
#  Shabdanbek  |     10
#  Vladislav   |      9
#  Jannatbek   |      9
#  Maksatbek   |      9
#  Anastasia   |      9
#  Sanzhar     |      7
#  Aigerim     |      7
#  Erkayim     |      7
#  Kalicha     |      7
#  Iskhak      |      6
#  Sultan      |      6
#  Aktan       |      5
#  Ertay       |      5
#  Tofik       |      5


#---------------------------------------------------------------


# my_db=# UPDATE makers SET salary = 8000 WHERE mentor_id = 2;
# UPDATE 1
# my_db=# SELECT * from makers                                        
# ;
#  mentor_id |    name     | position | birthdate | salary 
# -----------+-------------+----------+-----------+--------
#          1 | Sultan      | Mentor   |      2003 |   6000
#          3 | Aigerim     | Mentor   |      2002 |   7000
#          4 | Erkayim     | Tracker  |      2001 |   6500
#          5 | Ertay       | Scrum    |      2003 |   5000
#          6 | Iskhak      | Mentor   |      1998 |   5500
#          7 | Aktan       | Scrum    |      2001 |   6700
#          8 | Sharshanbek | Mentor   |      1999 |   6800
#          9 | Kalicha     | Mentor   |      2000 |   7100
#         10 | Shabdanbek  | Mentor   |      2002 |   7200
#         11 | Vladislav   | Mentor   |      2001 |   5900
#         12 | Anastasia   | Mentor   |      2002 |   9000
#         13 | Maksatbek   | Mentor   |      2000 |   7700
#         14 | Jannatbek   | Tracker  |      1999 |   6600
#         15 | Tofik       | Scrum    |      1998 |   5700
#          2 | Sanzhar     | Mentor   |      2002 |   8000


#----------------------------------------------------------my_db=# DELETE FROM makers WHERE mentor_id = 1;
# DELETE 1
# my_db=# SELECT * from makers
# ;
#  mentor_id |    name     | position | birthdate | salary 
# -----------+-------------+----------+-----------+--------
#          3 | Aigerim     | Mentor   |      2002 |   7000
#          4 | Erkayim     | Tracker  |      2001 |   6500
#          5 | Ertay       | Scrum    |      2003 |   5000
#          6 | Iskhak      | Mentor   |      1998 |   5500
#          7 | Aktan       | Scrum    |      2001 |   6700
#          8 | Sharshanbek | Mentor   |      1999 |   6800
#          9 | Kalicha     | Mentor   |      2000 |   7100
#         10 | Shabdanbek  | Mentor   |      2002 |   7200
#         11 | Vladislav   | Mentor   |      2001 |   5900
#         12 | Anastasia   | Mentor   |      2002 |   9000
#         13 | Maksatbek   | Mentor   |      2000 |   7700
#         14 | Jannatbek   | Tracker  |      1999 |   6600
#         15 | Tofik       | Scrum    |      1998 |   5700
#          2 | Sanzhar     | Mentor   |      2002 |   8000


#----------------------------------------------------------------
# ALTER TABLE makers DROP COLUMN salary;

#---------------------------------------------------------------

#ALTER TABLE makers
#RENAME COLUMN menthor_id TO employee_id;

