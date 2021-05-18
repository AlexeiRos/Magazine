# Generated by Django 3.1.7 on 2021-04-02 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0018_remove_order_for_anonymous_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='for_anonymous_user',
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
    ]
