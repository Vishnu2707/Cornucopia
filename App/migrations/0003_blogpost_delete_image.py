# Generated by Django 4.2.2 on 2023-06-13 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_image_alter_post_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]