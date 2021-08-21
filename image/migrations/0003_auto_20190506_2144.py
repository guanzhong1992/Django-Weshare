from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('image', '0002_auto_20190506_2142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='image',
            name='user_like',
            field=models.ManyToManyField(blank=True, related_name='images_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
