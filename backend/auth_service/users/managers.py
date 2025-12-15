from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, role='CUSTOMER'):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, role=role)
        user.set_password(password)  # 🔥 HASHING HAPPENS HERE
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password, role='ADMIN')
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
