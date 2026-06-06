# LoliCup — Copa Menstrual

Landing page para **LoliCup**, copa menstrual de silicona grado médico. Producto hondureño, venta directa al consumidor.

📍 **Acceso:** solo vía VPN Tailscale

## Stack

- **Frontend:** HTML5 + CSS3 vanilla
- **Backend:** Python 3 con `http.server` (servidor mínimo)
- **Despliegue:** Docker, puerto 8085

## Características

- Landing page one-page con diseño limpio y femenino
- Secciones: hero, beneficios, cómo usar, comparativa, FAQ, contacto
- Copy refinado con enfoque en beneficios reales (ahorro, salud, libertad)
- Totalmente responsive, mobile-first
- Sin dependencias externas de JS
- Carga rápida, HTML + CSS puro

## Levantar local

```bash
cd lolicup
python3 server.py
# Abrir http://localhost:8085
```

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
├── copy-audit.md            # Auditoría de copy previa
├── research-competitors.md  # Investigación de competencia
└── docker-compose.yml
```

## Notas

- El sitio corre solo en Tailscale, sin dominio público.
- El copy está refinado para conversión: lenguaje claro, beneficios tangibles, objeción-manejo.
- La investigación de competencia está en `research-competitors.md`.
