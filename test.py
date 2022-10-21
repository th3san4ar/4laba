from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
engine = create_engine("mysql://root:okennnn999@localhost/school")
Session = sessionmaker(bind=engine)
session = Session()

teacher = models.Teacher(
    first_name = 'a',
    second_name = 'a',
    email = 'a',
    password = 'a'
)

session.add(teacher)
session.commit()

print(teacher.first_name)