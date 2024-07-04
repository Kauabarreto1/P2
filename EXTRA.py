import pywhatkit
phone_number = str(input("Insira o número da pessoa desejada: "))
message = str(input("A mensagem que vc deseja enviar: "))
hours = int(input("A hora que a mensagem será enviada: "))
minutes = int(input("O minuto que a mensagem será enviada: "))
pywhatkit.sendwhatmsg(phone_number, message, hours, minutes)
print ("Mensagem enviada")