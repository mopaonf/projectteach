import sqlite3

class Course: 
  TABLE_NAME = "course"

  def __init__(self, course_id = None, course_name = None):
    self.course_id = course_id 
    self.course_name = course_name
    pass

  def save(self, ):
    with sqlite3.connect("db.sqlite3") as connection:
      cursor = connection.cursor()

      if self.course_id:
          query = f"UPDATE {self.TABLE_NAME} set course_name = ? WHERE course_id = ?"
          cursor.execute (query, (self.course_name, self.course_id))
      else:
          query = f"INSERT INTO {self.__class__.TABLE_NAME} (course_name) VALUES(?)"

          cursor.execute(query, (self.course_name))


      pass 

  def read(course_id=None):
    with sqlite3.connect("db.sqlite") as connection:
      cursor = connection.cursor()
      if course_id:
        query = f"SELECT (course_id, course_name) FROM {self.__class__.TABLE_NAME} where course_id = ?"

        result = cursor.execute(query, (course_id, )).fetchone()

        course = Course(course_name=result[1])
        course.id = result[0]

        return course
      else:
        query = f"SELECT (course_id, course_name) FROM {self.__class__.TABLE_NAME}"

        results = cursor.execute(query).fetchall()
        courses = []

        for result in results:
          course = Course(course_name=result[1])
          course.course_id = result[0]

          courses.append(course)

          return courses
    pass 

  def delete(self):
    if self.course_id:
      with sqlite3.connect("db.sqlite") as connection: 
        cursor= connection.cursor()

        cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE course_id = ?", {self.course_id, }) 
    pass 
