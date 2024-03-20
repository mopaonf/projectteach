import sqlite3

class CourseClass: 
  TABLE_NAME= "course_class"

  def __init__(self, course_class_id=None,course_id=None, class_id=None, num_hours=None ):
    self.course_class_id = course_class_id
    self.course_id = course_id
    self.class_id = class_id
    self.num_hours = num_hours
    pass

  def save(self, ):
    with sqlite3.connect("db.sqlite3") as connection:
      cursor = connection.cursor()

      if self.course_id:
        query = f"UPDATE {self.TABLE_NAME} set num_hours = ?,course_id = ?, class_id = ? WHERE course_class_id = ? "
        cursor.execute (query, (self.num_hours,self.course_id, self.class_id, self.course_class_id))
      else:
        query = f"INSERT INTO {self.__class__.TABLE_NAME} (course_id, class_id, num_hours) VALUES(?,?,?)"

        cursor.execute(query, (self.course_id, self.class_id, self.num_hours))
      pass

  def read(course_class_id=None):
    with sqlite3.connect("db.sqlite") as connection:
        cursor = connection.cursor()
        if id:
            query = f"SELECT (course_class_id, course_id, class_id, num_hours) FROM {self.__class__.TABLE_NAME} WHERE course_class_id=?"

            result = cursor.execute(query, (id, )).fetchone()

            course_class = CourseClass(name=result[1], path=result[2])
            course_class.course_class_id = result[0]

            return course_class
        else:
            query = f"SELECT (course_class_id, course_id, class_id, num_hours) FROM {self.__class__.TABLE_NAME}"
            results = cursor.execute(query).fetchall()
            course_classs = []

            for result in results:
                course_class = CourseClass(name=result[1], path=result[2])
                course_class.course_class_id = result[0]

                course_classs.append(course_class)
            
            return course_classs
    
    pass 

  def delete(self):
    if self.course_class_id:
      with sqlite3.connect("db.sqlite") as connection: 
        cursor= connection.cursor()

        cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE course_class_id = ?", {self.class_id, }) 
    pass 

