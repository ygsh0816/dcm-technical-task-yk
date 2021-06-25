# Generated by Django 3.0.7 on 2020-07-07 17:51
import os
from os import walk

from django.db import migrations
from django.conf import settings


def clear_data(apps, _):
    TestFilePath = apps.get_model('api', 'TestFilePath')
    TestEnvironment = apps.get_model('api', 'TestEnvironment')
    TestFilePath.objects.all().delete()
    TestEnvironment.objects.all().delete()


def init_data(apps, _):
    TestFilePath = apps.get_model('api', 'TestFilePath')
    TestEnvironment = apps.get_model('api', 'TestEnvironment')

    paths = []
    for base_dir in settings.TEST_BASE_DIRS:
        for (dirpath, dirnames, filenames) in walk(base_dir):
            for filename in filenames:
                if not filename.endswith('.py') or filename == '__init__.py':
                    continue
                paths.append(TestFilePath(path=os.path.join(base_dir, filename)[6:]))
    TestFilePath.objects.bulk_create(paths)

    envs = []
    for i in range(1, 101):
        envs.append(TestEnvironment(name='env' + str(i)))
    TestEnvironment.objects.bulk_create(envs)


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init_data, reverse_code=clear_data)

    ]