<header class="header">
    <img class="logo" src="logo-image.png" alt="">
    <div class="letra">
       <h2 class="t1">Copa de</h2>
       <h2 class="t2">Campeones</h2>
    </div>
    <!-- 
    SI SE PUEDEEEEEEEEEEE animos
    -->
    <nav class="navBar">
        <ul class="cont-ul">
            <li><a href="#home">HOME</a></li>
            <li class="despliegue">
                <a href="#equipo">Equipo ▼</a>
                <ul class="ul-second">
                    <li><a href="#his">Historia</a></li>
                    <li><a href="#dic">Directiva</a></li>
                    <li><a href="#per">Personal</a></li>
                </ul>
            </li>
            <li><a href="#nstrs">Nosotros</a></li>
            <li><a href="#ps">Posiciones</a></li>
            <li class="despliegue">
                <a href="#est">Estadistica ▼</a>
                <ul class="ul-second">
                    <li><a href="#arrimes">Arrimes</a></li>
                    <li><a href="#boche">Boche</a></li>
                    <li><a href="#rastreros">Rastreros</a></li>
                </ul>
            </li>
            <li class="despliegue">
                <a href="/contactar">Contactanos</a>
                <ul class="submenu">
                    <li><img src="qr.png" alt="Código QR de contacto"></li>
                </ul>
            </li>
        </ul>
    </nav>
    <div class="login">
        <button class="btn"><a href="/login"><b>Iniciar Sesion</b></a></button>
        <button class="btn2"><a href="/register"><b>Registrarte</b></a></button>
    </div>
</header>

<!--     <div class="info-section">
            <div class="info-box-o" id="equipo">
                <h2>Equipos Participantes</h2>
                <p>Conoce a los equipos que compiten en esta edición.</p>
            </div>
    </div> -->
<div class="container">            
    <div class="info-box" id="his">
        <div>
            <h3>Historia</h3>
            <p>La Organización Copa de Campeones, fundada en 2010 en Valencia, Estado Carabobo, se ha consolidado como un promotor clave del deporte de las Bolas Criollas. Dirigida por la Dra. Haydee Guillermina Páez como presidente y el Prof. Hugo Ferrini como vicepresidente, esta institución ha logrado unir diversos sectores de la sociedad valenciana, incluidos colegios profesionales, gremios institucionales y entes gubernamentales, posicionándose como referente en la promoción y desarrollo de este deporte tradicional.</p>
        </div>
    </div>   
    <div class="info-box" id="his">     
        <div>
            <h3>Vision</h3>
            <p>Ser, además de un medio de esparcimiento, un código ético de vida, en el que el compañerismo, la fraternidad, el compromiso, la responsabilidad, la solidaridad, la honestidad y el respeto primen en el transcurrir de cada encuentro deportivo, como valores superiores del atleta practicante de la disciplina Bolas Criollas, en representación de los clubes sociales, colegios profesionales y gremios colegiados afiliados.</p>
        </div>
    </div>
    <div class="info-box" id="his">
        <div>
            <h3>Mision</h3>
            <p>Apoyar el desarrollo de la práctica deportiva de la disciplina Bolas Criollas en los clubes sociales, colegios profesionales y gremios colegiados afiliados, para afianzar una convivencia social armónica y sinérgica, orientada a fortalecer los valores éticos y morales propios de una comunidad sana, saludable e integral, en pro del mejoramiento de la calidad de vida física y espiritual de sus integrantes.</p>
        </div>
    </div>
<div class="container-direc">
    

</div>
</div>
    <div class="info-box-imagen">
        <h3>Nosotros</h3>
        <p>Mira las mejores fotos de los partidos y eventos.</p>
        <div class="image-gallery">
            <img src="cbb.jpg" alt="imagen">
            <img src="cc.jpg" alt="imagen">
            <img src="ccbb.jpg" alt="imagen">
            <img src="galery.jpg" alt="imagen">
        </div>
    </div><br>

<div class="cp">
    Copyright © Copa de Campeones 2024-2025
</div>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap');
    
.container {
    display: flex;
    justify-content: space-between;
    gap: 30px;
    max-width: 1200px;
    width: 90%;  /* Permite que la página se ajuste mejor en diferentes tamaños */
    margin: auto;
    flex-wrap: wrap;
    padding: 10px;
}


.info-box {
    flex: 1 1 30%; 
    min-width: 250px; 
    max-width: 370px; 
    background: #f8f9fa; 
    border-left: 6px solid #09052e; 
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    padding: 20px;
    text-align: justify;
    margin: 30px 0; 
}

.info-box h3 {
    font-size: 26px;
    color: #44607e; 
    margin-bottom: 10px;
}

.info-box p {
    font-size: 15px;
    color: #333;
    line-height: 1.6;
}


.info-box-imagen {
    text-align: center;
    background: #e4eaf0;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    max-width: 1500px; 
    margin: 0 auto; 
}

.info-box-imagen h3 {
    font-size: 24px;
    color: #333;
    margin-bottom: 10px;
    margin: 0 20px;
}

.info-box-imagen p {
    font-size: 16px;
    color: #666;
    margin-bottom: 20px;
}

.image-gallery {
    display: flex;
    justify-content: center; 
    gap: 10px; 
    overflow-x: auto; 
    padding-bottom: 20px;
}

.image-gallery img {
    width: 250px; 
    height: auto;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
    transition: transform 0.3s ease-in-out;
}

.image-gallery img:hover {
    transform: scale(1.05); 
}
.navBar {
    width: 100%;
    background-color: #142130;
    padding: 10px;
}

.navBar ul {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    justify-content: space-between; /* Espaciado entre elementos */
    align-items: center;
    flex-wrap: wrap; /* Permite que los elementos se acomoden */
}

.navBar ul li {
    position: relative;
}

.navBar ul li a {
    text-decoration: none;
    color: white;
    padding: 10px;
    display: block;
}

/* Estilos para submenu */
.navBar ul li .submenu {
    display: none; 
    position: absolute;
    top: 100%;
    left: 0;
    background-color: #142130;
    padding: 5px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.navBar ul li:hover .submenu {
    display: block;
}

/* 🔹 Ajustar en pantallas pequeñas */
@media (max-width: 768px) {
    .navBar ul {
        flex-direction: column; /* Apilar elementos en columnas */
        align-items: flex-start;
    }

    .navBar ul li {
        width: 100%;
        text-align: left;
    }

    .navBar ul li a {
        padding: 15px;
        display: block;
        width: 100%;
    }

    .navBar ul li .submenu {
        position: relative;
        width: 100%;
    }

    .navBar ul li .submenu img {
        width: 100%; /* Ajustar imagen al ancho del contenedor */
    }
}

.cp {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    text-align: center;
    padding: 2vh 5vw; /* Usa unidades relativas para padding */
    background-color: #0d151f;
    border-style: ridge;
    border-color: #d4b505;
    color: white;
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
    0% { background-position: 0% 50%; }
    100% { background-position: 100% 50%; }
}

.t1, .t2 {
    background-size: 200% 200%;
    animation: brillo 2s linear infinite;
    font-size: 30px;
}

:root {
    --navbar-color: #0d151f; 
    --white: #ffffff; 
    --button: #f5e44d; 
    --icon-bg: #f8ec7e; 
    --hover-color: #77e858; 
}
.logo{
    width: 12vw
}
.login a{
    text-decoration: none;
    color: #000000;
    font-size: 17px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Lato', sans-serif;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 110px;
    width: 100%;
    padding: 0 0.3rem;
    background-color: var(--navbar-color);
    color: var(--white);
}

.navBar ul {
    list-style: none;
    display: flex;
    align-items: center;
}

.navBar ul li {
    position: relative;
    margin: 0 rem;
}

.navBar ul li a {
    color: var(--white);
    text-decoration: none;
    padding: 0.5rem 1rem;
    display: block;
    transition: color 0.3s ease;
}

.navBar ul li a:hover {
    color: var(--hover-color);
}

.navBar ul li .ul-second {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    background-color: var(--navbar-color);
    padding: 0.5rem 0;
    border-radius: 5px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.navBar ul li:hover .ul-second {
    display: block;
}

.navBar ul li .ul-second li {
    margin: 0;
}

.navBar ul li .ul-second li a {
    padding: 0.5rem 1rem;
    white-space: nowrap;
}

.header .login .btn, .header .login .btn2 {
    width: 150px;
    height: 45px;
    border: none;
    outline: none;
    border-radius: 50px;
    cursor: pointer;
    margin: 0 .4rem;
    font-size: 1rem;
    background-color: var(--icon-bg);
    color: var(--navbar-color);
    box-shadow: 0px 12px 12px 0px rgba(0, 0, 0, .1);
    transition: all .3s ease;
    
}
.login .btn, .login .btn2 {
    margin: 10px; 
    transition: transform 0.3s ease, background-color 0.3s ease; 
}

.login .btn:hover, .login .btn2:hover {
    background: var(--button);
    color: var(--white);
    transform: scale(1.05);
}


@media (max-width: 769px) {
    .header .login .btn,
    .header .login .btn2 {
        width: 75px;
        height: 40px;
        font-size: .6rem;
    }

    .navBar ul {
        flex-direction: column;
        align-items: flex-start;
    }

    .navBar ul li {
        margin: 0.5rem 0;
    }

    .navBar ul li .ul-second {
        position: static;
        display: none;
        padding-left: 1rem;
    }

    .navBar ul li:hover .ul-second {
        display: block;
    }
}

@media (max-width: 490px) {
    .header .login .btn, .header .login .btn2 { display: none; }
}
</style>