from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        try:
            transporte = max(0, float(request.form.get('transporte', 0)))
            energia = max(0, float(request.form.get('energia', 0)))
            dieta = max(0, float(request.form.get('dieta', 0)))
            huella = (transporte * 0.3) + (energia * 0.5) + (dieta * 4.3 * 27)
        except ValueError:
            huella = None
        return render_template('calculator.html', huella=huella)
    return render_template('calculator.html', huella=None)

@app.route('/blog')
def blog():
    articulos = [
        {
            "titulo": "Matemáticas e informática aplicadas a ecología y zoología",
            "descripcion": "¿Es el lenguaje R una oportunidad?",
            "url": "https://www.masscience.com/matematicas-e-informatica-aplicadas-a-ecologia-y-zoologia-es-el-lenguaje-r-una-oportunidad/",
            "imagen": url_for('static', filename='img/mat.jpg')
        },
        {
            "titulo": "El cambio climático en México",
            "descripcion": "Impacto del cambio climático en el territorio mexicano.",
            "url": "https://www.masscience.com/el-cambio-climatico-en-mexico/",
            "imagen": url_for('static', filename='img/cambio.jpg')
        },
        {
            "titulo": "Uso de modelos para estimar la distribución de plagas",
            "descripcion": "Modelos como herramienta para la distribución de plagas.",
            "url": "https://www.masscience.com/uso-de-modelos-como-herramienta-para-estimar-el-area-de-distribucion-potencial-de-plagas/",
            "imagen": url_for('static', filename='img/plaga.jpg')
        },
        {
            "titulo": "Las huellas genéticas del hambre",
            "descripcion": "Análisis de la genética y su relación con el hambre.",
            "url": "https://www.masscience.com/las-huellas-geneticas-del-hambre/",
            "imagen": url_for('static', filename='img/gen.jpg')
        },
        {
            "titulo": "Almacenamientos de CO₂ y protozoos",
            "descripcion": "Investigación sobre el almacenamiento de CO₂.",
            "url": "https://www.masscience.com/los-almacenamientos-de-co2-y-los-protozoos/",
            "imagen": url_for('static', filename='img/co2.jpg')
        },
        {
            "titulo": "Introducción a la microbiología",
            "descripcion": "Conceptos básicos sobre la microbiología.",
            "url": "https://www.masscience.com/introduccion-a-la-microbiologia/",
            "imagen": url_for('static', filename='img/micro.jpg')
        },
        {
            "titulo": "Genocentrismo: un siglo de reduccionismo genético",
            "descripcion": "Estudio del genocentrismo y su evolución.",
            "url": "https://www.masscience.com/genocentrismo-un-siglo-de-reduccionismo-genetico-primera-parte/",
            "imagen": url_for('static', filename='img/geno.jpg')
        },
        {
            "titulo": "Dinosaurios y plumaje",
            "descripcion": "Relación entre dinosaurios y el plumaje.",
            "url": "https://www.masscience.com/dinosaurios-y-plumaje/",
            "imagen": url_for('static', filename='img/dino.jpg')
        },
        {
            "titulo": "Proyecto: El mar a fondo",
            "descripcion": "Exploración y conservación del océano.",
            "url": "https://www.masscience.com/proyecto-el-mar-a-fondo/",
            "imagen": url_for('static', filename='img/mar.jpg')
        }
    ]

    return render_template('blog.html', articulos=articulos)

@app.route('/products')
def products():
    productos = [
        {"nombre": "Bolígrafo Alden", "descripcion": "Bolígrafo en aluminio reciclado. Con grip en corcho.", "url": "https://tupublicista.com/catalogos/productos-ecologicos/corcho/boligrafo-alden/","imagen": url_for('static', filename='img/alden.jpg')},
        {"nombre": "Portaidentificador de Carnet Redondo II", "descripcion": "Portaidentificador en plástico. Con área de marca de 2 cm diámetro.", "url": "https://tupublicista.com/catalogos/productos-ecologicos/bamboo/porta-identificador-con-carnet-redondo-ii/","imagen": url_for('static', filename='img/porta.jpg')},
        {"nombre": "Sticky Set Eco", "descripcion": "Estuche de cartón reciclado. Libreta con 5 stickies de colores y taco de papel adhesivo.", "url": "https://tupublicista.com/catalogos/fechas-especiales/temporada-escolar/sticky-set-eco/","imagen": url_for('static', filename='img/stick.jpg')},
        {"nombre": "Sticky Set Leader Eco", "descripcion": "Libreta con 5 stickies de colores, tacos de papel autoadhesivo y bolígrafo.", "url": "https://tupublicista.com/catalogos/fechas-especiales/dia-de-la-secretaria/sticky-set-leader-eco/","imagen": url_for('static', filename='img/stick2.jpg')},
        {"nombre": "Libreta con Bolígrafo Recycle Eco", "descripcion": "Libreta argollada y bolígrafo de cartón. 80 Hojas.", "url": "https://tupublicista.com/catalogos/fechas-especiales/navidad/libreta-con-boligrafo-recycle-eco/","imagen": url_for('static', filename='img/lib.jpg')},
        {"nombre": "Libreta con Bolígrafo Gulliver Eco", "descripcion": "Libreta doble argolla y bolígrafo de cartón. 50 hojas.", "url": "https://tupublicista.com/catalogos/fechas-especiales/navidad/libreta-gulliver-eco/","imagen": url_for('static', filename='img/lib2.jpg')},
        {"nombre": "Sticky Set Spring", "descripcion": "Set de portastickies en cartón en forma de flor, 5 stickies de colores.", "url": "https://tupublicista.com/catalogos/fechas-especiales/temporada-escolar/sticky-set-spring/","imagen": url_for('static', filename='img/steck.jpg')},
        {"nombre": "Set de Café Eco", "descripcion": "Set elaborado con material ecológico: bolígrafo, portaminas, regla, estuche y borrador.", "url": "https://tupublicista.com/catalogos/fechas-especiales/temporada-escolar/set-de-cafe-eco/","imagen": url_for('static', filename='img/cafe.jpg')},
        {"nombre": "Memoria USB Swivel", "descripcion": "Memoria USB metálica disponible en bambú y fibra de trigo.", "url": "https://tupublicista.com/catalogos/fechas-especiales/dia-del-padre/memoria-usb-swivel/","imagen": url_for('static', filename='img/usb.jpg')},
        {"nombre": "Bolígrafo Woody", "descripcion": "Bolígrafo en cartón, clip en madera y punta plástica.", "url": "https://tupublicista.com/catalogos/boligrafos-economicos/boligrafo-ecologico/woody/","imagen": url_for('static', filename='img/wod.jpg')},
    ]
    return render_template('products.html', productos=productos)

@app.route('/challenges')
def challenges():
    desafios = [
        {
            "titulo": "Reducir el consumo de plástico",
            "descripcion": "Evita el uso de bolsas y botellas de plástico durante una semana.",
        },
        {
            "titulo": "Usar transporte sostenible",
            "descripcion": "Camina, usa bicicleta o transporte público en vez de automóvil.",
        },
        {
            "titulo": "Reducir consumo de energía",
            "descripcion": "Apaga luces y desconecta aparatos eléctricos cuando no los uses.",
        },
        {
            "titulo": "Adoptar una dieta sostenible",
            "descripcion": "Come más alimentos de origen vegetal y reduce el desperdicio.",
        },
        {
            "titulo": "Ahorrar agua",
            "descripcion": "Reduce el tiempo en la ducha y reutiliza agua cuando sea posible.",
        },
        {
            "titulo": "Reciclar correctamente",
            "descripcion": "Clasifica tu basura y lleva los residuos reciclables a centros de acopio.",
        },
        {
            "titulo": "Evitar productos de un solo uso",
            "descripcion": "Usa tazas reutilizables, cubiertos de metal y servilletas de tela.",
        },
        {
            "titulo": "Apoyar marcas sostenibles",
            "descripcion": "Compra productos de empresas que promuevan la sostenibilidad.",
        },
        {
            "titulo": "Realizar limpieza ecológica",
            "descripcion": "Usa productos de limpieza naturales y evita químicos contaminantes.",
        },
        {
            "titulo": "Participar en una jornada de reforestación",
            "descripcion": "Planta árboles o participa en una iniciativa local de reforestación.",
        },
    ]

    return render_template('challenges.html', desafios=desafios)

if __name__ == '__main__':
    app.run(debug=True)
