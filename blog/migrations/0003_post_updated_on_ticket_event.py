# Generated by Django 4.2.15 on 2024-08-28 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_event_post_excerpt_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_tickets', to='blog.event'),
        ),
    ]
