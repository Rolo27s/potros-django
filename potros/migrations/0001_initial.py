from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('cuerpo1', models.CharField(max_length=1500)),
                ('cuerpo2', models.CharField(max_length=2500)),
                ('fecha', models.DateField(auto_now=True)),
                ('imagen', models.ImageField(upload_to='imagenes/noticias/')),
            ],
        ),
    ]
