from rest_framework import serializers
from .models import *

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'nombre', 'descripcion']
        
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre', 'descripcion']
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 'cedula', 'nombre_usuario', 'password', 'correo',
            'fecha_creacion', 'fecha_ultima_sesion', 'status_id', 'rol_id'
        ]
        
                
class TorneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        fields = [
            'id', 
            'nombre', 
            'fecha_inicio', 
            'fecha_fin', 
            'ubicacion', 
            'status_id'
        ]
        
class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = [
            'id', 
            'nombre', 
            'fecha_inicio', 
            'fecha_fin', 
            'status_id', 
            'torneo_id'
        ]
        
'''        
class GrupoEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo_equipo
        fields = [
            'id', 
            'grupo_equipo_id', 
            'equipo_grupo_id'
        ]
'''     
   
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = [
            'id', 
            'nombre', 
            'delegado_equipo', 
            'grupo_id', 
            'status_id'
        ]     

class EstadisticasEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadisticas_equipo
        fields = [
            'id', 
            'torneo_id', 
            'grupo_id', 
            'equipo_id', 
            'victorias', 
            'derrotas'
        ]
        
class StatusJugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status_jugador
        fields = [
            'id', 
            'nombre', 
            'descripcion'
        ]
        
class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = [
            'cedula', 
            'nombre', 
            'apellido', 
            'fecha_nacimiento', 
            'correo', 
            'telefono', 
            'equipo_id', 
            'status_id', 
            'genero',
            #'estadisticas_id'
        ]
        
class JugadorEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador_equipo
        fields = [
            'id', 
            'jugador_id', 
            'equipo_id'
        ]
        
class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = [
            'id', 
            'fecha', 
            'torneo_id', 
            'equipo_id', 
            'equipo_rival_id', 
            'puntos', 
            'puntos_rival', 
            'status_id'
        ]

class EstadisticasJugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadisticas_Jugador
        fields = [
            'id', 
            'fecha',
            'torneo_id', 
            'equipo_id', 
            'partido_id', 
            'jugador_id', 
            'arrimes_lanzados', 
            'arimes_buenos', 
            'average_arrimes', 
            'bolas_lanzadas', 
            'bolas_buenas', 
            'average_bolas', 
            'rastreros_lazados', 
            'rastreros_buenos', 
            'average_rastrero'
        ]