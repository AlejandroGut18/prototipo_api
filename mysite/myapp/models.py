from django.db import models

# Create your models here.
class Status(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(default='activo', max_length=20, null=False, blank=False)
    descripcion = models.CharField(default='activo por defecto', max_length=100, null=False, blank=False)
    
    class Meta():
        db_table = 'status'

    def __str__(self):
        return f"{self.nombre}"

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=150, null=False, blank=False)
    
    class Meta():
        db_table = 'rol'
    
    def __str__(self):
        return f"{self.nombre}"

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=15, null=False, blank=False)
    nombre_usuario = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    correo = models.EmailField(null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_sesion = models.DateTimeField(auto_now_add=True)
    status_id = models.ForeignKey('Status', on_delete=models.CASCADE, db_column='status_id')
    rol_id = models.ForeignKey('Rol', on_delete=models.CASCADE, db_column='rol_id')
    
    class Meta():
        db_table = 'usuario'
    
    def __str__(self):
        return f"{self.cedula} ({self.nombre_usuario})"
    
class Torneo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    fecha_inicio = models.DateField(auto_now=False) 
    fecha_fin = models.DateField(null=True, blank=True)
    ubicacion = models.CharField(max_length=200, null=False, blank=False)
    status_id = models.ForeignKey('Status', on_delete=models.CASCADE, db_column='status_id')
    
    class Meta():
        db_table = 'torneo'
    
    def __str__(self):
        return f"{self.nombre}"
    
class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    status_id = models.ForeignKey('Status', on_delete=models.CASCADE, db_column='status_id')
    torneo_id = models.ForeignKey('Torneo', on_delete=models.CASCADE, db_column='torneo_id')
    
    class Meta():
        db_table = 'grupo'
    
    def __str__(self):
        return f"{self.nombre}"

class Grupo_equipo(models.Model):
    id = models.AutoField(primary_key=True)
    grupo_equipo_id = models.ForeignKey('Grupo', on_delete=models.CASCADE, db_column='grupo_equipo_id')
    equipo_grupo_id = models.ForeignKey('Equipo', on_delete=models.CASCADE, db_column='equipo_grupo_id')
    
    class Meta():
        db_table = 'grupo_equipo'
    
    def __str__(self):
        return f"{self.grupo_equipo_id}"

class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    delegado_equipo = models.ForeignKey("Usuario", on_delete=models.CASCADE, db_column='delegado_equipo')
    # estadisticas_equipo_id = models.ForeignKey("Estadisticas", on_delete=models.CASCADE, db_column='estadisticas_equipo_id')
    grupo_id = models.ForeignKey('Grupo_equipo', on_delete=models.CASCADE, db_column='grupo_id')
    status_id = models.ForeignKey('Status', on_delete=models.CASCADE, db_column='status_id')
    
    #logo = models.ImageField(upload_to='logos/', null=False, blank=False)
    
    class Meta():
        db_table = 'equipo'
    
    def __str__(self):
        return f"{self.nombre_equipo}"
    
class Estadisticas_equipo(models.Model):
    id = models.AutoField(primary_key=True)
    torneo_id = models.ForeignKey('Torneo', on_delete=models.CASCADE, db_column='torneo_id')
    grupo_id = models.ForeignKey('Grupo', on_delete=models.CASCADE, db_column='grupo_id')
    equipo_id = models.ForeignKey('Equipo', on_delete=models.CASCADE, db_column='equipo_id')
    victorias = models.IntegerField(default=0, null=False, blank=False)
    derrotas = models.IntegerField(default=0, null=False, blank=False)
    
    class Meta():
        db_table = 'estadisticas_partido'
    
    def __str__(self):
        return f"{self.id}"

class Status_jugador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(default='activo', max_length=20, null=False, blank=False)
    descripcion = models.CharField(default='activo por defecto', max_length=100, null=False, blank=False)
    
    class Meta():
        db_table = 'status_jugador'
    
    def __str__(self):
        return f"{self.nombre}"

class Jugador(models.Model):
    cedula = models.CharField(primary_key=True, max_length=15, null=False, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido = models.CharField(max_length=100, null=False, blank=False)
    fecha_nacimiento = models.DateField(auto_now=False)
    correo = models.EmailField(null=False, blank=False)
    telefono = models.CharField(max_length=15, null=False, blank=False)
    equipo_id = models.ForeignKey('Equipo', on_delete=models.CASCADE, db_column='equipo_id')
    status_id = models.ForeignKey('Status_jugador', on_delete=models.CASCADE, db_column='status_id')
    genero = models.CharField(max_length=1, null=False, blank=False)
    
    class Meta():
        db_table = 'jugador'
    
    def __str__(self):
        return f"{self.nombre}"
    
class Jugador_equipo(models.Model):
    id = models.AutoField(primary_key=True)
    jugador_id = models.ForeignKey('Jugador', on_delete=models.CASCADE, db_column='jugador_id')
    equipo_id = models.ForeignKey('Equipo', on_delete=models.CASCADE, db_column='equipo_id')
    
    class Meta():
        db_table = 'jugador_equipo'
    
    def __str__(self):
        return f"{self.jugador_id} {self.equipo_id}"
   
class Partido(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    #grupo_id = models.ForeignKey('Grupo', on_delete=models.CASCADE, db_column='grupo_id')
    torneo_id = models.ForeignKey("Torneo", on_delete=models.CASCADE, db_column='torneo_id')
    equipo_id = models.ForeignKey('Equipo', on_delete=models.CASCADE, db_column='equipo_id', related_name='partido_equipo')
    equipo_rival_id = models.ForeignKey('Equipo', on_delete=models.CASCADE, db_column='equipo_rival_id', related_name='partidos_rival')
    puntos = models.IntegerField(default=0, null=False, blank=False)
    puntos_rival = models.IntegerField(default=0, null=False, blank=False)
    status_id = models.ForeignKey('Status', on_delete=models.CASCADE, db_column='status_id')
    
    class Meta():
        db_table = 'partido'
    
    def __str__(self):
        return f"{self.id}"
    
class Estadisticas_Jugador(models.Model):
    id = models.AutoField(primary_key=True)
    torneo_id = models.ForeignKey("Torneo", on_delete=models.CASCADE, db_column='torneo_id')  
    #grupo_id = models.ForeignKey('Grupo', on_delete=models.CASCADE, db_column='grupo_id')
    equipo_id = models.ForeignKey("Equipo", on_delete=models.CASCADE, db_column='equipo_id')
    partido_id = models.ForeignKey("Partido", on_delete=models.CASCADE, db_column='partido_id')
    jugador_id = models.ForeignKey("Jugador",  on_delete=models.CASCADE, db_column='jugador_id')
    arrimes_lanzados = models.IntegerField(default=0, null=False, blank=False)
    arimes_buenos = models.IntegerField(default=0, null=False, blank=False)
    average_arrimes = models.IntegerField(default=0, null=False)
    bolas_lanzadas = models.IntegerField(default=0, null=False, blank=False)
    bolas_buenas = models.IntegerField(default=0, null=False, blank=False)
    average_bolas = models.IntegerField(default=0, null=False)
    rastreros_lazados = models.IntegerField(default=0, null=False, blank=False)
    rastreros_buenos = models.IntegerField(default=0, null=False, blank=False)
    average_rastrero = models.IntegerField(default=0, null=False)
    
    class Meta():
        db_table = 'estadisticas_jugador'
        
    def __str__(self):
        return f"{self.id}"
    
    
    
    