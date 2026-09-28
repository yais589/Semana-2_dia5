# Día 5 - Google AI Studio y API de Gemini

## Introducción

En esta práctica se ha trabajado con Google AI Studio y la API de Gemini para aprender a integrar modelos de Inteligencia Artificial Generativa en aplicaciones desarrolladas con Python.

El objetivo principal ha sido comprender el proceso de autenticación mediante API Key, realizar solicitudes al modelo Gemini, analizar texto, extraer información relevante y explorar capacidades multimodales mediante el análisis de imágenes.

---

# Objetivos de la práctica

Durante esta actividad se han realizado las siguientes tareas:

- Acceder a Google AI Studio.
- Explorar la interfaz de pruebas de Gemini.
- Configurar parámetros de generación (Temperature, Top-P y Max Tokens).
- Generar una API Key gratuita.
- Instalar y configurar la librería `google-genai`.
- Realizar llamadas a la API desde Python.
- Analizar sentimientos en textos en español e inglés.
- Identificar entidades presentes en los textos.
- Utilizar capacidades multimodales para describir imágenes.
- Documentar el proceso completo de configuración y uso.

---

# Google AI Studio

Google AI Studio es una plataforma gratuita proporcionada por Google que permite probar y utilizar modelos de la familia Gemini sin necesidad de desarrollar una aplicación completa.

Durante la práctica se realizaron pruebas con distintos prompts para observar el comportamiento del modelo y comprobar la influencia de parámetros como:

## Temperature

Controla el nivel de creatividad de las respuestas.

- Valores bajos: respuestas más precisas y predecibles.
- Valores altos: respuestas más creativas y variadas.

## Top-P

Define el conjunto de palabras candidatas que el modelo puede utilizar para generar la respuesta.

## Max Tokens

Determina la longitud máxima de la respuesta generada.

---

# Obtención de la API Key

Para utilizar la API de Gemini se siguieron los siguientes pasos:

1. Acceder a Google AI Studio.
2. Iniciar sesión con una cuenta de Google.
3. Pulsar en la opción **Get API Key**.
4. Crear una nueva clave de acceso.
5. Copiar la clave generada.
6. Utilizar la clave en los scripts de Python mediante el parámetro `api_key`.

Ejemplo:

```python
client = genai.Client(
    api_key="TU_API_KEY"
)
```

---

# Instalación del entorno

## Requisitos

- Python 3.10 o superior
- Cuenta de Google
- Conexión a Internet

## Instalación de dependencias

```bash
pip install google-genai
pip install pillow
```

Comprobación:

```bash
pip list
```

---

# Desarrollo realizado

## 1. Conexión básica con Gemini

Se desarrolló un script para comprobar la conexión con la API.

### Funcionalidad

- Conectarse al modelo Gemini.
- Enviar un prompt.
- Mostrar la respuesta obtenida.

### Resultado

La conexión se realizó correctamente y el modelo respondió a las consultas realizadas sobre diferentes temas.

---

## 2. Análisis de sentimiento

Se desarrolló un sistema de clasificación automática de sentimientos utilizando Gemini.

### Textos analizados en español

- Me encanta este producto.
- Este servicio es horrible.
- Hoy es un día normal.
- Estoy muy feliz con los resultados.
- No recomiendo esta empresa.

### Textos analizados en inglés

- I love this movie.
- This game is terrible.
- The weather is okay.
- I am very excited.
- I feel disappointed.

### Información solicitada al modelo

Para cada texto se pidió:

- Clasificación del sentimiento.
- Identificación de entidades.

### Sentimientos posibles

- Positivo
- Negativo
- Neutro

### Resultados obtenidos

El modelo clasificó correctamente los distintos textos y fue capaz de identificar entidades relevantes cuando estaban presentes.

Ejemplos:

| Texto | Sentimiento |
|---------|---------|
| Me encanta este producto | Positivo |
| Este servicio es horrible | Negativo |
| Hoy es un día normal | Neutro |
| I love this movie | Positivo |
| This game is terrible | Negativo |

---

# Capacidades multimodales

Una de las características más importantes de Gemini es su capacidad para trabajar con distintos tipos de información.

Durante esta práctica se utilizó una imagen como entrada.

## Procedimiento

1. Guardar una imagen en formato JPG.
2. Cargarla mediante la librería Pillow.
3. Enviar la imagen junto a una instrucción al modelo.
4. Obtener una descripción detallada.

Ejemplo de prompt:

```text
Describe detalladamente esta imagen.
```

### Resultado

Gemini generó una descripción precisa del contenido de la imagen, identificando objetos, colores, personas y contexto visual.

---

# Limitaciones del plan gratuito

El plan gratuito de Gemini presenta determinadas restricciones.

## Límite de solicitudes

- Aproximadamente 15 solicitudes por minuto.

## Límite diario

- Hasta 1.000.000 de tokens diarios.

## Posibles errores encontrados

Durante la práctica aparecieron algunos errores relacionados con:

### Error 503

```text
UNAVAILABLE
```

Indica saturación temporal del servicio.

### Error 429

```text
RESOURCE_EXHAUSTED
```

Indica que se ha superado temporalmente el límite de solicitudes permitidas.

En ambos casos fue posible continuar tras esperar el tiempo indicado por la plataforma.

---

# Dificultades encontradas

Durante el desarrollo surgieron diferentes incidencias:

- Problemas con modelos no disponibles.
- Límites temporales de la API.
- Errores de sintaxis al copiar código.
- Configuración inicial del entorno Python.

Todas las incidencias fueron resueltas mediante la revisión del código y la consulta de la documentación oficial.

---

# Conclusiones

La práctica ha permitido conocer el funcionamiento básico de los modelos Gemini y su integración mediante Python.

Los resultados obtenidos demuestran que la API de Gemini facilita:

- Generación automática de texto.
- Clasificación de sentimientos.
- Extracción de entidades.
- Procesamiento multimodal de imágenes.
- Integración sencilla en aplicaciones Python.

En conclusión, Gemini constituye una herramienta potente y accesible para el desarrollo de aplicaciones basadas en Inteligencia Artificial Generativa, permitiendo implementar funcionalidades avanzadas con una configuración relativamente sencilla.

---

# Archivos entregados

```

gemini_test.py
sentimientos.py
imagen.py
README.md
foto.jpg

```

---

