#from urllib.request import Request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from django.contrib import messages
from pedidos.models import LineasPedidos, Pedidos

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


# Create your views here.

@login_required(login_url="Log_In")
def procesar_pedido(request):
    pedido=Pedidos.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedidos=list()

    for key, value in carro.carro.items():
        lineas_pedidos.append(LineasPedidos(
            productos_id = key,
            cantidad=value["cantidad"],
            user=request.user,
            pedidos = pedido
        ))

    LineasPedidos.objects.bulk_create(lineas_pedidos)

    enviar_email(
        pedidos_id=pedido,
        lineas_pedidos=lineas_pedidos,
        nombreusuario=request.user.username,
        emailusuario=request.user.email
    )

    messages.success(request, "El pedido se ha registrado correctamente.")

    return redirect("../")

def enviar_email(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html",{
        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreususario")
    })

    mensaje_texto=strip_tags(mensaje)
    from_email="lsomohano23@hotmail.com"
    to=kwargs.get("emailuser")

    send_mail(asunto, mensaje_texto, from_email, [to],html_message=mensaje)
