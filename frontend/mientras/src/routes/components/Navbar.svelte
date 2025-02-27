<div class="container">
    <div class="sidebar">
        <a href="/adminpanel"><img src="logo-image.png" alt="imagen" class="logo"></a>
        <nav>
            <ul>
                <button class="torneo" on:click={() => mostrarModalTorneo = true}>Torneo</button>
                <button class="equipos" on:click={() => mostrarModalEquipos = true}>Equipos</button>
                <button class="jugadores" on:click={() => mostrarModalJugadores = true}>Jugadores</button>
                <button class="grupos" on:click={() => mostrarModalGrupos = true}>Grupos</button>
            </ul>
        </nav>
        <button class="cerrar-btn" on:click={() => mostrarModal = true}>Salir</button>
    </div>
</div>
<div class="main-content">
    <h3>Lista de Torneos</h3>
    <div class="list-container">
        {#each torneos as torneo, index}
            <div class="list-item">
                <input type="text" bind:value={torneos[index]} readonly={!puedeModificarTorneo[index]}/>
                <button class="btn-modificar" on:click={() => modificarTorneo(index)}>Modificar</button>
                <button class="btn-eliminar" on:click={() => eliminarTorneo(index)}>Eliminar</button>
            </div>
        {/each}
    </div>

    <h3>Lista de Equipos</h3>
    <div class="list-container">
        {#each equipos as equipo, index}
            <div class="list-item">
                <input type="text" bind:value={equipos[index]} readonly={!puedeModificarEquipo[index]}/>
                <button class="btn-modificar" on:click={() => modificarTorneo(index)}>Modificar</button>
                <button class="btn-eliminar" on:click={() => eliminarEquipo(index)}>Eliminar</button>
            </div>
        {/each}
    </div>

    <h3>Lista de Jugadores</h3>
    <div class="list-container">
        {#each jugadores as jugador, index}
            <div class="list-item">
                <input type="text" bind:value={jugadores[index]} readonly={!puedeModificarJugador[index]} />
                <button class="btn-modificar" on:click={() => modificarTorneo(index)}>Modificar</button>
                <button class="btn-eliminar" on:click={() => eliminarJugador(index)}>Eliminar</button>
            </div>
        {/each}
    </div>

    <h3>Lista de Grupos</h3>
    <div class="list-container">
        {#each grupos as grupo, index}
            <div class="list-item">
                <input type="text" bind:value={grupos[index]} readonly={!puedeModificarGrupo[index]}/>
                <button class="btn-modificar" on:click={() => modificarTorneo(index)}>Modificar</button>
                <button class="btn-eliminar" on:click={() => eliminarGrupo(index)}>Eliminar</button>
            </div>
        {/each}
    </div>
</div>
{#if mostrarModal}
    <div class="modal">
        <div class="modal-content">
            <p>¿Estás seguro de que deseas salir?</p>
            <div class="modal-buttons">
                <button class="btn btn-yes" on:click={confirmarSalida}>Sí</button>
                <button class="btn btn-no" on:click={cerrarModal}>No</button>
            </div>
        </div>
    </div>
{/if}

{#if mostrarModalTorneo}
    <div class="modal-crud">
        <div class="modal-crud-container">
            <h3>Crear Torneo</h3>
            <input type="text" bind:value={nuevoTorneo} placeholder="Nombre del Torneo" />
            <button on:click={crearTorneo}>Crear</button>
            <button on:click={cerrarModalTorneo}>Cancelar</button>

            <h4>Lista de Torneos</h4>
            <ul>
                {#each torneos as torneo, index}
                    <li>{torneo} <button on:click={() => eliminarTorneo(index)}>Eliminar</button></li>
                {/each}
            </ul>
        </div>
    </div>
{/if}

{#if mostrarModalEquipos}
    <div class="modal-crud">
        <div class="modal-crud-container">
            <h3>Crear Equipo</h3>
            <input type="text" bind:value={nuevoEquipo} placeholder="Nombre del Equipo" />
            <button on:click={crearEquipo}>Crear</button>
            <button on:click={cerrarModalEquipos}>Cancelar</button>

            <h4>Lista de Equipos</h4>
            <ul>
                {#each equipos as equipo, index}
                    <li>{equipo} <button on:click={() => eliminarEquipo(index)}>Eliminar</button></li>
                {/each}
            </ul>
        </div>
    </div>
{/if}

{#if mostrarModalJugadores}
    <div class="modal-crud">
        <div class="modal-crud-container">
            <h3>Crear Jugador</h3>
            <input type="text" bind:value={nuevoJugador} placeholder="Nombre del Jugador" />
            <button on:click={crearJugador}>Crear</button>
            <button on:click={cerrarModalJugadores}>Cancelar</button>

            <h4>Lista de Jugadores</h4>
            <ul>
                {#each jugadores as jugador, index}
                    <li>{jugador} <button on:click={() => eliminarJugador(index)}>Eliminar</button></li>
                {/each}
            </ul>
        </div>
    </div>
{/if}

{#if mostrarModalGrupos}
    <div class="modal-crud">
        <div class="modal-crud-container">
            <h3>Crear Grupo</h3>
            <input type="text" bind:value={nuevoGrupo} placeholder="Nombre del Grupo" />
            <button on:click={crearGrupo}>Crear</button>
            <button on:click={cerrarModalGrupos}>Cancelar</button>

            <h4>Lista de Grupos</h4>
            
        </div>
    </div>
{/if}

<script>
    let mostrarModal = false;

    function cerrarModal() {
        mostrarModal = false;
    }

    function confirmarSalida() {
        window.location.href = "/"; 
    }

    let mostrarModalTorneo = false;
    let mostrarModalEquipos = false;
    let mostrarModalJugadores = false;
    let mostrarModalGrupos = false;

    let torneos = ['Torneo 1', 'Torneo 2'];
    let equipos = ['Equipo A', 'Equipo B'];
    let jugadores = ['Laura', 'Eduar'];
    let grupos = ['Grupo 1', 'Grupo 2'];

    let nuevoTorneo = '';
    let nuevoEquipo = '';
    let nuevoJugador = '';
    let nuevoGrupo = '';

    function crearTorneo() {
        if (nuevoTorneo) {
            torneos.push(nuevoTorneo);
            nuevoTorneo = '';
            mostrarModalTorneo = false;
        }
    }
    function crearEquipo() {
        if (nuevoEquipo) {
            equipos.push(nuevoEquipo);
            nuevoEquipo = ''; 
            mostrarModalEquipos = false;
        }
    }
    function crearJugador() {
        if (nuevoJugador) {
            jugadores.push(nuevoJugador);
            nuevoJugador = '';
            mostrarModalJugadores = false;
        }
    }

    function crearGrupo() {
        if (nuevoGrupo) {
            grupos.push(nuevoGrupo);
            nuevoGrupo = '';
            mostrarModalGrupos = false;
        }
    }
    let puedeModificarTorneo = Array(torneos.length).fill(false);
    let puedeModificarEquipo = Array(equipos.length).fill(false);
    let puedeModificarJugador = Array(jugadores.length).fill(false);
    let puedeModificarGrupo = Array(grupos.length).fill(false);

    function modificarTorneo(index) {
        puedeModificarTorneo[index] = true;
    }

    function modificarEquipo(index) {
        puedeModificarEquipo[index] = true;
    }
    function modificarJugador(index) {
        puedeModificarJugador[index] = true;
    }
    function modificarGrupo(index) {
        puedeModificarGrupo[index] = true;
    }

    function eliminarTorneo(index) {
        torneos.splice(index, 1);
    }
    function eliminarEquipo(index) {
        equipos.splice(index, 1);
    }
    function eliminarJugador(index) {
        jugadores.splice(index, 1);
    }
    function eliminarGrupo(index) {
        grupos.splice(index, 1);
    }
    function cerrarModalTorneo() {
        mostrarModalTorneo = false;
    }
    function cerrarModalEquipos() {
        mostrarModalEquipos = false;
    }
    function cerrarModalJugadores() {
        mostrarModalJugadores = false;
    }
    function cerrarModalGrupos() {
        mostrarModalGrupos = false;
    }
</script>
<style>

.btn-modificar {
    background-color: #3498db; 
    color: white;
    padding: 5px 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.btn-modificar:hover {
    background-color: #2980b9;
}
.btn-eliminar {
    color: white;
    padding: 5px 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    background-color: #c0392b;
    translate: -29px;
}

.btn-eliminar:hover {
    background-color: #920202;
}

.main-content {
    margin-left: 180px;
    padding: 20px;
    margin-top: 0;
    background: linear-gradient(180deg,#ffffff, #ffffff)
}

.list-container {
    margin-top: 0;
}

.list-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 5px 0;
}

.list-item input {
    width: 75%;
    padding: 8px;
    border-radius: 5px;
    border: 1px solid #ccc;
}
.modal-crud {
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
.modal-crud-container {
    background: white;
    padding: 20px;
    border-radius: 10px;
    width: 300px;
    text-align: center;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.modal-crud-container input {
    width: 90%;
    padding: 8px;
    margin-bottom: 10px;
    border-radius: 10px;
    border-color: #36d531;
}

.modal-crud-container button {
    translate: 4px;
    padding: 10px 20px;
    margin: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.modal-crud-container button:hover {
    background-color: #cc1c1c;
    color: white;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px 0;
}

button {
    background-color: #dc3545;
    color: white;
    padding: 5px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #c82333;
}

.modal {
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
.modal-content {
    background: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    translate: 90px;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 20px;
}
.modal-buttons {
    display: flex;
    justify-content: space-around;
    margin-top: 15px;
}
.btn {
    padding: 13px 29px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    
}
.btn-yes {
    background-color: #d9534f;
    color: white;
}
.btn-yes:hover {
    background-color: #c9302c;
}
.btn-no {
    background-color: #5bc0de;
    color: white;
}
.btn-no:hover {
    background-color: #31b0d5;
}
.container {
    background: #f9f9f9;
/*     min-height: 100vh;  */
    flex-direction: column;
}
.sidebar {
    width: 150px;
    height: 100vh;
    background-color:rgb(7, 3, 15);
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    position: fixed;
    left: 0;
    top: 0;
}
a .logo {
    width: 70%;
    translate: 23px -10px;
}
ul {
    margin: 0;
    font-family: Arial, sans-serif;
    list-style: none;
    padding: 0;
    width: 100%;
    text-align: center;
}
ul button {
    margin: 19px 0;
    text-decoration: none;
    color:rgb(255, 255, 255);
    background-color: rgb(7, 3, 15);
    font-size: 1.2rem;
    display: block;
    padding: 10px;
    transition: 0.3s;
    text-align: left;
    border: 0;
}
ul button:hover {
    background-color:rgb(22, 2, 54);
    border-radius: 5px;
    border: 0;
}
.cerrar-btn {
    margin-top: auto;
    background-color: rgb(94, 1, 1);
    text-decoration: none;
    padding: 10px 20px;
    border-radius: 5px;
    font-weight: bold;
    transition: 0.3s;
    translate: 0 -30px;
    color: aliceblue;
    border: none; 
}
.cerrar-btn:hover {
    background-color: rgb(73, 9, 9);
}
</style>
