import streamlit as st
import streamlit.components.v1 as components
import json
import random


# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="¿Deprimido? ¡Haz clic!",
    page_icon="🐭",
    layout="centered"
)


# =========================================================
# JOKES
# =========================================================

JOKES = [

    "¿Qué le dijo un techo a otro techo? Techo de menos.",

    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",

    "¿Cómo se despiden los químicos? Ácido un placer.",

    "¿Qué le dijo el cero al ocho? Bonito cinturón.",

    "¿Qué hace un pez? ¡Nada!",

    "¿Qué le dice una iguana a su hermana gemela? Somos iguanitas.",

    "¿Cuál es el colmo de un jardinero? Que siempre lo dejen plantado.",

    "¿Cuál es el colmo de un electricista? No encontrar su corriente de trabajo.",

    "¿Cuál es el colmo de un fotógrafo? Que todo se le revele.",

    "¿Cuál es el colmo de un astronauta? Quejarse de que su trabajo no tiene futuro.",

    "¿Qué hace una computadora cuando tiene frío? Cierra Windows.",

    "¿Qué le dijo una impresora a otra? ¿Esa hoja es tuya o es impresión mía?",

    "¿Qué hace un programador cuando tiene hambre? Se come un byte.",

    "¿Cómo se llama el campeón de buceo japonés? Tokofondo.",

    "¿Y el subcampeón? Kasitoko.",

    "¿Por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas.",

    "¿Qué le dijo una pared a otra? Nos vemos en la esquina.",

    "¿Qué le dijo un semáforo a otro? No me mires, me estoy cambiando.",

    "¿Cuál es el animal más antiguo? La cebra, porque está en blanco y negro.",

    "¿Qué hace un perro con un taladro? Taladrando.",

    "¿Cómo se llama el primo vegetariano de Bruce Lee? Broco Lee.",

    "¿Qué le dijo el café al azúcar? Sin ti mi vida es amarga.",

    "¿Qué hace una vaca cuando sale el sol? Sombra.",

    "¿Qué le dijo un jardinero a otro? Disfrutemos mientras podamos.",

    "¿Qué hace un lápiz sin punta? No tiene sentido.",

    "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",

    "¿Qué le dijo una pulga a otra? ¿Vamos caminando o esperamos al perro?",

    "¿Cuál es el colmo de un peluquero? Perder el corte.",

    "¿Cuál es el colmo de un músico? Perder el compás de su vida.",

    "¿Cuál es el colmo de un panadero? Tener un hijo que sea un pan de Dios.",

    "¿Cuál es el colmo de un sastre? Tener un hijo que sea un descarado.",

    "¿Qué hace una escoba en una fiesta? Barre con todo.",

    "¿Cómo se llama el campeón de salto de trampolín en China? Chin Lan Cha.",

    "¿Cómo se llama el campeón de natación en China? Yen Toko.",

    "¿Qué le dijo un gusano a otro gusano? Voy a dar una vuelta a la manzana.",

    "¿Qué hace un pez mago? Nada por aquí, nada por allá.",

    "¿Qué le dijo una uva verde a una uva morada? ¡Respira!",

    "¿Qué le dijo una cebolla a otra? Nos hicieron llorar.",

    "¿Qué hace una caja en el gimnasio? Se pone en forma.",

    "¿Qué hace un tomate en una carrera? Ketchup.",

    "¿Por qué el tomate se puso rojo? Porque vio la ensalada desnuda.",

    "¿Qué le dijo el mar a la playa? Nada, solo se acercó.",

    "¿Qué hace un pato con una pata? Camina con la otra.",

    "¿Qué hace un matemático en el jardín? Saca las raíces.",

    "¿Qué hace un químico en una fiesta? Busca una buena reacción.",

    "¿Qué hace un físico cuando tiene hambre? Busca energía.",

    "¿Qué hace un historiador cuando se aburre? Mira atrás.",

    "¿Qué hace un arquitecto cuando se enamora? Construye una relación.",

    "¿Qué hace un fotógrafo cuando se enamora? Enfoca sus sentimientos.",

    "¿Qué hace un reloj cuando tiene hambre? Se come las horas.",

    "¿Por qué el reloj fue al médico? Porque tenía problemas de tiempo.",

    "¿Qué le dijo una taza a otra? ¿Qué taza haciendo?",

    "¿Qué le dijo una silla a otra? No te sientes así.",

    "¿Qué le dijo el lápiz al papel? Tú tienes un punto.",

    "¿Qué le dijo el papel al lápiz? No me rayes.",

    "¿Qué le dijo el jabón al agua? Juntos hacemos espuma.",

    "¿Qué hace una nube cuando tiene comezón? Se rasca con un trueno.",

    "¿Por qué el calendario está triste? Porque tiene los días contados.",

    "¿Qué hace un árbol conectado a Internet? Navega por la red.",

    "¿Qué hace una computadora en el mar? Nada por la red.",

    "¿Qué le dijo el WiFi al celular? Siento que tenemos conexión.",

    "¿Por qué el celular fue al psicólogo? Porque tenía problemas de conexión.",

    "¿Qué hace un DJ en una granja? Mezcla los huevos.",

    "¿Qué hace un músico en el supermercado? Busca las ofertas de temporada.",

    "¿Qué hace un cantante cuando pierde la voz? Se queda sin palabras.",

    "¿Por qué el músico llevó escalera al concierto? Porque quería llegar a las notas altas.",

    "¿Qué le dijo el batería al guitarrista? Tú siempre estás haciendo ruido.",

    "¿Qué hace un vampiro conduciendo un tractor? Siembra el terror.",

    "¿Qué hace un vampiro en una fábrica de sangre? Trabaja por turnos.",

    "¿Qué le dijo Drácula al espejo? Qué mala cara tienes hoy.",

    "¿Qué hace un esqueleto en una fiesta? Nada, no tiene cuerpo para bailar.",

    "¿Por qué el fantasma fue al médico? Porque se sentía transparente.",

    "¿Qué le dijo un fantasma a otro? ¿Crees en personas?",

    "¿Qué hace un gato en una computadora? Busca el ratón.",

    "¿Qué le dijo el gato al ratón? Te tengo en el cursor.",

    "¿Cuál es el animal que tiene más dientes? El ratón Pérez.",

    "¿Qué hace un perro mago? Labracadabrador.",

    "¿Qué le dijo un perro a otro perro? ¡Guau!",

    "¿Qué hace un caballo en Internet? Navega a toda velocidad.",

    "¿Qué hace una oveja sin lana? No sé, está en pausa.",

    "¿Qué hace una vaca en un terremoto? Crema batida.",

    "¿Qué hace una vaca con los ojos cerrados? Leche concentrada.",

    "¿Qué le dijo una pulga a otra? ¿Nos vamos a pie o en perro?",

    "¿Qué hace un mosquito cuando se gradúa? Busca sangre profesional.",

    "¿Qué hace un cocodrilo con una corbata? Se pone elegante de la mandíbula.",

    "¿Qué hace un pez con corbata? Nada formal.",

    "¿Qué hace una rana con una computadora? Salta de página en página.",

    "¿Qué le dijo una rana a otra? ¡Qué salto verte!",

    "¿Qué hace una abeja después de trabajar? Se va a zumbar.",

    "¿Por qué la escoba llegó tarde? Porque se quedó barriendo el camino.",

    "¿Qué hace una escoba cuando está cansada? Se apoya.",

    "¿Qué hace una cama en una fiesta? Se tiende.",

    "¿Qué hace una almohada cuando está triste? Se desahoga.",

    "¿Qué le dijo la cama al despertador? Déjame dormir, tenemos historia.",

    "¿Qué hace una puerta cuando está cansada? Se cierra.",

    "¿Qué le dijo una puerta a otra? No me cierres la conversación.",

    "¿Qué hace una escalera cuando está aburrida? Sube de nivel.",

    "¿Qué hace una lámpara cuando tiene una idea? Se ilumina.",

    "¿Qué hace un espejo cuando se enoja? Refleja la situación.",

    "¿Qué hace una ventana cuando tiene frío? Se empaña.",

    "¿Qué hace un ventilador cuando se enamora? Da vueltas por alguien.",

    "¿Qué hace una nevera en una fiesta? Mantiene la calma.",

    "¿Qué hace una cuchara en una carrera? Va a toda sopa.",

    "¿Qué hace una papa en una fiesta? Se pone frita.",

    "¿Qué hace una papa en el gimnasio? Hace puré de pesas.",

    "¿Qué hace un pan cuando va al gimnasio? Se pone fuertecito.",

    "¿Qué le dijo el pan al cuchillo? No me cortes así.",

    "¿Qué hace una pizza cuando está triste? Se queda hecha una masa.",

    "¿Qué hace una hamburguesa cuando se deprime? Se va al psicólogo de la parrilla.",

    "¿Qué hace un huevo cuando cuenta un chiste? Se parte de risa.",

    "¿Por qué el huevo no cuenta secretos? Porque se le rompen.",

    "¿Qué hace una naranja cuando se enoja? Se exprime.",

    "¿Qué hace un limón cuando está triste? Se amarga.",

    "¿Qué hace una banana cuando se tropieza? Se pela.",

    "¿Qué le dijo una uva a otra? Respira, que nos están pisando.",

    "¿Qué hace un helado cuando tiene miedo? Se derrite.",

    "¿Qué hace el queso cuando ve una película de terror? Se queda rallado.",

    "¿Qué le dijo el queso a la cámara? Sonríe para la foto.",

    "¿Por qué el café llamó a la policía? Porque lo estaban siguiendo unos granos.",

    "¿Qué hace el azúcar cuando se enamora? Se derrite.",

    "¿Qué hace una cuchara cuando se enamora? Se mete en todo.",

    "¿Qué hace una tostada en una discusión? Se queda quemada.",

    "¿Qué hace un plato cuando se cae? Se rompe el argumento.",

    "¿Qué hace un tenedor en una entrevista? Pincha la pregunta.",

    "¿Qué hace una sopa cuando se enoja? Hierve.",

    "¿Qué hace una tortilla cuando está nerviosa? Se da la vuelta.",

    "¿Qué hace una computadora cuando va al médico? Se le hace un chequeo de sistema.",

    "¿Qué hace un teclado cuando está triste? Pierde el control.",

    "¿Qué hace un ratón cuando estudia? Se prepara para el examen de clic.",

    "¿Qué hace un programador cuando termina su trabajo? Busca dónde dejó el café.",

    "¿Por qué los programadores confunden Halloween y Navidad? Porque OCT 31 = DEC 25.",

    "Hay 10 tipos de personas: las que entienden binario y las que no.",

    "¿Por qué el programador se quedó encerrado? Porque olvidó cerrar el bucle.",

    "¿Qué hace un bug en un restaurante? Se mete en el código del menú.",

    "¿Qué le dijo un bit a otro? Nos vemos en el próximo byte.",

    "¿Qué hace un algoritmo cuando está triste? Busca otra solución.",

    "¿Por qué el ordenador fue al gimnasio? Para mejorar su procesamiento.",

    "¿Qué hace un USB cuando se equivoca? Lo intenta por el otro lado.",

    "¿Por qué el WiFi terminó con el router? Ya no había conexión.",

    "¿Qué hace una impresora cuando está triste? Tiene problemas de papel.",

    "¿Qué hace un estudiante antes del examen? Rezar para que el conocimiento sea retroactivo.",

    "¿Cuál es el animal favorito de los estudiantes? El búho, porque estudia de noche.",

    "¿Qué hace un estudiante cuando sabe la respuesta? Se sorprende.",

    "¿Cuál es la materia favorita de los fantasmas? Historia, porque ya la vivieron.",

    "¿Qué hace un profesor cuando se pierde? Sigue el programa.",

    "¿Qué hace un estudiante cuando termina un examen? Revisa si escribió su nombre.",

    "¿Por qué el libro fue al médico? Porque tenía las páginas en blanco.",

    "¿Qué hace una biblioteca cuando tiene sueño? Cierra sus libros.",

    "¿Qué hace un diccionario cuando se equivoca? Busca sus palabras.",

    "¿Por qué el diccionario es tan popular? Porque tiene muchas palabras.",

    "¿Qué hace un abogado cuando tiene hambre? Se come el caso.",

    "¿Qué hace un médico cuando cuenta un chiste? Espera una buena reacción.",

    "¿Qué hace un dentista en una fiesta? Busca una buena mordida.",

    "¿Qué hace un cirujano cuando se equivoca? Espera que nadie lo note.",

    "¿Cuál es el colmo de un médico? Tener mala salud.",

    "¿Cuál es el colmo de un abogado? Perder el juicio.",

    "¿Cuál es el colmo de un carpintero? Tener una vida sin futuro porque todo se le va en clavos.",

    "¿Cuál es el colmo de un zapatero? Que siempre le pisen los talones.",

    "¿Cuál es el colmo de un pescador? Pescar una gripe.",

    "¿Cuál es el colmo de un fotógrafo? Que se le revelen los secretos.",

    "¿Cuál es el colmo de un sordo? Que le digan que no oye ni una palabra.",

    "¿Cuál es el colmo de un ciego? Enamorarse a primera vista.",

    "¿Cuál es el colmo de un calvo? Tener mala suerte y que se le caiga el pelo.",

    "¿Cuál es el colmo de un peluquero? Que su negocio se quede sin corte.",

    "¿Cuál es el colmo de un panadero? Que su negocio no levante.",

    "¿Cuál es el colmo de un relojero? Perder el tiempo.",

    "¿Cuál es el colmo de un astronauta? Necesitar espacio.",

    "¿Cuál es el colmo de un bombero? Tener una relación incendiaria.",

    "¿Cuál es el colmo de un fotógrafo? No poder enfocar su futuro.",

    "¿Cuál es el colmo de un matemático? Morirse de cálculo.",

    "¿Cuál es el colmo de un filósofo? No saber qué pensar de su situación.",

    "¿Cuál es el colmo de un músico? No encontrar la nota correcta.",

    "¿Cuál es el colmo de un escritor? Quedarse sin palabras.",

    "¿Cuál es el colmo de un electricista? Que su pareja no tenga corriente con él.",

    "¿Cuál es el colmo de un jardinero? Que su novia lo deje plantado.",

    "¿Cuál es el colmo de un agricultor? Tener un campo de dudas.",

    "¿Cuál es el colmo de un panadero? Tener mala masa laboral.",

    "¿Cuál es el colmo de un conductor? Perder el rumbo de su vida.",

    "¿Cuál es el colmo de un taxista? No tener dirección.",

    "¿Cuál es el colmo de un piloto? Perder el control.",

    "¿Cuál es el colmo de un marinero? Tener miedo a perder el norte.",

    "¿Cuál es el colmo de un meteorólogo? No tener futuro claro.",

    "¿Cuál es el colmo de un detective? No encontrar la solución.",

    "¿Cuál es el colmo de un ladrón? Que le roben el corazón.",

    "¿Cuál es el colmo de un fotógrafo enamorado? No poder desarrollar la relación.",

    "¿Cuál es el colmo de un reloj? Tener las horas contadas."

]


# =========================================================
# JAVASCRIPT DATA
# =========================================================

jokes_json = json.dumps(
    JOKES,
    ensure_ascii=False
)


# =========================================================
# APP
# =========================================================

components.html(
    f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<style>

html,
body {{
    margin: 0;
    padding: 0;
    width: 100%;
    background: transparent;
    overflow: hidden;
}}

#page {{
    width: 100%;
}}

#title {{
    height: 95px;

    display: flex;
    align-items: center;
    justify-content: center;

    overflow: hidden;

    font-family: Arial, sans-serif;
    font-size: 34px;
    font-weight: 800;

    color: white;

    text-align: center;

    white-space: nowrap;

    text-shadow:
        0 0 12px rgba(255,255,255,0.25);
}}

.title-letter {{
    display: inline-block;

    will-change: transform;

    animation:
        drift 2.8s ease-in-out infinite;
}}

@keyframes drift {{

    0% {{
        transform:
            translateY(0px)
            rotate(0deg);
    }}

    25% {{
        transform:
            translateY(-3px)
            rotate(-1deg);
    }}

    50% {{
        transform:
            translateY(2px)
            rotate(1deg);
    }}

    75% {{
        transform:
            translateY(-2px)
            rotate(-0.5deg);
    }}

    100% {{
        transform:
            translateY(0px)
            rotate(0deg);
    }}
}}


#stage {{

    width: 100%;
    height: 500px;

    position: relative;

    overflow: hidden;

    border-radius: 28px;

    background:
        radial-gradient(
            circle at 50% 50%,
            #343434 0%,
            #171717 55%,
            #050505 100%
        );

    cursor: crosshair;

    transition:
        background 0.2s ease,
        box-shadow 0.25s ease;
}}

#stage:hover {{

    box-shadow:
        0 0 35px rgba(255,255,255,0.13),
        inset 0 0 70px rgba(255,255,255,0.06);
}}

canvas {{

    position: absolute;

    inset: 0;

    pointer-events: none;
}}

#mouse {{

    position: absolute;

    left: -100px;
    top: -100px;

    font-size: 42px;

    pointer-events: none;

    transform:
        translate(-50%, -50%)
        rotate(-15deg);

    filter:
        drop-shadow(
            0 0 8px rgba(255,255,255,0.55)
        );

    transition:
        transform 0.08s linear;
}}

#joke {{

    position: absolute;

    left: 50%;
    top: 50%;

    width: 78%;

    transform:
        translate(-50%, -50%);

    text-align: center;

    font-family: Arial, sans-serif;

    font-size: 30px;
    font-weight: 700;

    line-height: 1.35;

    color: white;

    text-shadow:
        0 0 12px rgba(255,255,255,0.28),
        0 4px 18px rgba(0,0,0,0.9);

    opacity: 0;

    pointer-events: none;
}}

#status {{

    position: absolute;

    left: 0;
    right: 0;
    bottom: 18px;

    text-align: center;

    font-family: Arial, sans-serif;

    font-size: 14px;

    color:
        rgba(255,255,255,0.50);

    pointer-events: none;

    transition:
        opacity 0.25s ease;
}}

</style>

</head>

<body>

<div id="page">

    <div id="title"></div>

    <div id="stage">

        <canvas id="canvas"></canvas>

        <div id="mouse">🐭</div>

        <div id="joke"></div>

        <div id="status">
            Mueve el ratón. Haz clic.
        </div>

    </div>

</div>


<script>


// =========================================================
// HEADER
// =========================================================

const title =
    "¿Deprimido? ¡Haz clic!";

const titleElement =
    document.getElementById("title");

for (
    let i = 0;
    i < title.length;
    i++
) {{

    const letter =
        document.createElement("span");

    letter.className =
        "title-letter";

    letter.textContent =
        title[i] === " "
        ? "\\u00A0"
        : title[i];

    letter.style.animationDelay =
        (-i * 0.08) + "s";

    titleElement.appendChild(
        letter
    );
}}


// =========================================================
// ELEMENTS
// =========================================================

const stage =
    document.getElementById("stage");

const canvas =
    document.getElementById("canvas");

const ctx =
    canvas.getContext("2d");

const mouse =
    document.getElementById("mouse");

const jokeElement =
    document.getElementById("joke");

const status =
    document.getElementById("status");

const jokes =
    {jokes_json};


// =========================================================
// STATE
// =========================================================

let width = 0;
let height = 0;

let mouseX = -100;
let mouseY = -100;

let lastX = -100;
let lastY = -100;

let hue = 0;

let particles = [];
let sparks = [];

let busy = false;

let lastJoke = -1;


// =========================================================
// RESIZE
// =========================================================

function resize() {{

    width =
        stage.clientWidth;

    height =
        stage.clientHeight;

    const ratio =
        window.devicePixelRatio || 1;

    canvas.width =
        width * ratio;

    canvas.height =
        height * ratio;

    canvas.style.width =
        width + "px";

    canvas.style.height =
        height + "px";

    ctx.setTransform(
        ratio,
        0,
        0,
        ratio,
        0,
        0
    );
}}

resize();

window.addEventListener(
    "resize",
    resize
);


// =========================================================
// MOUSE MOVEMENT
// =========================================================

stage.addEventListener(
    "mousemove",
    function(event) {{

        const rect =
            stage.getBoundingClientRect();

        mouseX =
            event.clientX - rect.left;

        mouseY =
            event.clientY - rect.top;


        mouse.style.left =
            mouseX + "px";

        mouse.style.top =
            mouseY + "px";


        const dx =
            mouseX - lastX;

        const dy =
            mouseY - lastY;

        const speed =
            Math.sqrt(
                dx * dx +
                dy * dy
            );


        if (speed > 0.5) {{

            const angle =
                Math.atan2(
                    dy,
                    dx
                ) * 180 / Math.PI;

            mouse.style.transform =
                "translate(-50%, -50%) " +
                "rotate(" +
                (angle + 180) +
                "deg)";
        }}


        const xPercent =
            Math.max(
                0,
                Math.min(
                    1,
                    mouseX / width
                )
            );

        const yPercent =
            Math.max(
                0,
                Math.min(
                    1,
                    mouseY / height
                )
            );


        const color =
            Math.floor(
                xPercent * 360
            );


        stage.style.background =
            "radial-gradient(" +
            "circle at " +
            (xPercent * 100) +
            "% " +
            (yPercent * 100) +
            "%, " +
            "hsla(" +
            color +
            ", 70%, 45%, 0.30), " +
            "#111 60%, " +
            "#030303 100%)";


        const amount =
            Math.min(
                5,
                Math.floor(speed / 4)
            );


        for (
            let i = 0;
            i < amount;
            i++
        ) {{

            sparks.push({{

                x: mouseX,
                y: mouseY,

                vx:
                    (Math.random() - 0.5)
                    * 5,

                vy:
                    (Math.random() - 0.5)
                    * 5,

                life: 1,

                size:
                    Math.random() * 3 + 1,

                hue:
                    (
                        hue +
                        Math.random() * 70
                    ) % 360
            }});
        }}


        if (
            speed > 18 &&
            !busy
        ) {{

            createFirework(
                mouseX,
                mouseY
            );
        }}


        hue += 3;

        lastX = mouseX;
        lastY = mouseY;

    }}
);


// =========================================================
// FIREWORK
// =========================================================

function createFirework(x, y) {{

    const color =
        Math.floor(
            Math.random() * 360
        );


    for (
        let i = 0;
        i < 42;
        i++
    ) {{

        const angle =
            Math.random()
            * Math.PI
            * 2;

        const velocity =
            Math.random() * 5.5 + 2;


        particles.push({{

            x: x,
            y: y,

            vx:
                Math.cos(angle)
                * velocity,

            vy:
                Math.sin(angle)
                * velocity,

            life: 1,

            size:
                Math.random() * 3 + 1,

            hue:
                color +
                Math.random() * 35
        }});
    }}
}}


// =========================================================
// PARTICLES
// =========================================================

function updateParticles() {{

    for (
        let i = particles.length - 1;
        i >= 0;
        i--
    ) {{

        const p =
            particles[i];

        p.x += p.vx;
        p.y += p.vy;

        p.vx *= 0.97;
        p.vy *= 0.97;

        p.vy += 0.045;

        p.life -= 0.018;


        if (
            p.life <= 0
        ) {{

            particles.splice(
                i,
                1
            );
        }}
    }}


    for (
        let i = sparks.length - 1;
        i >= 0;
        i--
    ) {{

        const s =
            sparks[i];

        s.x += s.vx;
        s.y += s.vy;

        s.vx *= 0.95;
        s.vy *= 0.95;

        s.life -= 0.035;


        if (
            s.life <= 0
        ) {{

            sparks.splice(
                i,
                1
            );
        }}
    }}
}}


// =========================================================
// DRAW
// =========================================================

function drawParticles() {{

    ctx.clearRect(
        0,
        0,
        width,
        height
    );


    for (
        const p of particles
    ) {{

        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            p.size,
            0,
            Math.PI * 2
        );

        ctx.fillStyle =
            "hsla(" +
            p.hue +
            ",100%,65%," +
            p.life +
            ")";

        ctx.shadowBlur = 14;

        ctx.shadowColor =
            "hsl(" +
            p.hue +
            ",100%,60%)";

        ctx.fill();
    }}


    for (
        const s of sparks
    ) {{

        ctx.beginPath();

        ctx.arc(
            s.x,
            s.y,
            s.size,
            0,
            Math.PI * 2
        );

        ctx.fillStyle =
            "hsla(" +
            s.hue +
            ",100%,70%," +
            s.life +
            ")";

        ctx.shadowBlur = 9;

        ctx.fill();
    }}


    ctx.shadowBlur = 0;
}}


// =========================================================
// ANIMATION
// =========================================================

function animate() {{

    updateParticles();

    drawParticles();

    requestAnimationFrame(
        animate
    );
}}

animate();


// =========================================================
// TEXT ANIMATION
// =========================================================

function animateText(text) {{

    return new Promise(
        function(resolve) {{

            jokeElement.textContent = "";

            jokeElement.style.opacity =
                "1";

            let index = 0;


            function typeNext() {{

                if (
                    index >= text.length
                ) {{

                    resolve();

                    return;
                }}


                jokeElement.textContent +=
                    text[index];

                index++;


                setTimeout(
                    typeNext,
                    32
                );
            }}


            typeNext();

        }}
    );
}}


// =========================================================
// SPEECH
// =========================================================

function speak(text) {{

    return new Promise(
        function(resolve) {{

            if (
                !("speechSynthesis" in window)
            ) {{

                resolve();

                return;
            }}


            window.speechSynthesis.cancel();


            const utterance =
                new SpeechSynthesisUtterance(
                    text
                );

            utterance.lang =
                "es-ES";

            utterance.rate =
                0.95;

            utterance.pitch =
                1.0;

            utterance.volume =
                1.0;


            utterance.onstart =
                function() {{

                    status.textContent =
                        "🐭 El ratón está hablando...";

                }};


            utterance.onend =
                function() {{

                    status.textContent =
                        "Haz clic para otro chiste.";

                    resolve();

                }};


            utterance.onerror =
                function() {{

                    status.textContent =
                        "Haz clic para otro chiste.";

                    resolve();

                }};


            window.speechSynthesis.speak(
                utterance
            );

        }}
    );
}}


// =========================================================
// CLICK
// =========================================================

stage.addEventListener(
    "click",
    async function(event) {{

        if (busy) return;

        busy = true;


        status.textContent =
            "Espera...";


        const rect =
            stage.getBoundingClientRect();

        const x =
            event.clientX -
            rect.left;

        const y =
            event.clientY -
            rect.top;


        // -------------------------------------------------
        // Mouse reaction
        // -------------------------------------------------

        mouse.style.left =
            x + "px";

        mouse.style.top =
            y + "px";

        mouse.style.transform =
            "translate(-50%, -50%) scale(1.3)";


        setTimeout(
            function() {{

                mouse.style.transform =
                    "translate(-50%, -50%) scale(1)";

            }},
            140
        );


        // -------------------------------------------------
        // Fireworks
        // -------------------------------------------------

        createFirework(
            x,
            y
        );

        createFirework(
            width / 2,
            height / 2
        );


        setTimeout(
            function() {{

                createFirework(
                    Math.random() * width,
                    Math.random() * height
                );

            }},
            180
        );


        // -------------------------------------------------
        // Select joke
        // -------------------------------------------------

        let index;

        do {{

            index =
                Math.floor(
                    Math.random()
                    * jokes.length
                );

        }} while (
            index === lastJoke &&
            jokes.length > 1
        );


        lastJoke =
            index;


        const joke =
            jokes[index];


        // -------------------------------------------------
        // Reveal
        // -------------------------------------------------

        await animateText(
            joke
        );


        // -------------------------------------------------
        // Speak
        // -------------------------------------------------

        await speak(
            joke
        );


        // -------------------------------------------------
        // Ready
        // -------------------------------------------------

        status.textContent =
            "Haz clic para otro chiste.";

        busy = false;

    }}
);


// =========================================================
// AMBIENT FIREWORKS
// =========================================================

setInterval(
    function() {{

        if (
            !busy &&
            Math.random() > 0.55
        ) {{

            createFirework(
                Math.random() * width,
                Math.random() * height
            );
        }}

    }},
    1100
);


</script>

</body>

</html>
""",
    height=620
)