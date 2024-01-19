from django.shortcuts import render, redirect
from django.core.mail import EmailMessage



def contacto(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        email=EmailMessage("mensajes de app tornilleria", "el usuario: {}\n correo: {}\n Asunto: {}\n solicita:\n\n {}"
                           .format(name, email, subject, message),"",["marquezanthoan15@gmail.com"],reply_to=[email])

        try:
            email.send()

            return redirect("/contacto/?valid")
        
        except:
            return redirect("/contacto/?novalid")
        # Guarda la información del formulario en la base de datos si es necesario
        # Aquí puedes agregar la lógica para enviar el correo electrónico
       
    else:
        return render(request, 'contacto/contact.html')