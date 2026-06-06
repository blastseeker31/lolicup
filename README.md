# LoliCup

Landing page para LoliCup, copa menstrual de silicona grado médico. Producto de venta directa al consumidor en Honduras.

## Stack

- **Frontend:** HTML5, CSS3 vanilla
- **Backend:** Python 3 (`http.server`)
- **Despliegue:** Docker

## Características

- Landing page one-page con enfoque en conversión
- Secciones: hero, beneficios, modo de uso, comparativa, FAQ
- Diseño responsive, mobile-first
- Sin dependencias externas de JavaScript
- Copy optimizado para venta directa

## Instalación

```bash
git clone git@github.com:blastseeker31/lolicup.git
cd lolicup
python3 server.py
```

Abrir `http://localhost:8085` en el navegador.

## Docker

```bash
docker compose up -d
```

## Estructura

```
lolicup/
├── index.html               # Landing page completa
├── server.py                # Servidor HTTP mínimo
├── img/                     # Imágenes de producto
├── copy-refinado.md         # Guía de copywriting
├── research-competitors.md  # Investigación de competencia
└── docker-compose.yml
```
