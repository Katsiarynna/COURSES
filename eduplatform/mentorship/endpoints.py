from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import permissions, mixins, generics
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from itertools import chain
from rest_framework.routers import DefaultRouter

from .models import User, Teacher, Student, Group, Email
from .serializers import \
    (UserSerializer, TeacherSerializer, StudentSerializer,
     GroupSerializer, TeacherStudentSerializer, RegisterSerializer, EmailSerializer)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.AllowAny]


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]


class EmailViewSet(ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]


router = DefaultRouter()
router.register(r'emails', EmailViewSet, basename='email')


class GroupStudentAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        group_id = self.kwargs["id"]
        group = get_object_or_404(Group, id=group_id)
        return Student.objects.filter(group=group)


class GroupMembersAPIView(ListAPIView):
    serializer_class = TeacherStudentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        group_id = self.kwargs["id"]
        group = get_object_or_404(Group, id=group_id)
        students = Student.objects.filter(group=group)
        teacher = Teacher.objects.filter(group=group)
        members = list(chain(students, teacher))
        return members


class RegisterUserViewSet(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return HttpResponse(f"User {serializer.validated_data['email']} created!", status=201)

class EmailListCreateView(ListCreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user = self.request.user
        return Email.objects.filter(recipient=user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class EmailDetailView(generics.RetrieveAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [permissions.AllowAny]
