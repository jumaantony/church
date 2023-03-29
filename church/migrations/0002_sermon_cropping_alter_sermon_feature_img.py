# Generated by Django 4.1.7 on 2023-03-29 07:56

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sermon',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('feature_img', '300x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='feature_img',
            field=image_cropping.fields.ImageCropField(blank=True, null=True, upload_to='feature_img/'),
        ),
    ]