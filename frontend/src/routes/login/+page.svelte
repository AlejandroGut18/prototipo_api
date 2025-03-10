<script>
  import { PUBLIC_API_URL } from '$env/static/public';
    let email = "";
    let password = "";
    let error = "";
    /**
	 * @type {any[]}
	 */
    let usuarios = []; // Variable para almacenar los usuarios
  
    // Función para obtener los usuarios desde el backend
    async function obtenerUsuarios() {
      try {
        const response = await fetch(`${PUBLIC_API_URL}/api/usuarios/`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });
  
        if (response.ok) {
          usuarios = await response.json(); // Guarda los usuarios en la variable
        } else {
          error = "Error al obtener los usuarios";
          usuarios = []; // Asegúrate de que usuarios sea un array vacío
        }
      } catch (err) {
        error = "Error al conectar con el servidor";
        usuarios = []; // Asegúrate de que usuarios sea un array vacío
      }
    }
  
    // Función para manejar el login
    function handleLogin() {
      if (usuarios.length === 0) {
        error = "No se pudieron cargar los usuarios. Intenta de nuevo más tarde.";
        return;
      }
  
      // Busca el usuario en la lista
      const usuario = usuarios.find(
        (u) => u.correo === email && u.password === password
      );
  
      if (usuario) {
        // Si las credenciales son válidas, redirige al panel administrativo
        window.location.href = "/panel/";
      } else {
        error = "Credenciales inválidas";
      }
    }
  
    // Obtén los usuarios cuando el componente se monte
    obtenerUsuarios();
  </script>
  
  <div class="login-container">
    <div class="login-form">
      <div class="card">
        <img src="logo-image.png" alt="logo-imagen" />
        <h2>Iniciar Sesión</h2>
      </div>
  
      <div class="form-group">
        <form on:submit|preventDefault={handleLogin}>
          <label for="email">Correo Electrónico</label>
          <input
            type="email"
            id="email"
            bind:value={email}
            placeholder="Ingresa tu correo"
            required
          /><br /><br />
  
          <label for="password">Contraseña</label>
          <input
            type="password"
            id="password"
            bind:value={password}
            placeholder="Ingresa tu contraseña"
            required
          /><br /><br />
  
          <button class="login-button" type="submit">Iniciar Sesión</button>
        </form>
      </div>
  
      {#if error}
        <br />
        <p style="color: red;">{error}</p>
      {/if}
  
      <div class="register-link">
        <p>¿No es miembro de Copa Campeones?</p>
      </div>
      <b><a href="/register">Regístrese aquí</a></b>
    </div>
  </div>

<style>
  /* Ajusta la imagen dentro de la caja de login */
.login-container img {
    width: 100px;
    max-width: 100%; /* Para evitar que la imagen se estire más de lo necesario */
    height: auto;
    translate: 50%;
}
.login-button a{
    text-decoration: none;
    color:#ccc
}

/* Ajuste de la tarjeta de login */
.login-container .card {
    overflow: hidden;
    position: relative;
    width: 90%; /* Ajuste porcentual para más flexibilidad */
    max-width: 400px; /* Limitar el ancho máximo */
    margin: 0 auto; /* Centra la tarjeta */
    padding: 8px 10px 0px 60px;
    translate: -12% -32px;
    border-radius: 8px;
    box-sizing: border-box;
}

/* Media query para pantallas más grandes */
@media (min-width: 500px) {
    .card {
        width: 360px; /* Fijo para pantallas más grandes */
        margin: 0 auto; /* Centrado */
    }
}

/* Ajuste visual de la pseudo-clase :before */
.card::before {
    content: "";
    top: -880px;
    left: 50%;
    translate: -50% 0;
    width: 1000px;
    height: 1000px;
    border-radius: 50%;
    background: #090616c4;
}

/* Ajustes adicionales para pantallas pequeñas */
@media (max-width: 500px) {
    .login-container img {
        width: 50%; /* Asegura que la imagen se ajuste en pantallas pequeñas */
    }

    .card {
        padding: 10px 20px; /* Reduce el padding en pantallas pequeñas */
    }
}

   /* Contenedor principal */
.login-container {
    display: flex;
    align-items: center;
    height: 100vh;
    background-color: #f0f2f5;
    background-image: url('/login-fondo.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    padding: 0 100px; /* Agrega algo de espacio lateral en pantallas pequeñas */
}

/* Formulario de login */
.login-form {
    background: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: -9px 10px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 370px; /* Limita el tamaño máximo */
    box-sizing: border-box; /* Asegura que el padding no afecte al tamaño */
    translate: none; /* Evita el desplazamiento innecesario */
}

/* Título del formulario */
.login-form h2 {
    font-size: 2.0rem;
    color: #000000;
    text-align: center; /* Centra el título */
}


/* Grupo de campos */
.form-group {
    margin-bottom: 1.3rem;
}

/* Etiqueta de los campos */
.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
    color: #555;
}

/* Campos de entrada */
.form-group input {
    width: 100%; /* Cambiado de 95.3% a 100% para que ocupe todo el ancho */
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 10px;
    font-size: 1rem;
    box-sizing: border-box; /* Para que el padding no afecte el tamaño */
}

/* Estilo al hacer foco en los campos */
.form-group input:focus {
    outline: none;
    border-color: #d4c00a;
}

/* Media query para pantallas más pequeñas */
@media (max-width: 500px) {
    .login-form {
        padding: 1.5rem; /* Reduce el padding en pantallas pequeñas */
    }
    .login-container {
        padding: 0 10px; /* Reduce el padding lateral */
    }
    .login-form h2 {
        font-size: 1.8rem; /* Reduce el tamaño del título en pantallas pequeñas */
    }
}

  
    /* Botón de login */
.login-button {
    width: 100%;
    padding: 0.75rem;
    background-color: #e2d515;
    color: rgb(57, 55, 55);
    border: none;
    border-radius: 10px;
    font-size: 1.3rem;
    cursor: pointer;
    transition: transform 0.3s ease, background-color 0.3s ease; /* Transición suave */
  }

/* Hover del botón de login */
.login-button:hover {
    background-color: #d7cb26;
    transform: scale(1.05);
}

/* Indicadores de estado */
.indicator {
    display: flex;
    justify-content: center; /* Centra los puntos */
    margin-top: 10px;
}

.dot {
    height: 10px;
    width: 10px;
    border-radius: 50%;
    margin: 0 5px;
    background-color: #ccc;
}

#red-dot {
    background-color: red;
}

#orange-dot {
    background-color: orange;
}

#green-dot {
    background-color: green;
}

/* Estilo de párrafos */
p {
    color: #555;
    font-size: 1rem; /* Asegura que el texto no sea demasiado grande */
}

/* Enlace de registro */
.register-link {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: 1rem;
    justify-content: center; /* Centra el contenido en pantallas grandes */
}

.register-link p {
    margin: 0;
    font-size: 1rem; /* Ajuste de tamaño para pantallas pequeñas */
}

b {
    display: flex;
    justify-content: center;
    color: #059b19;
    text-decoration: none;
    font-weight: bold;
    font-size: 1.1rem; /* Ajuste para que sea legible en pantallas pequeñas */
}

/* Hover en el enlace de registro */
b:hover {
    text-decoration: underline;
}

/* Media query para pantallas pequeñas */
@media (max-width: 500px) {
    .login-button {
        font-size: 1.1rem; /* Reduce el tamaño del texto en el botón */
        padding: 0.6rem; /* Reduce el padding en pantallas pequeñas */
    }

    .indicator {
        margin-top: 8px; /* Reduce el margen en pantallas pequeñas */
    }

    .register-link {
        margin-top: 0.8rem;
        font-size: 1rem; /* Ajuste para pantallas más pequeñas */
    }

    .register-link a {
        font-size: 1rem; /* Ajuste el tamaño del enlace */
    }
}

</style>