<script>
    let name = '';
    let email = '';
    let password = '';
    let confirmPassword = '';
    let errorMessage = '';

    const handleRegister = () => {
        if (password !== confirmPassword) {
            errorMessage = 'Las contraseñas no coinciden';
            console.log(errorMessage);
        } else {
            errorMessage = '';
            console.log('Nombre:', name);
            console.log('Email:', email);
            console.log('Contraseña:', password);
        }
    };
</script>
  <!-- #9b0127ee -->
<style>
    .register-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #042408ee;
        background-image: url('/register-fondo.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-image: url('/register-fondo.png');
        background-size: 50%;
        background-position: -1%;
        background-repeat: no-repeat;
    }

    .register-form {
        background: white;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 9px 10px rgba(0, 0, 0, 0.1);
        width: 70%;
        max-width: 370px;
        translate: 350px;
    }

    .register-form h2 {
        margin-bottom: 1.8rem;
        font-size: 2.0rem;
        translate: 87px;
        color: #000000;
    }

    .form-group {
        margin-bottom: 1.3rem;
    }

    .form-group label {
        display: block;
        margin-bottom: 0.5rem;
        font-weight: bold;
        color: #555;
    }

    .form-group input {
        width: 95.3%;
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 1rem;
    }

    .form-group input:focus {
        outline: none;
        border-color: #ccbb1e;
    }

    .register-button {
        width: 100%;
        padding: 0.75rem;
        background-color: #059b19;
        color: white;
        border: none;
        border-radius: 4px;
        font-size: 1.3rem;
        cursor: pointer;
    }

    .register-button:hover {
        background-color: #048417;
    }

    .login-link {
        display: flex;
        align-items: center;
        gap: 90px;
        margin-top: 1.8rem;
    }

    .login-link p {
        margin: 0;
    }

    .login-link a {
        color: #0f81b6;
        text-decoration: none;
        font-weight: bold;
    }

    .login-link a:hover {
        text-decoration: underline;
        font-size: 17px;
    }
</style>

<div class="register-container">
    <div class="register-form">
        <h2>Crea tu cuenta</h2>
        <div class="form-group">
            <label for="name">Nombre</label>
            <input type="text" id="name" bind:value={name} placeholder="Ingresa tu nombre" required />
        </div>
        <div class="form-group">
            <label for="email">Correo Electrónico</label>
            <input type="email" id="email" bind:value={email} placeholder="Ingresa tu correo electrónico" required />
        </div>
        <div class="form-group">
            <label for="password">Contraseña</label>
            <input type="password" id="password" bind:value={password} placeholder="Ingresa tu contraseña" required />
        </div>
        <div class="form-group">
            <label for="confirmPassword">Confirmar Contraseña</label>
            <input type="password" id="confirmPassword" bind:value={confirmPassword} placeholder="Repite tu contraseña" required />
        </div>
        <button class="register-button" on:click={handleRegister}>Registrarse</button>
        <div class="login-link">
            <p>¿Ya tienes una cuenta?</p>
            <b><a href="/login">Inicia sesión aquí</a></b>
        </div>
    </div>
</div>
