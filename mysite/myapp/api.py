from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

class LoginViewSet(viewsets.ViewSet):
    def create(self, request):
        correo = request.data.get('correo')
        password = request.data.get('password')

        # Autenticar al usuario
        user = authenticate(request, email=correo, password=password)

        if user is not None:
            # Si el usuario es válido, redirige o devuelve un token
            return Response({"message": "Login exitoso"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
        
        
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.AllowAny]
    
class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [permissions.AllowAny]
    
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]

class TorneoViewSet(viewsets.ModelViewSet):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerializer
    permission_classes = [permissions.AllowAny]

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = [permissions.AllowAny]
'''
class GrupoEquipoViewSet(viewsets.ModelViewSet):
    queryset = Grupo_equipo.objects.all()
    serializer_class = GrupoEquipoSerializer
    permission_classes = [permissions.AllowAny]
'''
class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    permission_classes = [permissions.AllowAny]

class EstadisticasEquipoViewSet(viewsets.ModelViewSet):
    queryset = Estadisticas_equipo.objects.all()
    serializer_class = EstadisticasEquipoSerializer
    permission_classes = [permissions.AllowAny]

class StatusJugadorViewSet(viewsets.ModelViewSet):
    queryset = Status_jugador.objects.all()
    serializer_class = StatusJugadorSerializer
    permission_classes = [permissions.AllowAny]

class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
    permission_classes = [permissions.AllowAny]

class JugadorEquipoViewSet(viewsets.ModelViewSet):
    queryset = Jugador_equipo.objects.all()
    serializer_class = JugadorEquipoSerializer
    permission_classes = [permissions.AllowAny]

class PartidoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer
    permission_classes = [permissions.AllowAny]

class EstadisticasJugadorViewSet(viewsets.ModelViewSet):
    queryset = Estadisticas_Jugador.objects.all()
    serializer_class = EstadisticasJugadorSerializer
    permission_classes = [permissions.AllowAny]