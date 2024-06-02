from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('potros', '0003_equipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='provincia',
            new_name='estado',
        ),
    ]
