from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Student, Group, Subject, Teacher, Grade, Base

# Підключення до бази даних
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

# Створення сесії
Session = sessionmaker(bind=engine)
session = Session()

# Ініціалізація генератора випадкових даних Faker
fake = Faker()

# Додавання груп
groups = []
for _ in range(3):
    group = Group(name=fake.random_element(['A', 'B', 'C']))
    session.add(group)
    groups.append(group)

# Додавання предметів
subjects = []
for _ in range(5):
    subject = Subject(name=fake.word())
    session.add(subject)
    subjects.append(subject)

# Додавання викладачів
teachers = []
for _ in range(5):
    teacher = Teacher(name=fake.name())
    session.add(teacher)
    teachers.append(teacher)

# Додавання студентів та оцінок
for _ in range(30):
    student = Student(name=fake.name(), group=fake.random_element(groups))
    session.add(student)
    for subject in subjects:
        mark = Grade(value=fake.random_int(min=1, max=5),
                    subject=subject,
                    teacher=fake.random_element(teachers),
                    student=student)
        session.add(mark)

# Збереження змін у базу даних
session.commit()

# Закриття сесії
session.close()
