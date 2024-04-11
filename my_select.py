from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from main import Student, Group, Subject, Teacher, Grade, Base

# Функція для з'єднання з базою даних та створення сесії
def connect_to_database(database_url):
    engine = create_engine(database_url)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    return Session()

# Запит 1: Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def select_1(session):
    query = (
        session.query(Student, func.avg(Grade.value).label('average'))
        .join(Grade)
        .group_by(Student.id)
        .order_by(func.avg(Grade.value).desc())
        .limit(5)
        .all()
    )
    return query

# Запит 2: Знайти студента із найвищим середнім балом з певного предмета
def select_2(session, subject_name):
    query = (
        session.query(Student, func.avg(Grade.value).label('average'))
        .join(Grade)
        .join(Subject)
        .filter(Subject.name == subject_name)
        .group_by(Student.id)
        .order_by(func.avg(Grade.value).desc())
        .first()
    )
    return query

# Запит 3: Знайти середній бал у групах з певного предмета
def select_3(session, subject_name):
    query = (
        session.query(Group, func.avg(Grade.value).label('average'))
        .join(Student)
        .join(Grade)
        .join(Subject)
        .filter(Subject.name == subject_name)
        .group_by(Group.id)
        .all()
    )
    return query

# Запит 4: Знайти середній бал на потоці (по всій таблиці оцінок)
def select_4(session):
    query = session.query(func.avg(Grade.value)).scalar()
    return query

# Запит 5: Знайти які курси читає певний викладач
def select_5(session, teacher_name):
    query = (
        session.query(Subject.name)
        .join(Grade)
        .join(Teacher)
        .filter(Teacher.name == teacher_name)
        .group_by(Subject.name)
        .all()
    )
    return query

# Запит 6: Знайти список студентів у певній групі
def select_6(session, group_name):
    query = (
        session.query(Student)
        .join(Group)
        .filter(Group.name == group_name)
        .all()
    )
    return query

# Запит 7: Знайти оцінки студентів у окремій групі з певного предмета
def select_7(session, group_name, subject_name):
    query = (
        session.query(Student, Grade)
        .join(Group)
        .join(Grade)
        .join(Subject)
        .filter(Group.name == group_name, Subject.name == subject_name)
        .all()
    )
    return query

# Запит 8: Знайти середній бал, який ставить певний викладач зі своїх предметів
def select_8(session, teacher_name):
    query = (
        session.query(func.avg(Grade.value).label('average'))
        .join(Subject)
        .join(Teacher)
        .filter(Teacher.name == teacher_name)
        .scalar()
    )
    return query

# Запит 9: Знайти список курсів, які відвідує певний студент
def select_9(session, student_name):
    query = (
        session.query(Subject.name)
        .join(Grade)
        .join(Student)
        .filter(Student.name == student_name)
        .group_by(Subject.name)
        .all()
    )
    return query

# Запит 10: Список курсів, які певному студенту читає певний викладач
def select_10(session, student_name, teacher_name):
    query = (
        session.query(Subject.name)
        .join(Grade)
        .join(Student)
        .join(Teacher)
        .filter(Student.name == student_name, Teacher.name == teacher_name)
        .group_by(Subject.name)
        .all()
    )
    return query
