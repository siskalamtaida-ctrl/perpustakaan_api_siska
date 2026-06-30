from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.get_or_create(
        username='adminss',
        defaults={
            'password': make_password('siska321'),
            'is_superuser': True,
            'is_staff': True,
        }
    )

class Migration(migrations.Migration):
    dependencies = [
        ('layanan', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_superuser),
    ]