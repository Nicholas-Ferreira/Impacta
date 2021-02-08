import paho.mqtt.client as mqtt

client = mqtt.Client()
# Funçao a ser chamada quando chegar um pacote do tipo CONNACK .

def conectou(client, userdata, flags, rc):
  print("Conectado! Código recebido:"+str(rc))
  client.subscribe("testes/primeiro")

def chegou_mensagem(client, userdata, msg):
  dado = str(msg.payload)
  print(msg.topic+" "+dado)


client.on_connect = conectou
client.on_message = chegou_mensagem
client.connect ("mqtt.eclipse.org",1883, 60)

client.loop_forever()