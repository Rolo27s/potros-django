from django.db import models

# Tabla Noticias
class Noticias(models.Model):
    titulo = models.CharField(max_length=255)
    cuerpo1 = models.CharField(max_length=1500)
    cuerpo2 = models.CharField(max_length=2500)
    fecha = models.DateField(auto_now=True)
    imagen = models.ImageField(upload_to='imagenes/noticias/')

    def to_json(self):
        return {'id':self.id, 
                'titulo':self.titulo, 
                'cuerpo1':self.cuerpo1, 
                'cuerpo2':self.cuerpo2, 
                'fecha':self.fecha,
                'imagen':self.imagen.url }
       
# Tabla Calendario
class Calendario(models.Model):
    fecha = models.DateField(auto_now=False)
    local = models.CharField(max_length=255)
    logo_local = models.ImageField(upload_to='imagenes/calendario/')
    hora = models.CharField(max_length=5)
    logo_visitante = models.ImageField(upload_to='imagenes/calendario/')
    visitante = models.CharField(max_length=255)
    jornada = models.CharField(max_length=100)

    def to_json(self):
        return {'id':self.id, 
                'fecha':self.fecha, 
                'local':self.local, 
                'logo_local':self.logo_local.url,
                'hora':self.hora, 
                'logo_visitante':self.logo_visitante.url,
                'visitante':self.visitante, 
                'jornada':self.jornada,  }

# Tabla equipos
class Equipo(models.Model):
    foto_jugador = models.ImageField(upload_to='imagenes/equipo/')
    nombre_jugador = models.CharField(max_length=100)
    dorsal = models.CharField(max_length=8)
    posicion = models.CharField(max_length=8)
    estadistica1 = models.CharField(max_length=8)
    estadistica2 = models.CharField(max_length=8)
    edad = models.IntegerField()
    experiencia = models.IntegerField()
    estado = models.CharField(max_length=100) # Pendiente de ajustar a 'pais' con carga de datos reales

    def to_json(self):
        return {'id':self.id, 
                'foto_jugador':self.foto_jugador.url, 
                'nombre_jugador':self.nombre_jugador, 
                'dorsal':self.dorsal,
                'posicion':self.posicion, 
                'estadistica1':self.estadistica1,
                'estadistica2':self.estadistica2, 
                'edad':self.edad,
                'experiencia':self.experiencia, 
                'estado':self.estado,   }
    
# Tabla fotos (solución temporal sustituyendo a API de Instragram)
class Instagram(models.Model):
    imagen = models.ImageField(upload_to='imagenes/instagram/')
    fecha = models.DateField(auto_now=True)
    descripcion = models.CharField(max_length=500)

    def to_json(self):
        return {'id':self.id,
                'imagen':self.imagen.url, 
                'fecha':self.fecha,
                'descripcion':self.descripcion }