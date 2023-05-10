from django.contrib.auth.base_user import BaseUserManager



class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, name, password, **extra_fields):
        """
        Create and save a user with the given email, name and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        if not name:
            raise ValueError("The Name must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password, **extra_fields):
        """
        Create and save a SuperUser with the given email, name and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, name, password, **extra_fields)