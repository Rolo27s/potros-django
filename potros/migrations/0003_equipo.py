from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potros', '0002_calendario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_jugador', models.ImageField(upload_to='imagenes/equipo/')),
                ('nombre_jugador', models.CharField(max_length=100)),
                ('dorsal', models.CharField(max_length=8)),
                ('posicion', models.CharField(max_length=8)),
                ('estadistica1', models.CharField(max_length=8)),
                ('estadistica2', models.CharField(max_length=8)),
                ('edad', models.IntegerField()),
                ('experiencia', models.IntegerField()),
                ('provincia', models.CharField(max_length=100)),
            ],
        ),
    ]
