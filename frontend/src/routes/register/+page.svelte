<script lang="ts">
    import { enhance } from '$app/forms';
    //import { invalid, redirect } from '@sveltejs/kit';
    //import { page } from '$app/stores';

    let name = '';
    let email = '';
    let password = '';
    let confirmPassword = '';
    let errorMessage = '';

    const handleSubmit = async (event: SubmitEvent) => {
        event.preventDefault();

        if (password !== confirmPassword) {
            errorMessage = 'Las contraseñas no coinciden';
            return;
        }

        const formData = new FormData(event.target as HTMLFormElement);
        const response = await fetch('/register', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            // Redirige al usuario después del registro exitoso
            window.location.href = '/login';
        } else {
            const result = await response.json();
            errorMessage = result.message || 'Error en el registro';
        }
    };
</script>
<main>
    {#if errorMessage}
        <div class="error-message">{errorMessage}</div>
    {/if}
    <div class="register-container">
        <div class="register-form">
            <h2>Crea tu cuenta</h2>
            <form on:submit|preventDefault={handleSubmit} use:enhance>
                <div class="form-group">
                    <label for="name">Nombre</label>
                    <input type="text" id="name" name="name" bind:value={name} required />
                </div>
                <div class="form-group">
                    <label for="email">Correo Electrónico</label>
                    <input type="email" id="email" name="email" bind:value={email} required />
                </div>
                <div class="form-group">
                    <label for="password">Contraseña</label>
                    <input type="password" id="password" name="password" bind:value={password} required />
                </div>
                <div class="form-group">
                    <label for="confirmPassword">Confirmar Contraseña</label>
                    <input type="password" id="confirmPassword" name="confirmPassword" bind:value={confirmPassword} required />
                </div>
                {#if errorMessage}
                    <div class="error-message">{errorMessage}</div>
                {/if}
                <button type="submit">Registrarse</button>
            </form>
        </div>
    </div>
</main>
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

