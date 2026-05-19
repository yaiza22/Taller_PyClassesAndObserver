from observer_practice.canal import CanalNoticias
from observer_practice.suscriptores import SuscriptorSMS
from observer_practice.suscriptores import SuscriptorEmail


canal = CanalNoticias("Python TV")
suscri1 = SuscriptorEmail("Carlitos")
suscri2 = SuscriptorSMS("Yaizita")

canal.suscribir(suscri1)
canal.suscribir(suscri2)
canal.publicar("No tiene un pedacito de queso?")
canal.publicar("Han hackeado el sistema!")

print("Mensajes del suscriptor " + suscri1.nombre)
for msj in suscri1.mensajes:
    print(msj)
print("Mensajes del suscriptor " + suscri2.nombre)
for msj in suscri2.mensajes:
    print(msj)
