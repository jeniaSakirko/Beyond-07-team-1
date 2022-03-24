from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ('msgboard', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        from msgboard.models import Message
        from django.contrib.auth.models import User

        test_data = [
            ('Test User1', 'A simple test message'),
            ('Test User2', 'Another simple test message'),
            ('test', 'this is txt'),
        ]

        test_user_data = [
            ('email 1', 'username 1', 'password 1'),
            ('email 2', 'username 2', 'password 2'),
            ('testuser@gmail.com', 'testuser', 'testpassowrd'),
        ]

        with transaction.atomic():
            for email, username, password in test_user_data:
                User(email=email, username=username, password=password)
            for author, text in test_data:
                Message(author=author, text=text).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
