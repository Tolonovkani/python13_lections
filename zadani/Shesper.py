# # Дана база данных произведений Шекспира, в которой содержатся следующие
# # таблицы: character – герои произведений, work – произведения, chapter - главы
# # произведений, paragraph – параграфы, wordform – слова, встречающиеся в
# # произведениях
# # Напишите следующие запросы:
# # 1. Найдите 10 самых часто встречающихся слов.
# """ shakespeare_db=# select stemtext,occurences from wordform order by occurences desc limit 10
# ;
#  stemtext | occurences 
# ----------+------------
#  the      |      28932
#  and      |      27296
#  i        |      21120
#  to       |      20136
#  of       |      17169
#  a        |      14943
#  you      |      13989
#  my       |      12950
#  in       |      11512
#  that     |      11487
# (10 rows)
#  """
# # 2. Найдите все слова, которые начинаются с буквы ‘a’, регистр не должен иметь
# # значения.a’, регистр не должен иметь значения. 
# """shakespeare_db=# select plaintext from wordform where plaintext ilike 'a%';
    
# plaintext     
# -------------------
#  and
#  a
#  as
#  all
#  are
#  at
#  am
#  an
#  art
#  away
#  any
#  again
#  ay
#  against
#  aside
#  after
#  about
#  answer
#  another
#  arms
#  antony
#  alone
#  alas
#  age
#  air
#  ah
#  ask
#  almost
#  above
#  arm
#  already
#  appear
#  """
# # 3. Найдите все произведения,
# # которые относятся к жанру ‘a’, регистр не должен иметь значения.p’.
# """ shakespeare_db=# SELECT title FROM work WHERE work.genretype = 'a';
#  title 
# -------
# (0 rows) """

# # 4. Найдите среднее количество параграфов в произведения жанра ‘a’, регистр не
# # должен иметь значения.t’.

# # 5. Выведите все произведения, в которых количество слов выше среднего.
# # shakespeare_db=# select title from work where (select avg(totalwords) from work) < totalwords
# # shakespeare_db-# ;
# #            title           
# # ---------------------------
# #  All's Well That Ends Well
# #  Antony and Cleopatra
# #  As You Like It
# #  Coriolanus
# #  Cymbeline
# #  Hamlet
# #  Henry IV, Part I
# #  Henry IV, Part II
# #  Henry V
# #  Henry VI, Part I
# #  Henry VI, Part II
# #  Henry VI, Part III
# #  Henry VIII
# #  King John
# #  King Lear
# #  Love's Labour's Lost
# #  Measure for Measure
# #  Merchant of Venice
# #  Merry Wives of Windsor
# #  Much Ado about Nothing
# #  Othello
# #  Richard II
# #  Richard III
# #  Romeo and Juliet
# #  Taming of the Shrew
# #  Titus Andronicus
# #  Troilus and Cressida
# #  The Winter's Tale
# # (28 rows)


# # 6. Выведите имя героя, количество его реплик, и произведение, в котором
# # этот герой встречается.
# """shakespeare_db=# select c1 .charname, c1.speechcount,w.title 
# from character c1
# join character_work c2 on c1.charid = c2.charid
# join work w on  w.workid = c2.workid;
# shakespeare_db=# 
   
#                charname                 | speechcount |           title           
# ------------------------------------------+-------------+---------------------------
#  First Apparition                         |           1 | Macbeth
#  First Citizen                            |           3 | Romeo and Juliet
#  First Conspirator                        |           3 | Coriolanus
#  First Gentleman                          |           1 | Othello
#  First Goth                               |           4 | Titus Andronicus
#  First Murderer                           |          21 | Macbeth
#  First Musician                           |           5 | Othello
#  First Musician                           |          10 | Romeo and Juliet
#  First Officer                            |           3 | Othello
#  First Player                             |           8 | Hamlet
#  First Senator                            |          33 | Coriolanus
#  First Senator                            |           8 | Othello
#  First Servant                            |           4 | Romeo and Juliet
#  First Serving-Man                        |           5 | Henry VI, Part I
#  First Soldier                            |           8 | Coriolanus
#  First Watchman                           |           6 | Much Ado about Nothing
#  First Watchman                           |           6 | Romeo and Juliet
#  First Witch                              |          23 | Macbeth
#  Second Apparition                        |           2 | Macbeth
#  Second Conspirator                       |           2 | Coriolanus
#  Second Gentleman                         |           5 | Othello
#  Second Goth                              |           1 | Titus Andronicus
#  Second Murderer                          |           6 | Macbeth
#  Second Musician                          |           3 | Romeo and Juliet
#  Second Patrician                         |           1 | Coriolanus
#  Second Senator                           |          10 | Coriolanus
#  Second Senator                           |           1 | Othello
#  Second Servant                           |           6 | Romeo and Juliet
#  Second Serving-Man                       |           2 | Henry VI, Part I
#  Second Soldier                           |           1 | Coriolanus
#  Second Watchman                          |           5 | Much Ado about Nothing
#  Second Watchman                          |           1 | Romeo and Juliet
#  Second Witch                             |          15 | Macbeth
#  Third Apparition                         |           1 | Macbeth
#  Third Conspirator                        |           3 | Coriolanus
#  Third Gentleman                          |           4 | Othello
#  Third Goth                               |           1 | Titus Andronicus
#  Third Murderer                           |           6 | Macbeth
#  Third Musician                           |           1 | Romeo and Juliet
#  Third Serving-Man                        |           2 | Henry VI, Part I
#  Third Watchman                           |           1 | Romeo and Juliet
#  Third Witch                              |          13 | Macbeth
#  Fourth Gentleman                         |           1 | Othello
#  Aaron                                    |          57 | Titus Andronicus
#  Abbot                                    |           2 | Richard II
#  Lord Abergavenny                         |           5 | Henry VIII
#  Abhorson                                 |          13 | Measure for Measure
#  Abraham                                  |           5 | Romeo and Juliet
# :

#  """

# # 7. Выведите среднее количество реплик героев в произведении ‘a’,
# # регистр не должен иметь значения.Romeo and Juliet’.
# # 
# # shakespeare_db=# select avg(c1.speechcount) 
# # from character c1
# # join character_work c2 on c1.charid = c2.charid
# # join work w on  w.workid = c2.workid
# # where w.title = 'Romeo and Juliet';
# #          avg         
# # ---------------------
# #  25.5454545454545455
# # (1 row)

# # shakespeare_db=# 

# #  8. Выведите общее
# # количество слов в каждой из секций в таблице paragraph.
# """ shakespeare_db=# select  count(plaintext) + count(phonetictext) + count(stemtext) as total from paragraph;
#  total  
# --------
#  106395
# (1 row)
#  """
# #  9. Выведите
# # всех героев, которые имеют от 15 до 30 реплик
#  """ shakespeare_db=# select c1 charename                                                    
# from character c1
# join character_work c2 on c1.charid = c2.charid
# join work w on  w.workid = c2.workid
# where 15 < c1.speechcount and 30 > c1.speechcount;
# shakespeare_db=# 
#  """
# # 10. Выведите все произведения, которые были написаны в 17 веке
# """ shakespeare_db=# select title from work where year >= 1601 and year <= 1700;
#            title           
# ---------------------------
#  All's Well That Ends Well
#  Antony and Cleopatra
#  Coriolanus
#  Cymbeline
#  Henry VIII
#  King Lear
#  Lover's Complaint
#  Macbeth
#  Measure for Measure
#  Othello
#  Pericles
#  Phoenix and the Turtle
#  Sonnets
#  Tempest
#  Timon of Athens
#  Troilus and Cressida
#  The Winter's Tale
# (17 rows)

# shakespeare_db=# 
# """
# # 11. Найдите все произведения, которые имею в полном названии
# # слово ‘a’, регистр не должен иметь значения.the’ 
# # shakespeare_db=# select title from work where work.longtitle ilike '%the%';
#          title          
# ------------------------
#  Comedy of Errors
#  Hamlet
#  Julius Caesar
#  King Lear
#  Macbeth
#  Merchant of Venice
#  Merry Wives of Windsor
#  Othello
#  Passionate Pilgrim
#  Phoenix and the Turtle
#  Rape of Lucrece
#  Romeo and Juliet
#  Taming of the Shrew
#  Tempest
#  Timon of Athens
#  The Winter's Tale
# (16 rows)


# # 12. Выведите всеуникальные секции в paragraph.
# shakespeare_db=# select distinct section from paragraph; 
#  section 
# ---------
#        0
#        1
#        3
#        5
#        4
#        2
# (6 rows)


# # 13. Для каждой главы выведите: id, описание и название произведения, к которой
# относится данная глава.
# shakespeare_db=# select c.chapterid, c.description,  w.title
# from chapter c
# join work w on w.workid = c.workid;

#  chapterid |                                       description                                        |           title           
# -----------+------------------------------------------------------------------------------------------+---------------------------
#      18934 | Prologue.                                                                                | Henry V
#      18704 | DUKE ORSINO's palace.                                                                    | Twelfth Night
#      18705 | The sea-coast.                                                                           | Twelfth Night
#      18706 | OLIVIA'S house.                                                                          | Twelfth Night
#      18707 | DUKE ORSINO's palace.                                                                    | Twelfth Night
#      18708 | OLIVIA'S house.                                                                          | Twelfth Night
#      18709 | The sea-coast.                                                                           | Twelfth Night
#      18710 | A street.                                                                                | Twelfth Night
#      18711 | OLIVIA's house.                                                                          | Twelfth Night
#      18712 | DUKE ORSINO's palace.                                                                    | Twelfth Night
#      18713 | OLIVIA's garden.                                                                         | Twelfth Night

# 14. Для каждого параграфа выведите: номер параграфа, имя героя, и количество
# реплик героя

# shakespeare_db=# SELECT p.paragraphnum, ch.charname, ch.speechcount
# FROM paragraph p
# JOIN character ch ON p.charid = ch.charid;

#  paragraphnum |                 charname                 | speechcount 
# --------------+------------------------------------------+-------------
#             3 | (stage directions)                       |         126
#             4 | Orsino                                   |          59
#            19 | Curio                                    |           4
#            20 | Orsino                                   |          59
#            21 | Curio                                    |           4
#            22 | Orsino                                   |          59
#            30 | Valentine                                |           3
#            39 | Orsino                                   |          59

# 15. Для каждого параграфа выведите: номер параграфа, название произведения и
# год выхода этого произведения.

# shakespeare_db=# select p.paragraphnum, w.title, w.year
# shakespeare_db-# from paragraph p
# shakespeare_db-# join work w on p.workid = w.workid;
#      paragraphnum |           title           | year 
# --------------+---------------------------+------
#             3 | Twelfth Night             | 1599
#             4 | Twelfth Night             | 1599
#            19 | Twelfth Night             | 1599
#            20 | Twelfth Night             | 1599
#            21 | Twelfth Night             | 1599
# ======================================================================================
# № 2
# 1. Вытащить все произведения в котрых sourse = Moby и кол-во параграфов меньше 100

# shakespeare_db=# select title from work where source = 'Moby' and totalparagraphs< 100;
#          title          
# ------------------------
#  Lover's Complaint
#  Passionate Pilgrim
#  Phoenix and the Turtle
# (3 rows)

# 2. Найти кол-во глав в каждом произведении

# shakespeare_db=# select w.title, count(c.chapter) from work w JOIN chapter c ON c.workid = w.workid group by w.workid;
#        title           | count 
# ---------------------------+-------
#  Tempest                   |     9
#  Passionate Pilgrim        |    21
#  Taming of the Shrew       |    14
#  Measure for Measure       |    17
#  Henry IV, Part I          |    19
#  Henry VI, Part I          |    27

# 3. Найти сколько произведений относятся к каждому 

# 4. Найти кол-во параграфов в каждом произведении и вытащить названия произведений

# shakespeare_db=# select totalparagraphs, title 
# from  work;

#  totalparagraphs |           title           
# -----------------+---------------------------
#             1031 | Twelfth Night
#             1025 | All's Well That Ends Well
#             1344 | Antony and Cleopatra

# 5. Вытащить имена героев, чьи реплики состовляют больше 200 слов, также произведения в которых они встречаються, жанр, год выхода произдведения в порядке убывания

# 6. Вытащить героя, который чаще всех появляется в произведениях


