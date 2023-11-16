import paho.mqtt.client as mqtt
from decouple import config


def em_conexao(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker MQTT")
    else:
        print(f"Falha na conexão, código de retorno: {rc}")

def desconectando(client, userdata, rc):
    if rc != 0:
        print(f"Desconectado inesperadamente, código de retorno: {rc}")

def conectar_ao_broker():
    # Configurações MQTT
    mqtt_broker = config('MQTT_BROKER')
    mqtt_port = config('MQTT_PORT', default=1883, cast=int)

    # Cria um cliente MQTT
    client = mqtt.Client()

    # Define os callbacks de conexão e desconexão
    client.on_connect = em_conexao
    client.on_disconnect = desconectando

    # Conecta ao broker MQTT
    client.connect(mqtt_broker, mqtt_port, 60)

    # Inicia o loop MQTT em segundo plano
    client.loop_start()

    return client

def inscrever(client, topic):
    # Inscreve-se em um tópico específico
    client.subscribe(topic, qos=0)
    print(f"Inscrito no tópico: {topic}")