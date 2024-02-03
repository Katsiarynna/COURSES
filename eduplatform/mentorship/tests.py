from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from .consts import (
      USER_DATA, create_user, create_teacher,
      create_student, create_course, create_group, create_email)
from .serializers import (
      UserSerializer, TeacherSerializer,
      StudentSerializer, GroupSerializer, EmailSerializer)

__all__ = {"CreateUserTest", 'ReadUserTest', 'UpdateUserTest', 'DeleteUserTest',
           'CreateTeacherTest', 'ReadTeacherTest', 'UpdateTeacherTest', 'DeleteTeacherTest',
           'CreateStudentTest', 'ReadStudentTest', 'UpdateStudentTest', 'DeleteStudentTest',
           'CreateGroupTest', 'ReadGroupTest', 'UpdateGroupTest', 'DeleteGroupTest'}


class CreateUserTest(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        response = self.client.post(url, data=USER_DATA, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_read_user_list(self):
        url = reverse("user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_user_detail(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.data = UserSerializer(self.user).data
        self.data.update({"first_name": "newName_test"})

    def test_update_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_delete_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_create_user(self):
        url = reverse('teacher-list')
        response = self.client.post(
              url,
              data={"experience": 12, "user": self.user.id},
              format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)

    def test_read_teacher_list(self):
        url = reverse("teacher-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_teacher_detail(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.data = TeacherSerializer(self.teacher).data
        self.data.update({"experience": 20})

    def test_update_teacher(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)

    def test_delete_teacher(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_create_student(self):
        url = reverse('student-list')
        response = self.client.post(
              url,
              data={"age": 22, "user": self.user.id, "rating": 85.30},
              format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)

    def test_read_student_list(self):
        url = reverse("student-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_student_detail(self):
        url = reverse("student-detail", args=[self.student.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)
        self.data = StudentSerializer(self.student).data
        self.data.update({"age": 32})

    def test_update_student(self):
        url = reverse("student-detail", args=[self.student.id])
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)

    def test_delete_student(self):
        url = reverse("student-detail", args=[self.student.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# GROUP
class CreateGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)

    def test_create_group(self):
        url = reverse('group-list')
        response = self.client.post(
              url,
              data={
                    "group_name": "Test",
                    "teacher": self.teacher.id,
                    "student": [self.student.id],
                    "course": self.course.id},
              format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.group = create_group(teacher_id=self.teacher, course_id=self.course)

    def test_read_group_list(self):
        url = reverse("group-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_group_detail(self):
        url = reverse("group-detail", args=[self.group.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.group = create_group(teacher_id=self.teacher, course_id=self.course)
        self.data = GroupSerializer(self.group).data
        self.data.update({"group_name": "newName"})

    def test_update_group(self):
        url = reverse("group-detail", args=[self.group.id])
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.group = create_group(teacher_id=self.teacher, course_id=self.course)

    def test_delete_group(self):
        url = reverse("group-detail", args=[self.group.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateEmailTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.student = create_student(self.user)
        self.email = create_email(sender=self.user, recipients=[self.teacher])

    def test_create_email(self):
        url = reverse("email-list")
        response = self.client.post(
            url,
            data={
                "subject": "Test",
                "email": self.email.id,
                "message": "test_text",
                "is_read": True},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
