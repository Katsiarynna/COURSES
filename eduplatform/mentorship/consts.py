from .models import User, Teacher, Student, Group, Email
from testing_system.models import (Course, Topic, Article,
                                   Test, Question, Answer, Attempt)
from chat.models import Room, Message, ConversationRequest

from .annotations import (
    UserAnnotation, TeacherAnnotation, StudentAnnotation,
    CourseAnnotation, TopicAnnotation, GroupAnnotation,
    ArticleAnnotation, TestAnnotation, QuestionAnnotation,
    AnswerAnnotation, AttemptAnnotation, EmailAnnotation)


USER_DATA = {
    'password': 'qwerty',
    'first_name': 'Name_test',
    'last_name': 'Surname_test',
    'email': 'test@mail.ru',
}

def create_user(email="sender@example.com") -> UserAnnotation:
    user = User.objects.create_user(
        password='qwerty',
        first_name='Name_test',
        last_name='Surname_test',
        email='test@mail.ru',)
    return user


def create_teacher(user_id) -> TeacherAnnotation:
    teacher = Teacher.objects.create(experience=10, user=user_id)
    return teacher

def create_student(user_id) -> StudentAnnotation:
    student = Student.objects.create(age=18, rating=55.55, user=user_id)
    return student

def create_course(teacher_id) -> CourseAnnotation:
    course = Course.objects.create(name="Test", teacher=teacher_id, price=1000)
    return course

def create_group(teacher_id, course_id) -> GroupAnnotation:
    group = Group.objects.create(
        group_name="Teacher",
        teacher=teacher_id,
        course=course_id)
    return group

def create_topic(course_id) -> TopicAnnotation:
    topic = Topic.objects.create(name="Test", course=course_id, content="123456")
    return topic

def create_article(teacher_id, topic_id) -> ArticleAnnotation:
    article = Article.objects.create(
        title="Test",
        teacher=teacher_id,
        topic=topic_id,
        content="123456")
    return article

def create_test(teacher_id, topic_id) -> TestAnnotation:
    test = Test.objects.create(
        title="Test",
        teacher=teacher_id,
        topic=topic_id,
        description="123456",
        is_open=False)
    return test


def create_question(test_id) -> QuestionAnnotation:
    question = Question.objects.create(
        text='test_text', test=test_id, is_important=True)
    return question


def create_answer(question_id) -> AnswerAnnotation:
    answer = Answer.objects.create(
        text='answer',
        question=question_id,
        is_correct=True)
    return answer


def create_attempt(test_id, student_id) -> AttemptAnnotation:
    attempt = Attempt.objects.create(
        test=test_id,
        student=student_id,
        score=50)
    return attempt


def create_email(user_id) -> EmailAnnotation:
    email = Email.objects.create(
        sender=user_id,
        recipients=user_id,
        subject='issue',
        message='1+2=?'
    )
    return email

def create_room(user):
    room = Room.objects.create(
        name="Lucky"
    )
    room.online.add(user)
    return room


def create_message(user, room):
    message = Message.objects.create(
        room=room,
        user=user,
        content="Very interesting"
    )
    return message


def create_conversationrequest(user_id):
    user = User.objects.get(pk=user_id)
    conversationrequest = ConversationRequest.objects.create(
        from_user=user,
        to_user=user,  # Например, отправляем запрос самому себе
        message="Test for my chat"
    )
    return conversationrequest





