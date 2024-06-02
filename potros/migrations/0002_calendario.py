from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('local', models.CharField(max_length=255)),
                ('logo_local', models.ImageField(upload_to='imagenes/calendario/')),
                ('hora', models.CharField(max_length=5)),
                ('logo_visitante', models.ImageField(upload_to='imagenes/calendario/')),
                ('visitante', models.CharField(max_length=255)),
                ('jornada', models.CharField(max_length=100)),
            ],
        ),
    ]
