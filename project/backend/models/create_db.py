import os
import sqlite3

PATH_TO_DB = os.path.join(
  os.path.dirname(__file__),
  "db.sqlite"
)

create_course_table_query = "CREATE TABLE course (course_id INTERGER PRIMARY KEY AUTOINCREMENT, course_name TEXT)"

create_classes_table_query = "CREATE TABLE classes (class_id INTERGER PRIMARY KEY AUTO INCREMENT, class_name TEXT)"

create_course_class_table_query = """CREATE TABLE course_class (course_class_id INTERGER PRIMARY KEY AUTO INCREMENT, course_id INTERGER, class_id INTERGER, num_hours INTERGER, FOREIGN KEY(course_id) REFERENCES course(course_id),
FOREIGN KEY(class_id) REFERENCES TO classes(class_id))"""

with sqlite3.connect(PATH_TO_DB) as connection:
  cursor = connection.cursor()
  
  for query in [create_course_table_query, create_classes_table_query, create_course_class_table_query]:
    cursor.execute(query)