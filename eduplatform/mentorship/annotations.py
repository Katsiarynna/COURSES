from dataclasses import dataclass
from typing import List

from django.forms import EmailField


@dataclass(frozen=True, slots=True)
class UserAnnotation:
    password: str
    first_name: str
    last_name: str
    email: str


@dataclass(frozen=True, slots=True)
class TeacherAnnotation:
    user: UserAnnotation
    experience: int


@dataclass(frozen=True, slots=True)
class StudentAnnotation:
    user: UserAnnotation
    rating: int
    age: int


@dataclass(frozen=True, slots=True)
class CourseAnnotation:
    name: str
    teacher: TeacherAnnotation
    price: int


@dataclass(frozen=True, slots=True)
class GroupAnnotation:
    group_name: str
    teacher: TeacherAnnotation
    student: List[StudentAnnotation]
    course: CourseAnnotation


@dataclass(frozen=True, slots=True)
class TopicAnnotation:
    name: str
    teacher: TeacherAnnotation
    course: CourseAnnotation
    content: str


@dataclass(frozen=True, slots=True)
class ArticleAnnotation:
    title: str
    topic: TopicAnnotation
    teacher: TeacherAnnotation
    content: str


@dataclass(frozen=True, slots=True)
class TestAnnotation:
    title: str
    topic: TopicAnnotation
    teacher: TeacherAnnotation
    description: str
    is_open: bool


@dataclass(frozen=True, slots=True)
class QuestionAnnotation:
    text: str
    test: TestAnnotation
    is_important: bool


@dataclass(frozen=True, slots=True)
class AnswerAnnotation:
    text: str
    question: QuestionAnnotation
    is_correct: bool


@dataclass(frozen=True, slots=True)
class AttemptAnnotation:
    test: TestAnnotation
    student: StudentAnnotation
    score: int


@dataclass(frozen=True, slots=True)
class EmailAnnotation:
    recipients: TeacherAnnotation
    is_read: True
    sender: StudentAnnotation
    subject: str
    message: str


@dataclass(frozen=True, slots=True)
class RoomAnnotation:
    name: str
    online: True


@dataclass(frozen=True, slots=True)
class MessageAnnotation:
    room: RoomAnnotation
    user: UserAnnotation
    content: str


@dataclass(frozen=True, slots=True)
class ConversationRequest:
    from_user: UserAnnotation
    to_user: UserAnnotation
    message: str
