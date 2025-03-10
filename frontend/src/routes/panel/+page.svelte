<script lang="ts">
	import { onMount } from 'svelte';
	import { writable } from 'svelte/store';
	
	import type { SubmitFunction } from '@sveltejs/kit';

	import { Home, Table, Users, Trophy, UsersRound } from 'lucide-svelte';
	export let data;
	let { torneos, grupos, jugadores, equipos } =  data;
	let form;
	import { enhance } from '$app/forms';

	let busquedaGeneral = '';  // Variable de búsqueda única

    // Función genérica de filtrado
    $: datosFiltrados = busquedaGeneral
        ? (tablaVisible === 'jugadores' ? jugadores.filter(j => j.cedula.includes(busquedaGeneral)) :
           tablaVisible === 'equipos' ? equipos.filter(e => String(e.id).includes(busquedaGeneral)) :
           tablaVisible === 'torneos' ? torneos.filter(t => String(t.id).includes(busquedaGeneral)) :
           tablaVisible === 'grupos' ? grupos.filter(g => String(g.id).includes(busquedaGeneral)) : [])
        : (tablaVisible === 'jugadores' ? jugadores :
           tablaVisible === 'equipos' ? equipos :
           tablaVisible === 'torneos' ? torneos :
           tablaVisible === 'grupos' ? grupos : []);

	let busquedaCedula = '';

	// Función para filtrar jugadores por cédula
	$: jugadoresFiltrados = busquedaCedula
		? jugadores.filter((jugador) => jugador.cedula.includes(busquedaCedula))
		: jugadores;
	//

	let isJugadorModalOpen = false;
	let isEquipoModalOpen = false;

	function abrirJugadorModal() {
		isJugadorModalOpen = true;
	}

	function cerrarJugadorModal() {
		isJugadorModalOpen = false;
	}

	function abrirEquipoModal() {
		isEquipoModalOpen = true;
	}

	function cerrarEquipoModal() {
		isEquipoModalOpen = false;
	}
	let isModalOpen = false;
	function abrirModal() {
		isModalOpen = true;
	}

	// Función para cerrar el modal
	function cerrarModal() {
		isModalOpen = false;
	}
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

	// Estado inicial del formulario
	let jugador: Jugador = {
		cedula: '',
		nombre: '',
		apellido: '',
		fecha_nacimiento: '',
		correo: '',
		telefono: '',
		equipo_id: 1,
		status_id: 1,
		genero: 'M'
	};

	type Equipo = {
		id: number;
		nombre: string;
		delegado_equipo: string;
		grupo_id: number;
		status_id: number;
	};

	let equipo: Equipo = {
		id: 0,
		nombre: '',
		delegado_equipo: '',
		grupo_id: 1,
		status_id: 1
	};

	let isUserMenuOpen = false;
	let showLogoutModal = false;
	let tablaVisible: 'Home' | 'torneos' | 'equipos' | 'jugadores' | 'grupos' = 'Home';

	// Funciones para mostrar la tabla correspondiente
	function mostrarHome() {
		tablaVisible = 'Home';
	}

	function mostrarTorneos() {
		tablaVisible = 'torneos';
	}

	function mostrarEquipos() {
		tablaVisible = 'equipos';
	}

	function mostrarJugadores() {
		tablaVisible = 'jugadores';
	}

	function mostrarGrupos() {
		tablaVisible = 'grupos';
	}

	// Función para abrir el modal correspondiente
	function abrirModalAgregar() {
		if (tablaVisible === 'torneos') {
		} else if (tablaVisible === 'equipos') {
		} else if (tablaVisible === 'jugadores') {
		} else if (tablaVisible === 'grupos') {
		}
	}

	let showEquipoModal = true;
	let showJugadorModal = true;
	function closeEquipoModal() {
		showEquipoModal = false;
	}

	function closeJugadorModal() {
		showJugadorModal = false;
	}

	function toggleUserMenu() {
		isUserMenuOpen = !isUserMenuOpen;
	}

	function confirmLogout() {
		showLogoutModal = true;
	}

	function logout() {
		window.location.href = '/';
	}

	function cancelLogout() {
		showLogoutModal = false;
	}

	let isMenuOpen = writable(true);
	let isTorneoOpen = writable(false);

	function toggleMenu() {
		isMenuOpen.update((n) => !n);
	}

	function toggleTorneo() {
		isTorneoOpen.update((n) => !n);
	}
	/**
	 * @param {{ result: any; update: any; }} param0
	 */
	function handleEnhance({ result, update }: { result: any; update: any }) {
        if (result?.success) {
            cerrarJugadorModal(); // Cierra el modal si la respuesta es exitosa
			cerrarEquipoModal();
        }
    }

</script>

<header>
	<div class="left">
		<div class="menu-container">
			<button class="menu" on:click={toggleMenu}>
				<div></div>
				<div></div>
				<div></div>
			</button>
			<div class="brand">
				<img src="logo-image.png" alt="logo-menu" class="logo" />
				<div class="name">
					<span class="t1">Copa de</span>
					<span class="t2">Campeones</span>
				</div>
			</div>
		</div>
	</div>
	<div class="right">
		<button class="users" on:click={toggleUserMenu}>
			<img src="icons/icon-admin.svg" alt="icon-admin" />
		</button>
		{#if isUserMenuOpen}
			<div class="user-menu">
				<div class="user-info">
					<strong>Admin</strong>
				</div>
				<ul>
					<li class="logout-item">
						<button on:click={confirmLogout}>
							<img src="icons/icon-logout.svg" alt="icon-logout" class="icon-logout" />
							Salir
						</button>
					</li>
				</ul>
			</div>
		{/if}
	</div>
</header>

<div class="sidebar {$isMenuOpen ? 'open' : ''}">
	<button class="toggle-btn" on:click={toggleMenu}>☰</button>

	<ul>
		<li>
			<a href="" on:click={mostrarHome}>
				<Home size={24} /> <span>Home</span>
			</a>
		</li>

		<li>
			<a href="#" on:click={toggleTorneo}>
				<Table size={24} /> <span>Tablas</span> ▼
			</a>
			<ul class="submenu {$isTorneoOpen ? 'open' : ''}">
				<li><a href="" on:click={mostrarTorneos}><Trophy size={20} />Torneo</a></li>
				<li><a href="" on:click={mostrarEquipos}><Users size={20} /> Equipos</a></li>
				<li><a href="" on:click={mostrarJugadores}><UsersRound size={20} /> Jugadores</a></li>
				<li><a href="" on:click={mostrarGrupos}><Trophy size={20} /> Grupos</a></li>
			</ul>
		</li>
	</ul>
</div>

{#if Error}
	<div class="error">{Error}</div>
{/if}

<!-- Contenido dinámico según la vista actual -->
<div class="content">
	<div class="header-table">
		<h2>
			{#if tablaVisible === 'Home'}
				<div class="home-container">
					<div class="home-content">
						<h3>BIENVENIDO ADMIN</h3>
						<p>
							Desde aquí puedes gestionar torneos, equipos, jugadores y grupos.<br /><b
								>Utiliza el menú lateral para navegar.</b
							>
						</p>
						<img class="home-logo" src="/logo-image.png" alt="logo" />
					</div>
				</div>
			{:else if tablaVisible === 'torneos'}
				Torneos
			{:else if tablaVisible === 'equipos'}
				Equipos
			{:else if tablaVisible === 'jugadores'}
				Jugadores
			{:else if tablaVisible === 'grupos'}
				Grupos
			{/if}
		</h2>
	</div>

	<!-- Tablas -->
	{#if tablaVisible === 'torneos'}
		<table>
			<thead>
				<tr>
					<th>ID</th>
					<th>Nombre</th>
					<th>Fecha Inicio</th>
					<th>Fecha Fin</th>
					<th>Ubicación</th>
					<th>Status</th>
					<th>Acciones</th>
				</tr>
			</thead>
			<tbody>
				{#each torneos as torneo}
					<tr>
						<td>{torneo.id}</td>
						<td>{torneo.nombre}</td>
						<td>{torneo.fecha_inicio}</td>
						<td>{torneo.fecha_fin}</td>
						<td>{torneo.ubicacion}</td>
						<td>{torneo.status_id}</td>
						<td>
							<div class="acciones">
								<button>Modificar</button>
							</div>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
		<button class="btn-agregar" on:click={abrirModalAgregar}> Agregar </button>
	{/if}

	{#if tablaVisible === 'equipos'}
		<table>
			<thead>
				<tr>
					<th>ID</th>
					<th>Nombre</th>
					<th>Delegado</th>
					<th>Status</th>
					<th>Grupo</th>
					<th>Acciones</th>
				</tr>
			</thead>
			<tbody>
				{#each equipos as equipo}
					<tr>
						<td>{equipo.id}</td>
						<td>{equipo.nombre}</td>
						<td>{equipo.delegado_equipo}</td>
						<td>{equipo.status_id}</td>
						<td>{equipo.grupo_id}</td>
						<td>
							<div class="acciones">
								<button>Modificar</button>
							</div>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
		<button class="btn-agregar" on:click={abrirEquipoModal}> Agregar </button>
	{/if}

	{#if tablaVisible === 'jugadores'}
		<div class="busqueda">
			<label for="buscar-cedula">Buscar por cédula:</label>
			<input
				type="text"
				id="buscar-cedula"
				bind:value={busquedaCedula}
				placeholder="Ingrese la cédula"
			/>
		</div>
		<table>
			<thead>
				<tr>
					<th>Cedula</th>
					<th>Nombre</th>
					<th>Apellido</th>
					<th>Correo</th>
					<th>Género</th>
					<th>Fecha de Nacimiento</th>
					<th>Acciones</th>
				</tr>
			</thead>
			<tbody>
				{#each jugadoresFiltrados as jugador}
					<tr>
						<td>{jugador.cedula}</td>
						<td>{jugador.nombre}</td>
						<td>{jugador.apellido}</td>
						<td>{jugador.correo}</td>
						<td>{jugador.genero}</td>
						<td>{jugador.fecha_nacimiento}</td>
						<td>
							<div class="acciones">
								<button>Modificar</button>
							</div>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
		<button class="btn-agregar" on:click={abrirJugadorModal}> Agregar </button>
	{/if}

	{#if tablaVisible === 'grupos'}
		<table>
			<thead>
				<tr>
					<th>ID</th>
					<th>Nombre</th>
					<th>Fecha Inicio</th>
					<th>Fecha Fin</th>
					<th>Torneo</th>
					<th>Acciones</th>
				</tr>
			</thead>
			<tbody>
				{#each grupos as grupo}
					<tr>
						<td>{grupo.id}</td>
						<td>{grupo.nombre}</td>
						<td>{grupo.fecha_inicio}</td>
						<td>{grupo.fecha_fin}</td>
						<td>{grupo.torneo_id}</td>
						<td>
							<div class="acciones">
								<button>Modificar</button>
							</div>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
		<button class="btn-agregar" on:click={abrirModalAgregar}> Agregar </button>
	{/if}
</div>

{#if showLogoutModal}
	<div class="modal-overlay">
		<div class="modal">
			<h2>¿Estás seguro de que quieres salir?</h2>
			<div class="modal-buttons">
				<button on:click={logout}>Sí, salir</button>
				<button on:click={cancelLogout}>Cancelar</button>
			</div>
		</div>
	</div>
{/if}
{#if isJugadorModalOpen}
	<div class="modal-overlay">
		<div class="modal">
			<h2>Agregar Jugador</h2>
			<form method="POST" action="?/agregarJugador" use:enhance={cerrarJugadorModal}>				
				<label for="cedula">Cédula:</label>
				<input type="text" id="cedula" name="cedula" bind:value={jugador.cedula} required />

				<label for="nombre">Nombre:</label>
				<input type="text" id="nombre" name="nombre" bind:value={jugador.nombre} required />

				<label for="apellido">Apellido:</label>
				<input type="text" id="apellido" name="apellido" bind:value={jugador.apellido} required />

				<label for="fecha_nacimiento">Fecha de Nacimiento:</label>
				<input
					type="date"
					id="fecha_nacimiento"
					name="fecha_nacimiento"
					bind:value={jugador.fecha_nacimiento}
					required
				/>

				<label for="correo">Correo:</label>
				<input type="email" id="correo" name="correo" bind:value={jugador.correo} required />

				<label for="telefono">Teléfono:</label>
				<input type="tel" id="telefono" name="telefono" bind:value={jugador.telefono} required />

				<label for="equipo_id">Equipo ID:</label>
				<input
					type="number"
					id="equipo_id"
					name="equipo_id"
					bind:value={jugador.equipo_id}
					required
					min="1"  
					max="2" 
				/>

				<label for="status_id">Status ID:</label>
				<input
					type="number"
					id="status_id"
					name="status_id"
					bind:value={jugador.status_id}
					min="1"  
					max="2" 
					required
				/>

				<label for="genero">Género:</label>
				<select id="genero" name="genero" bind:value={jugador.genero}>
					<option value="M">Masculino</option>
					<option value="F">Femenino</option>
				</select>

				<div class="modal-buttons">
					<button type="submit">Agregar</button>
					<button type="button" on:click={cerrarJugadorModal}>Cancelar</button>
				</div>
			</form>
		</div>
	</div>
{/if}

<!-- Modal de Equipo -->
{#if isEquipoModalOpen}
	<div class="modal-overlay">
		<div class="modal">
			<h2>Agregar Equipo</h2>
            <form method="POST" action="?/agregarEquipo" use:enhance={handleEnhance}>
				<label for="nombre">Nombre:</label>
				<input type="text" id="nombre" name="nombre" bind:value={equipo.nombre} required />

				<label for="delegado_equipo">Delegado:</label>
				<input
					type="number"
					id="delegado_equipo"
					name="delegado_equipo"
					bind:value={equipo.delegado_equipo}
					min="1"  
					max="2" 
					required
				/>

				<label for="grupo_id">Grupo:</label>
				<input 
					type="number" 
					id="grupo_id" 
					name="grupo_id" 	
					bind:value={equipo.grupo_id}
					min="1"  
					max="2" 
				required />

				<label for="status_id">Status:</label>
				<select id="status_id" name="status_id" bind:value={equipo.status_id}>
					<option value="1">Activo</option>
					<option value="2">Inactivo</option>
				</select>

				<div class="modal-buttons">
					<button type="submit">Agregar</button>
					<button type="button" on:click={cerrarEquipoModal}>Cancelar</button>
				</div>
			</form>
		</div>
	</div>
{/if}

<style>
	.home-container {
		translate: 24%;
		position: relative;
		display: flex;
		justify-content: center;
		align-items: center;
		min-height: 10vh; /* Ocupa toda la altura de la pantalla */
		padding: 1px;
		overflow: hidden;
	}

	/* Contenido principal */
	.home-content {
		position: relative;
		text-align: center;
		color: white;
		max-width: 700px;
		width: 100%; /* Asegura que el contenido no exceda el ancho máximo */
		padding: 0.1rem; /* Espaciado interno */
	}

	/* Título */
	.home-content h3 {
		font-size: 1.9rem;
		margin-bottom: 1rem;
		color: var(--gold);
		text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
	}

	/* Párrafo */
	.home-content p {
		font-size: 1.2rem;
		line-height: 1.6;
		margin-bottom: 2rem;
		color: rgb(200, 200, 200); /* Color gris claro para mejor legibilidad */
		text-align: center; /* Asegura que el texto esté centrado */
	}

	/* Logo */
	.home-logo {
		display: block; /* Hace que el logo sea un bloque para poder centrarlo */
		width: 350px;
		height: 290px;
		margin: 0 auto; /* Centra el logo horizontalmente */
		filter: drop-shadow(2px 2px 4px rgba(0, 0, 0, 0.3));
	}
	.busqueda {
		margin-bottom: 20px;
	}

	.busqueda label {
		margin-right: 10px;
	}

	.busqueda input {
		padding: 8px;
		border: 1px solid #ccc;
		border-radius: 4px;
	}
	@import url('https://fonts.googleapis.com/css2?family=Nunito+Sans:ital,opsz,wght@0,6..12,200..1000;1,6..12,200..1000&display=swap');
	:root {
		--background-color: #ffffff;
		--text-title-color: #053d4e;
		--text-color: #32363b;
		--icon-color: #32363b;
		--icon-menu-color: #707780;
		--menu-color: #707780;
		--text-selected-color: #355cc0;
		--background-hover: #f7f9fa;
		--border-color: #e6e9ed;
		--red: #ff0000;
		--green: #0bc00b;
		--gold: #ffd700;
		--modal-background: #1c2a3a;
		--modal-border: #2c3e50;
		--button-hover: #2c3e50;
		--modal-color: #142130;
	}
	* {
		margin: 0;
		padding: 0;
		box-sizing: border-box;
		font-family: 'Nunito Sans', serif;
	}
	.logo-home {
		display: flex;
		justify-content: center;
	}
	.home {
		text-align: center;
		padding: 2rem;
	}

	.logo-home {
		width: 150px;
		height: 150px;
		margin-bottom: 1rem;
	}

	.home h1 {
		font-size: 2rem;
		margin-bottom: 1rem;
	}

	.home p {
		font-size: 1.2rem;
		color: #666;
	}

	header {
		z-index: 300;
		width: 100%;
		display: flex;
		justify-content: space-between;
		padding: 0.45rem 2rem 0.45rem 1.27rem;
		border-bottom: 1px solid var(--border-color);
		position: fixed;
		background-color: #142130;
		top: 0;
		left: 0;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}
	.menu-container {
		height: 100%;
		display: flex;
		align-items: center;
		gap: 1rem;
	}
	.menu {
		width: 24px;
		height: 18px;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		background: none;
		border: none;
		padding: 0;
		cursor: pointer;
	}
	.menu div {
		width: 100%;
		height: 3px;
		background-color: white;
		transition:
			transform 0.3s ease,
			opacity 0.3s ease;
	}
	.menu:hover div {
		background-color: var(--gold);
	}
	.left {
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.brand {
		display: flex;
		justify-content: center;
		align-items: center;
		gap: 0.6rem;
	}
	.brand .logo {
		width: 4.9rem;
		display: flex;
		justify-content: center;
		gap: 1.4rem;
	}
	.brand .name {
		font-size: 17px;
		color: var(--text-title-color);
		width: 7.1rem;
	}
	.t1 {
		background: linear-gradient(45deg, #ffd700, #ffec8b, #cfa300, #ffd700);
		background-clip: text;
		-webkit-background-clip: text;
		color: transparent;
		text-shadow: 2px 2px 4px rgba(255, 215, 0, 0.3);
		font-weight: bold;
	}
	.t2 {
		background: linear-gradient(45deg, #dcdcdc, #ffffff, #a9a9a9, #dcdcdc);
		background-clip: text;
		-webkit-background-clip: text;
		color: transparent;
		text-shadow: 2px 2px 4px rgba(192, 192, 192, 0.3);
		font-weight: bold;
	}
	@keyframes brillo {
		0% {
			background-position: 0% 50%;
		}
		100% {
			background-position: 100% 50%;
		}
	}
	.t1,
	.t2 {
		background-size: 200% 200%;
		animation: brillo 4s linear infinite;
	}
	.right {
		display: flex;
		align-items: center;
		position: relative;
	}
	.right img {
		width: 3.1rem;
		height: 3.2rem;
		margin: 0.5rem;
	}
	.users {
		background: none;
		border: none;
		cursor: pointer;
		padding: 0;
	}
	.user-menu {
		position: absolute;
		top: 100%;
		right: 0;
		background-color: #142130;
		border: 1px solid var(--border-color);
		border-radius: 8px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
		padding: 1rem;
		z-index: 400;
		width: 200px;
	}
	.user-info {
		margin-bottom: 1rem;
	}
	.user-info strong {
		display: block;
		color: white;
		font-size: 1.1rem;
	}
	.user-menu ul {
		list-style: none;
		padding: 0;
		margin: 0;
	}
	.user-menu ul li {
		padding: 0.5rem 0;
		color: white;
		cursor: pointer;
		display: flex;
		align-items: center;
		gap: 0.5rem;
		transition:
			transform 0.2s ease,
			color 0.2s ease;
	}
	.user-menu ul li:hover {
		color: var(--gold);
		transform: scale(1.05);
	}
	.icon-logout {
		width: 20px;
		height: 20px;
	}
	.modal-overlay {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background-color: rgb(163, 45, 45);
		display: flex;
		justify-content: center;
		align-items: center;
		z-index: 500;
	}
	.modal {
		background-color: var(--modal-background);
		padding: 2rem;
		color: white;
		border-radius: 12px;
		box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
		text-align: left;
		width: 90%;
		max-width: 500px;
	}
	.modal h2 {
		color: white;
		margin-bottom: 1.5rem;
		font-size: 1.5rem;
		text-align: center;
	}
	.modal input,
	.modal select {
		width: 100%;
		padding: 0.75rem;
		margin-bottom: 1rem;
		border: 1px solid var(--modal-border);
		border-radius: 6px;
		background-color: rgba(132, 131, 142, 0.651);
		color: white;
		font-size: 1rem;
	}
	.modal input::placeholder,
	.modal select::placeholder {
		color: #a9a9a9;
	}
	.modal-buttons {
		display: flex;
		justify-content: center;
		gap: 1rem;
		margin-top: 1.5rem;
	}
	.modal-buttons button {
		padding: 0.75rem 1.5rem;
		border: none;
		border-radius: 6px;
		cursor: pointer;
		font-size: 1rem;
		transition: background-color 0.3s ease;
	}
	.modal-buttons button:first-child {
		background-color: var(--green);
		color: white;
	}
	.modal-buttons button:first-child:hover {
		background-color: #09a809;
	}
	.modal-buttons button:last-child {
		background-color: var(--red);
		color: white;
	}
	.modal-buttons button:last-child:hover {
		background-color: #cc0000;
	}
	.sidebar {
		position: fixed;
		top: 60px;
		left: 0;
		width: 200px;
		height: calc(100% - 60px);
		background-color: #142130;
		border-right: 1px solid var(--border-color);
		transform: translateX(-100%);
		transition: transform 0.3s ease-in-out;
		z-index: 200;
		box-shadow: 2px 0 4px rgba(0, 0, 0, 0.1);
	}
	.sidebar.open {
		transform: translateX(0);
	}
	.sidebar ul {
		list-style: none;
		padding: 1rem;
	}
	.sidebar ul li {
		margin: 1rem 0;
	}
	.sidebar ul li a {
		text-decoration: none;
		color: white;
		font-size: 1.2rem;
		transition: color 0.3s ease;
	}
	.sidebar ul li a:hover {
		color: var(--gold);
	}
	.content {
		margin-top: 80px;
		padding: 1rem;
		max-width: 800px; /* Limita el ancho del contenido */
		margin-left: auto;
		margin-right: auto; /* Centra el contenido */
	}
	table {
		width: 100%;
		table-layout: auto;
		border-collapse: collapse;
		margin-bottom: 1rem; /* Menos separación entre tablas */
		background-color: #29333fe3;
		border-radius: 8px;
		overflow: hidden;
		box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
	}
	table th,
	table td {
		padding: 0.75rem;
		text-align: left;
		border-bottom: 1px solid var(--border-color);
	}
	table th {
		background-color: #1c2a3a;
		color: white;
		font-weight: bold;
	}
	table td {
		background-color: #142130;
		color: white;
	}
	/* botones modificar/ deshabilitar */
	table td .acciones {
		display: flex;
		gap: 0.2rem;
	}
	table td button {
		padding: 0.4rem 0.6rem;
		border: none;
		border-radius: 4px;
		cursor: pointer;
		font-size: 0.9rem;
		transition: background-color 0.3s ease;
	}
	table td button:first-child {
		background-color: var(--green);
		color: white;
		margin-right: 0.5rem;
	}
	table td button:first-child:hover {
		background-color: #09a809;
	}
	table td button:last-child {
		background-color: var(--red);
		color: white;
	}
	table td button:last-child:hover {
		background-color: #cc0000;
	}
	/* Responsive */
	@media (max-width: 768px) {
		.menu-container {
			width: 100%;
		}
		.brand .name {
			font-size: 14px;
		}
		.sidebar {
			width: 100%;
			top: 50px;
			height: calc(100% - 50px);
		}
		.user-menu {
			width: 100%;
			right: 0;
			left: 0;
			border-radius: 0;
			box-shadow: none;
		}
		.user-menu ul li {
			padding: 1rem 0;
		}
		.user-menu ul li button {
			width: 100%;
			text-align: left;
		}
		.modal {
			padding: 1.5rem;
		}
		.modal input,
		.modal select {
			padding: 0.5rem;
		}
		.modal-buttons button {
			padding: 0.5rem 1rem;
		}
		.content {
			padding: 0.5rem;
		}
		table {
			margin-bottom: 0.5rem; /* Menos separación en móviles */
		}
		label {
			font-style: var(--background-color);
		}
	}
	/* boton */
	.header-table {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 1rem;
	}
	.header-table h2 {
		font-size: 27px;
		font-family: Arial, Helvetica, sans-serif;
	}

	.btn-agregar {
		background-color: var(--green);
		color: white;
		border: none;
		padding: 0.5rem 1rem;
		border-radius: 6px;
		cursor: pointer;
		font-size: 1rem;
		transition: background-color 0.3s ease;
		display: flex;
		justify-content: end;
	}
	.btn-agregar-div {
		display: flex;
		justify-content: end;
	}

	.btn-agregar:hover {
		background-color: #09a809;
	}
	.modal-overlay {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background: rgba(0, 0, 0, 0.5);
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.modal {
		background: white;
		padding: 20px;
		border-radius: 8px;
		width: 300px;
	}

	.modal-buttons {
		display: flex;
		justify-content: space-between;
		margin-top: 20px;
	}

	.error {
		color: red;
		margin-bottom: 10px;
	}

	body {
		font-family: Arial;
	}
	.modal-overlay {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0.5);
		display: flex;
		justify-content: center;
		align-items: center;
		overflow-y: auto; /* Permite el desplazamiento vertical */
		padding: 20px; /* Espacio alrededor del modal */
	}
	/* fondo modal */
	.modal {
		background-color: var(--modal-color);
		padding: 20px;
		border-radius: 8px;
		width: 100%;
		max-width: 400px;
		max-height: 90vh; /* Limita la altura del modal */
		overflow-y: auto; /* Permite el desplazamiento dentro del modal */
	}

	.modal h2 {
		margin-bottom: 20px;
	}

	.modal-buttons {
		display: flex;
		gap: 10px;
		margin-top: 20px;
	}

	.modal-buttons button {
		flex: 1;
		padding: 10px;
		border: none;
		border-radius: 4px;
		cursor: pointer;
	}

	.modal-buttons button[type='submit'] {
		background-color: var(--green);
		color: white;
	}

	.modal-buttons button[type='submit']:hover {
		background-color: #019a03;
	}

	.modal-buttons button[type='button'] {
		background-color: #fa1414;
		color: rgb(255, 255, 255);
	}

	.modal-buttons button[type='button']:hover {
		background-color: #dc3535;
	}
</style>
