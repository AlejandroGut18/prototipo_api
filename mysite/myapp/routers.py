from rest_framework.routers import DefaultRouter
from .api import *

router = DefaultRouter()

# Registro de rutas
router.register('api/status', StatusViewSet)

router.register('api/roles', RolViewSet)

router.register('api/usuarios', UsuarioViewSet)

router.register('api/torneos', TorneoViewSet)

router.register('api/grupos', GrupoViewSet)

router.register('api/grupo-equipos', GrupoEquipoViewSet)

router.register('api/equipos', EquipoViewSet)

router.register('api/estadisticas-equipos', EstadisticasEquipoViewSet)

router.register('api/status-jugadores', StatusJugadorViewSet)

router.register('api/jugadores', JugadorViewSet)

router.register('api/jugador-equipos', JugadorEquipoViewSet)

router.register('api/partidos', PartidoViewSet)

router.register('api/estadisticas-jugadores', EstadisticasJugadorViewSet)