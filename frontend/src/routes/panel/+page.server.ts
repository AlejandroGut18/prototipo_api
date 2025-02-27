import type { PageServerLoad } from './$types';

import { PUBLIC_API_URL } from '$env/static/public';
import { error } from '@sveltejs/kit';

// src/routes/panel/+page.server.ts
import { fail } from '@sveltejs/kit';

export const actions = {
    default: async ({ request }) => {
        const formData = await request.formData();

        // Extrae los datos del formulario
        const jugador = {
            cedula: formData.get('cedula'),
            nombre: formData.get('nombre'),
            apellido: formData.get('apellido'),
            fecha_nacimiento: formData.get('fecha_nacimiento'),
            correo: formData.get('correo'),
            telefono: formData.get('telefono'),
            equipo_id: Number(formData.get('equipo_id')),
            status_id: Number(formData.get('status_id')),
            genero: formData.get('genero'),
        };

        // Envía los datos a tu API
        const response = await fetch(`${PUBLIC_API_URL}/api/jugadores/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(jugador),
        });

        if (!response.ok) {
            return fail(400, { error: 'Error al agregar el jugador' });
        }

        // Retorna un mensaje de éxito
        return { success: true };
    },
};

export const load: PageServerLoad = async () => {
    try {
        // Realiza las tres solicitudes en paralelo
        const [torneosResponse, gruposResponse, jugadoresResponse, equiposResponse] = await Promise.all([
            fetch(`${PUBLIC_API_URL}/api/torneos/`),
            fetch(`${PUBLIC_API_URL}/api/grupos/`),
            fetch(`${PUBLIC_API_URL}/api/jugadores/`),
			fetch(`${PUBLIC_API_URL}/api/equipos/`)
        ]);

        // Verifica si alguna de las respuestas falló
        if (!torneosResponse.ok || !gruposResponse.ok || !jugadoresResponse.ok || !equiposResponse.ok) {
            // Lanza un error con el código de estado de la primera respuesta que falle
            const failedResponse = !torneosResponse.ok ? torneosResponse :
                                  !gruposResponse.ok ? gruposResponse :
                                  jugadoresResponse.ok ? jugadoresResponse : equiposResponse;
            error(failedResponse.status, 'Failed to fetch data');
        }

        // Convierte las respuestas a JSON
        const torneos = await torneosResponse.json() as Torneo[];
        const grupos = await gruposResponse.json() as Grupo[];
        const jugadores = await jugadoresResponse.json() as Jugador[];
		const equipos = await equiposResponse.json() as Equipo[];


        // Retorna los datos para que estén disponibles en la página
        return {
            torneos,
            grupos,
            jugadores,
			equipos
        };
    } catch (err) {
        error(500, 'Internal Server Error');
    }
};

// Tipos para los datos
type Torneo = {
    id: number;
    nombre: string;
    fecha_inicio: string;
    fecha_fin: string;
    ubicacion: string;
    status_id: number;
};

type Grupo = {
    id: number;
    nombre: string;
    fecha_inicio: string; 
    fecha_fin: string;    
    status_id: number;
    torneo_id: number;
};

type Jugador = {
    cedula: string;
    nombre: string;
    apellido: string;
    fecha_nacimiento: string;
    correo: string;
    telefono: string;
    equipo_id: number;
    status_id: number;
    genero: string;
};

type Equipo = {
    id: number;
    nombre: string;
	delegado_equipo: string;
	grupos_id: number;
    status_id: number;
}