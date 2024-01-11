from django.contrib.auth.models import BaseUserManager

class UsuarioFPManager(BaseUserManager):
    def create_user(self, email, documento, password=None, **extra_fields):
        if not documento:
            raise ValueError('El número de documento es obligatorio')
        email = self.normalize_email(email)
        user = self.model(documento=documento, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, documento, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, documento, password, **extra_fields)
