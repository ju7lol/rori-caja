from flask import Flask, request, jsonify
from flask_cors import CORS
import paho.mqtt.publish as publish
import ssl  # Agrega esta importación al inicio si no está

app = Flask(__name__)
CORS(app, origins=["https://ju7lol.github.io"])

MQTT_BROKER = "ffb81d830b244852851f07010b2d10b7.s1.eu.hivemq.cloud"  # Reemplaza con tu hostname
MQTT_PORT = 8883
MQTT_USER = "rori_caja"             # Reemplaza con tu usuario
MQTT_PASS = "Trasero123!"            # Reemplaza con tu contraseña

@app.route("/abrir", methods=["POST", "GET"])
def abrir():
    dispositivo = request.args.get("dispositivo")
    if not dispositivo:
        return jsonify({"ok": False, "mensaje": "Falta 'dispositivo'"})

    topic = f"rori/{dispositivo}"
    try:
        publish.single(
            topic=topic,
            payload="abrir",
            hostname=MQTT_BROKER,
            port=MQTT_PORT,
            auth={"username": MQTT_USER, "password": MQTT_PASS},
            tls={"tls_version": ssl.PROTOCOL_TLS}
        )
        return jsonify({"ok": True, "mensaje": f"{dispositivo} activado"})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
