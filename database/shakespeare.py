# 1. Найдите 10 самых часто встречающихся слов.
# Select plaintext from wordform LIMIT 10;

#-------------------------------------------------------------------
# 2) Найдите все слова, которые начинаются с буквы ‘a’, регистр не должен иметь значения.

# SELECT  plaintext FROM wordform WHERE plaintext ILIKE 'a%';

#-------------------------------------------------------------------

# 3. Найдите все произведения, которые относятся к жанру ‘p’.

# SELECT title from work WHERE genretype like 'p';

#-----------------------------------------------------------------------

# 4. Найдите среднее количество параграфов в произведения жанра ‘t’.

# SELECT AVG(totalparagraphs) FROM work  WHERE genretype like 't';

#-------------------------------------------------------------------

# 5. Выведите все произведения, в которых количество слов выше среднего.

# SELECT title FROM work WHERE totalwords > (SELECT AVG(totalwords) FROM work);


#---------------------------------------------------------------------

# 6. Выведите имя героя, количество его реплик, и произведение, в котором этот герой
# встречается.

# SELECT character.charname, speechcount, work.title FROM character LEFT JOIN character_work ON character.charid = character_work.charid LEFT JOIN work ON character_work.workid = work.workid;

#----------------------------------------------------------------------------------------

# 7. Выведите среднее количество реплик героев в произведении ‘Romeo and Juliet’.

# SELECT ROUND(AVG(speechcount)), work.title FROM character JOIN character_work ON character.charid = character_work.charid  JOIN work ON character_work.workid = work.workid WHERE work.title = 'Romeo and Juliet' GROUP BY work.title;


#-----------------------------------------------------------------------------------------

# 8. Выведите общее количество слов в каждой из секций в таблице paragraph.

# SELECT section, SUM(wordcount) as sum FROM paragraph GROUP BY section;


#-----------------------------------------------------------------------------------------

# 9. Выведите всех героев, которые имеют от 15 до 30 реплик.


# SELECT charname FROM character WHERE speechcount between 15 and 30;

#-----------------------------------------------------------------------------------------

# 10. Выведите все произведения, которые были написаны в 17 веке

# SELECT title FROM work  WHERE year between 1601 and 1700;

#-----------------------------------------------------------------------------------------

# 11. Найдите все произведения, которые имею в полном названии слово значения.'the'

# SELECT title FROM work  WHERE longtitle ILIKE '%the%';

#--------------------------------------------------------------------------------------------

# 12. Выведите все уникальные секции в paragraph.

# SELECT  DISTINCT section FROM paragraph;

#--------------------------------------------------------------------------------------------

# 13. Для каждой главы выведите: id, описание и название произведения, к которой относится
# данная глава.

# SELECT chapterid, description, work.title FROM chapter JOIN work ON chapter.workid = work.workid;

#----------------------------------------------------------------------------------


# 14. Для каждого параграфа выведите: номер параграфа, имя героя, и количество реплик героя.

# select paragraphnum, character.charname, character.speechcount from paragraph JOIN character ON paragraph.charid = character.charid;

#---------------------------------------------------------------------------------------------------

# 15. Для каждого параграфа выведите: номер параграфа, название произведения и год выхода
# этого произведения.

# select paragraphnum, work.title, work.year from paragraph JOIN work ON paragraph.workid = work.workid;


