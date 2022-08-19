from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# 헬퍼 클래스
class UserManager(BaseUserManager):
    # 일반 유저 생성
    def create_user(self, email, username, contact, nickname, privillege, password=None):
        if not email:
            raise ValueError('이메일은 필수입니다')
        if not contact:
            raise ValueError('전화번호는 필수입니다')
        if not username:
            raise ValueError('아이디는 필수입니다')
        if not nickname:
            raise ValueError('유저이름은 필수입니다')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            contact = contact,
            nickname = nickname,
            privillege = privillege,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 유저 생성
    def create_superuser(self, email, username, contact, nickname, password=None):
        user = self.create_user(
            email,
            password = password,
            username = username,
            contact = contact,
            nickname = nickname
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(default='', max_length=30, null=False, blank=False)
    contact = models.CharField(max_length = 15, default='')
    nickname = models.CharField(default='', max_length=20, null=False, blank=False, unique=True)
    privillege = models.BooleanField(default=False)
    
    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    
    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD = 'nickname'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['username', 'email', 'contact', 'nickname']

    def __str__(self):
        return self.username