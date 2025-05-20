from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt



def pagina_inicial(request):
    return render(request, 'minha_pagina/index.html')


@csrf_exempt
def chatbot(request):
    opcoes = ["Consultar saldo", "Ver extrato", "Falar com atendente", "Encerrar chat"]

    if request.method == "POST":
        escolha = request.POST.get("escolha")
        if escolha == "Encerrar chat":
            return render(request, "minha_pagina/chatbot.html", {
                "opcoes": [], 
                "mensagem": "Chat encerrado. Obrigado!"
            })
        return render(request, "minha_pagina/chatbot.html", {
            "opcoes": opcoes, 
            "mensagem": f"Você escolheu: {escolha}"
        })

    return render(request, "minha_pagina/chatbot.html", {"opcoes": opcoes})



def adicionar_contatos(request):
    # Aqui você poderá futuramente implementar a lógica para adicionar contatos.
    return render(request, 'minha_pagina/adicionar_contatos.html')


contatos = [
    {'nome': 'João', 'telefone': '12345-6789'},
    {'nome': 'Maria', 'telefone': '98765-4321'},
]

def lista_contatos(request):
    return render(request, 'minha_pagina/lista_contatos.html', {'contatos': contatos})

