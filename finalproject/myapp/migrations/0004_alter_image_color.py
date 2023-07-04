# Generated by Django 4.2.2 on 2023-06-09 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_image_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='color',
            field=models.CharField(choices=[('red', 'Red'), ('green', 'Green'), ('blue', 'Blue'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('purple', 'Purple'), ('pink', 'Pink'), ('brown', 'Brown'), ('black', 'Black'), ('white', 'White'), ('gray', 'Gray'), ('cyan', 'Cyan'), ('magenta', 'Magenta'), ('lime', 'Lime'), ('olive', 'Olive'), ('maroon', 'Maroon'), ('navy', 'Navy'), ('teal', 'Teal'), ('aqua', 'Aqua'), ('silver', 'Silver'), ('gold', 'Gold'), ('bronze', 'Bronze'), ('beige', 'Beige'), ('azure', 'Azure'), ('ivory', 'Ivory'), ('lavender', 'Lavender'), ('coral', 'Coral'), ('salmon', 'Salmon'), ('tan', 'Tan'), ('turquoise', 'Turquoise'), ('violet', 'Violet'), ('indigo', 'Indigo'), ('crimson', 'Crimson'), ('fuchsia', 'Fuchsia'), ('orchid', 'Orchid'), ('plum', 'Plum'), ('khaki', 'Khaki'), ('chocolate', 'Chocolate'), ('tomato', 'Tomato'), ('wheat', 'Wheat'), ('snow', 'Snow'), ('seashell', 'Seashell'), ('salmon', 'Salmon')], default='white', max_length=20),
        ),
    ]
