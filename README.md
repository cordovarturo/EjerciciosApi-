# API de Promedio de Calificaciones


API REST construida con Flask que recive el nombre de un estudiante
y una lista de calificaciones, y retorna el promedio calculado.

---

## Tecnologias

- Python 3.x
- Flask

---

## Instalacion
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## Uso
```bash
python app.py
```

El servidor corre en: `http://127.0.0.1:5000`

---

## Endpoint

### POST `/promedio`

Calcula el promedio de las calificaciones de un estudiante.

**Body (JSON):**
```json
{
  "nombre": "Juan",
  "calificaciones": [80, 90, 85, 70]
}
```

**Respuesta exitosa `200`:**
```json
{
  "nombre": "Juan",
  "calificaciones": [80, 90, 85, 70],
  "promedio": 81.25
}
```

**Errores posibles:**

| Codigo | Descripcion                                      |
|--------|--------------------------------------------------|
| 400    | No se enviaron datos                             |
| 400    | Faltan campos requeridos                         |
| 400    | La lista de calificaciones no puede estar vacia  |

---

## Prueba rapida con curl
```bash
curl -X POST http://127.0.0.1:5000/promedio \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Juan", "calificaciones": [80, 90, 85, 70]}'
```

---

## Estructura del proyecto
```
proyecto/
├── app.py
├── requirements.txt
└── README.md
```
# API Conversor de Temperaturas

API REST construida con Flask que convierte temperaturas entre
Celsius y Fahrenheit usando las formulas de conversion estandar.

---

## Tecnologias

- Python 3.x
- Flask

---

## Instalacion
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## Uso
```bash
python app.py
```

El servidor corre en: `http://127.0.0.1:5000`

---

## Endpoint

### POST `/convertir-temperatura`

Convierte un valor de temperatura segun la escala de origen.

**Celsius a Fahrenheit:**
```json
{
  "valor": 100,
  "escala": "Celsius"
}
```
```json
{
  "valor_original": 100,
  "escala_origen": "Celsius",
  "valor_convertido": 212.0,
  "escala_destino": "Fahrenheit"
}
```

**Fahrenheit a Celsius:**
```json
{
  "valor": 32,
  "escala": "Fahrenheit"
}
```
```json
{
  "valor_original": 32,
  "escala_origen": "Fahrenheit",
  "valor_convertido": 0.0,
  "escala_destino": "Celsius"
}
```

**Errores posibles:**

| Codigo | Descripcion                                      |
|--------|--------------------------------------------------|
| 400    | No se enviaron datos                             |
| 400    | Faltan campos requeridos                         |
| 400    | Escala no valida                                 |

---

## Formulas utilizadas

| Conversion            | Formula              |
|-----------------------|----------------------|
| Celsius a Fahrenheit  | (C x 9/5) + 32       |
| Fahrenheit a Celsius  | (F - 32) x 5/9       |

---

## Prueba rapida con curl
```bash
curl -X POST http://127.0.0.1:5000/convertir-temperatura \
  -H "Content-Type: application/json" \
  -d '{"valor": 100, "escala": "Celsius"}'
```

---

## Estructura del proyecto
```
proyecto/
├── app.py
├── requirements.txt
└── README.md
```
