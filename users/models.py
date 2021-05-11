from uuid import uuid4
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import Group
from .managers import MyUserManager

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=150, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    email2 = models.EmailField(_('alternative mail address'), unique=True,null=True, blank=True)
    remember_me = models.BooleanField(_('remember me'), default=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Profile(models.Model):
    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def f(self, filename):
        ext = filename.split('.')[-1]
        return '{}.{}'.format(uuid4().hex, ext)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.IntegerField(_('mobile number'), null=True, blank=True)
    is_email_confirmed = models.BooleanField(default=False, null=True, blank=True)
    is_email2_confirmed = models.BooleanField(default=False, null=True, blank=True)
    bio = models.TextField(_('bio'), max_length=500, null=True, blank=True)
    birth_date = models.DateField(_('birth date'), null=True, blank=True)
    address = models.TextField(_('address'), max_length=150, null=True, blank=True)
    city = models.CharField(_('city'), max_length=100, null=True, blank=True)
    username = models.CharField(_('username'), max_length=100, null=True, blank=True)
    district = models.CharField(_('district'), max_length=100, null=True, blank=True)
    state = models.CharField(_('state'), max_length=100, null=True, blank=True)
    country = models.CharField(_('country'), max_length=100, null=True, blank=True)
    postal_code = models.CharField(_('postal code'), max_length=12, null=True, blank=True)
    profile_image = models.ImageField(_('profile image'), upload_to=f, null=True, blank=True)
    company = models.CharField(_('company'), max_length=100, null=True, blank=True)    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()