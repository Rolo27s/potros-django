from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potros', '0004_rename_provincia_equipo_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes/instagram/')),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
    ]
