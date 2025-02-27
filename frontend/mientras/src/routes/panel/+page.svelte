<script>
	import { onMount } from 'svelte';
	let tablaVisible = 'home';

	export let data;
	let {torneos} = data;
	
	let showEquipoModal = false; // Estado del modal
	
	// Datos del formulario
	let nombreEquipo = '';
	let delegado = '';
	let telefonoDelegado = '';
	let statusId = '';

	function abrirModalAgregar() {
		showEquipoModal = true;
	}

	function closeEquipoModal() {
		showEquipoModal = false;
		limpiarFormulario();
	}

	function limpiarFormulario() {
		nombreEquipo = '';
		delegado = '';
		telefonoDelegado = '';
		statusId = '';
	}

	let isMenuOpen = false;
	let isUserMenuOpen = false;
	let showLogoutModal = false;

	// Estados para los modales de agregar
	let showTorneoModal = false;
	let showJugadorModal = false;
	let showGrupoModal = false;

	function toggleMenu() {
		isMenuOpen = !isMenuOpen;
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

	// Funciones para abrir modales
	// @ts-ignore
	function openTorneoModal() {
		showTorneoModal = true;
	}

	// @ts-ignore
	function openEquipoModal() {
		showEquipoModal = true;
	}

	// @ts-ignore
	function openJugadorModal() {
		showJugadorModal = true;
	}

	// @ts-ignore
	function openGrupoModal() {
		showGrupoModal = true;
	}

	// Funciones para cerrar modales
	function closeTorneoModal() {
		showTorneoModal = false;
	}

	function closeJugadorModal() {
		showJugadorModal = false;
	}

	function closeGrupoModal() {
		showGrupoModal = false;
	}

	// Funciones para mostrar la tabla correspondiente

	function mostrarHome() {
		tablaVisible = 'home';
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
	/*
	function abrirModalAgregar() {
		if (tablaVisible === 'torneos') {
			openTorneoModal();
		} else if (tablaVisible === 'equipos') {
			openEquipoModal();
		} else if (tablaVisible === 'jugadores') {
			openJugadorModal();
		} else if (tablaVisible === 'grupos') {
			openGrupoModal();
		}
	}*/
</script>

<header>
	<div class="left">
		<div class="menu-container">
			<!-- svelte-ignore a11y_consider_explicit_label -->
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

<div class="sidebar {isMenuOpen ? 'open' : ''}">
	<ul>
		<li><a href="#" on:click={mostrarHome}>Home</a></li>
		<!-- Nueva opción -->
		<li><a href="#" on:click={mostrarTorneos}>Torneo</a></li>
		<li><a href="#" on:click={mostrarEquipos}>Equipos</a></li>
		<li><a href="#" on:click={mostrarJugadores}>Jugadores</a></li>
		<li><a href="#" on:click={mostrarGrupos}>Grupos</a></li>
	</ul>
</div>

<!-- Modal para Agregar Torneo -->
{#if showTorneoModal}
	<div class="modal-overlay">
		<div class="modal">
			<h2>Agregar Torneo</h2>
			<input type="text" placeholder="Nombre del Torneo" />

			<!-- Label y campo para Fecha de Inicio -->
			<label
				for="fechaInicio"
				style="color: white; text-align: left; display: block; margin-bottom: 0.5rem;"
				>Fecha de Inicio</label
			>
			<input type="date" id="fechaInicio" />

			<!-- Label y campo para Fecha de Fin -->
			<label
				for="fechaFin"
				style="color: white; text-align: left; display: block; margin-bottom: 0.5rem;"
				>Fecha de Fin</label
			>
			<input type="date" id="fechaFin" />

			<input type="text" placeholder="Ubicación"  />
			<div class="modal-buttons">
				<button >Agregar</button>
				<button on:click={closeTorneoModal}>Cancelar</button>
			</div>
		</div>
	</div>
{/if}

<!-- MODAL -->
{#if showEquipoModal}
	<div class="modal-overlay">
		<div class="modal">
			<h2>Agregar Equipo</h2>
			<input type="text" bind:value={nombreEquipo} placeholder="Nombre del Equipo" />
			<input type="text" bind:value={delegado} placeholder="Nombre del Delegado" />
			<input type="tel" bind:value={telefonoDelegado} placeholder="Teléfono del Delegado" />
			<select bind:value={statusId}>
				<option value="">Selecciona un estado</option>
				{#each status as s}
					<option value={s.id}>{s.nombre}</option>
				{/each}
			</select>
			<div class="modal-buttons">
				<button on:click={agregarEquipo}>Agregar</button>
				<button on:click={closeEquipoModal}>Cancelar</button>
			</div>
		</div>
	</div>
{/if}

<!-- Modal para Agregar Jugador -->
{#if showJugadorModal}
	<div class="modal-overlay">
		<div class="modal">
			<h2>{modoEdicion ? 'Editar' : 'Agregar'}</h2>
			<!-- <input type="text" placeholder="Cédula" bind:value={cedula} /> -->
			<input type="text" placeholder="Nombre" bind:value={nombre} />
			<input type="text" placeholder="Apellido" bind:value={apellido} />
			<input type="date" placeholder="Fecha de Nacimiento" bind:value={fechaNacimiento} />
			<input type="email" placeholder="Correo" bind:value={correo} />
			<input type="text" placeholder="Género" bind:value={genero} />
			<select bind:value={equipoId}>
				<option value="">Selecciona un equipo</option>
				{#each equipos as equipo}
					<option value={equipo.id}>{equipo.nombre}</option>
				{/each}
			</select>
			<input type="text" placeholder="Posición" bind:value={posicion} />

			<!-- Campo para subir imagen (opcional) -->
			<label
				for="imagenJugador"
				style="color: white; text-align: left; display: block; margin-bottom: 0.5rem;"
				>Imagen del Jugador (opcional)</label
			>
			<input type="file" id="imagenJugador" bind:files={imagenJugador} accept="image/*" />

			<div class="modal-buttons">
				<button on:click={guardarJugador}>{modoEdicion ? 'Modificar' : 'Agregar'}</button>
				<button on:click={closeJugadorModal}>Cancelar</button>
			</div>
		</div>
	</div>
{/if}

<!-- Modal para Agregar Grupo -->
{#if showGrupoModal}
	<div class="modal-overlay">
		<div class="modal">
			<h2>Agregar Grupo</h2>
			<input type="text" placeholder="Nombre del Grupo" />
			<select>
				<option value="">Selecciona el Equipo 1</option>
				{#each equipos as equipo}
					<option value={equipo.id}>{equipo.nombre}</option>
				{/each}
			</select>
			<select>
				<option value="">Selecciona el Equipo 2</option>
				{#each equipos as equipo}
					<option value={equipo.id}>{equipo.nombre}</option>
				{/each}
			</select>
			<input type="date" placeholder="Fecha del Enfrentamiento" />
			<div class="modal-buttons">
				<button on:click={closeGrupoModal}>Agregar</button>
				<button on:click={closeGrupoModal}>Cancelar</button>
			</div>
		</div>
	</div>
{/if}

<!-- Modal de confirmación para salir -->
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

<!-- Tablas -->
<div class="content">
	{#if tablaVisible === 'home'}
		<div class="home">
			<div class="logo-home"><img src="logo-image.png" alt="logo-empresa" /></div>
			<h1>Bienvenido al Panel de Administración</h1>
			<p>Selecciona una opción del menú para comenzar.</p>
		</div>
	{/if}

	<!-- Tablas -->
	{#if tablaVisible === 'torneos'}
		<h1>Lista de torneos</h1>
		<table>
			<thead>
				<tr>
					<th>ID</th>
					<th>Nombre</th>
					<th>Fecha Inicio</th>
					<th>Fecha Fin</th>
					<th>Ubicación</th>
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
						<td>
							<button>Modificar</button>
							<button>Deshabilitar</button>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
		<div class="btn-agregar-div">
			<button class="btn-agregar" on:click={abrirModalAgregarJugador}>Nuevo +</button>
		</div>
	{/if}

	<!-- TABLA DE EQUIPOS -->
	{#if tablaVisible === 'equipos'}
		<h1>Lista de Equipos</h1>
		<table>
			<thead>
				<tr>
					<th>ID</th>
					<th>Nombre</th>
					<th>Delegado</th>
					<th>Teléfono</th>
					<th>Status</th>
					<th>Acciones</th>
				</tr>
			</thead>
			<tbody>
				{#each equipos as equipo}
					<tr>
						<td>{equipo.id}</td>
						<td>{equipo.nombre}</td>
						<td>{equipo.delegado_equipo}</td>
						<td>{equipo.telefono}</td>
						<td>{equipo.status_nombre}</td>
						<td>
							<button>Modificar</button>
							<button>Deshabilitar</button>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>

		<div class="btn-agregar-div">
			<button class="btn-agregar" on:click={abrirModalAgregar}>Nuevo +</button>
		</div>
	{/if}

	{#if tablaVisible === 'jugadores'}
		<h1>Lista de Jugadores</h1>
		<table>
			<thead>
				<tr>
					<th>Nro. Cedula</th>
					<th>Nombre</th>
					<th>Apellido</th>
					<th>Fecha de Nacimiento</th>
					<th>Correo</th>
					<th>Genero</th>
					<th>Acciones</th>
				</tr>
			</thead>
			<tbody>
				{#each jugadores as jugador}
					<tr>
						<td>{jugador.cedula}</td>
						<td>{jugador.nombre}</td>
						<td>{jugador.apellido}</td>
						<td>{jugador.fecha_nacimiento}</td>
						<td>{jugador.correo}</td>
						<td>{jugador.genero}</td>
						<td>
							<button>Modificar</button>
							<button>Deshabilitar</button>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
		<div class="btn-agregar-div">
			<button class="btn-agregar" on:click={abrirModalAgregar}>Nuevo +</button>
		</div>
	{/if}

	{#if tablaVisible === 'grupos'}
		<h1>Lista de Grupos</h1>
		<table>
			<thead>
				<tr>
					<th>ID</th>
					<th>Nombre</th>
					<th>Fecha Inicio</th>
					<th>Fecha Final</th>
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
							<button>Modificar</button>
							<button>Deshabilitar</button>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
		<div class="btn-agregar-div">
			<button class="btn-agregar" on:click={abrirModalAgregar}>Nuevo +</button>
		</div>
	{/if}
</div>

<style>
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
		background-color: rgba(0, 0, 0, 0.5);
		display: flex;
		justify-content: center;
		align-items: center;
		z-index: 500;
	}
	.modal {
		background-color: var(--modal-background);
		padding: 2rem;
		border-radius: 12px;
		box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
		text-align: center;
		width: 90%;
		max-width: 500px;
	}
	.modal h2 {
		color: white;
		margin-bottom: 1.5rem;
		font-size: 1.5rem;
	}
	.modal input,
	.modal select {
		width: 100%;
		padding: 0.75rem;
		margin-bottom: 1rem;
		border: 1px solid var(--modal-border);
		border-radius: 6px;
		background-color: #2c3e50;
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
		border-collapse: collapse;
		margin-bottom: 1rem; /* Menos separación entre tablas */
		background-color: #142130;
		border-radius: 8px;
		overflow: hidden;
		box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
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
	table td button {
		padding: 0.5rem 1rem;
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
</style>
