import paho.mqtt.client as mqtt
from decouple import config


def em_conexao(client, userdata, flags, rc):
    """
    Função de retorno chamada quando o cliente recebe uma resposta CONNACK do broker MQTT.

    :param client: A instância do cliente para esta função de retorno.
    :type client: paho.mqtt.client.Client
    :param userdata: Dados do usuário privado definidos em Client() ou userdata_set().
    :type userdata: Qualquer
    :param flags: Flags de resposta enviadas pelo broker.
    :type flags: dict
    :param rc: O resultado da conexão. 0 indica sucesso, qualquer outro valor indica falha.
    :type rc: int
    """
    if rc == 0:
        print("Conectado ao broker MQTT")
    else:
        print(f"Falha na conexão, código de retorno: {rc}")

def desconectando(client, userdata, rc):
    """
    Função de retorno chamada quando o cliente se desconecta do servidor.

    Parameters:
        client (mqtt.Client): A instância do cliente MQTT.
        userdata (Any): Os dados do usuário passados para o cliente MQTT.
        rc (int): O código de retorno que indica o motivo da desconexão.

    Returns:
        None
    """
    if rc != 0:
        print(f"Desconectado inesperadamente, código de retorno: {rc}")

def conectar_ao_broker():
    """
    Conecta ao broker MQTT e retorna o cliente MQTT.

    Parameters:
        None

    Returns:
        client (mqtt.Client): O cliente MQTT conectado ao broker.
    """

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
    """
    Inscreve o cliente a um tópico específico no broker MQTT.

    Parameters:
        client (mqtt.Client): O cliente MQTT que será inscrito.
        topic (str): O tópico ao qual o cliente será inscrito.

    Returns:
        None
    """

    # Inscreve-se em um tópico específico
    client.subscribe(topic, qos=0)
    print(f"Inscrito no tópico: {topic}")