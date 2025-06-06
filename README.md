# RORI Caja API

Este es el prototipo de la "Caja RORI", una API que expone una ruta `/abrir` y se conecta a un broker MQTT para controlar dispositivos ESP32 con relé.

## 🔧 Tecnologías

- Python 3.10+
- Flask
- paho-mqtt
- flask-cors
- Mosquitto MQTT broker

## 📦 Instalación local

```bash
pip install -r requirements.txt
python caja_rori.py
```

## 🌐 Ruta principal

```
POST /abrir?dispositivo=esp32/1
```

Esto publicará un mensaje `"abrir"` en el topic MQTT `rori/esp32/1`.

## 🌍 Despliegue recomendado

Puedes desplegar este proyecto en [Render](https://render.com/) como un Web Service gratuito.

- Start Command:
  ```
  python caja_rori.py
  ```

## 🔐 CORS

Esta API acepta peticiones únicamente desde:

```
https://ju7lol.github.io
```
