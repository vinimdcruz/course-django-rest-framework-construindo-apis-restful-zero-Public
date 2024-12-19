from django.http import JsonResponse

def estudantes(request):
    return JsonResponse({
        'estudantes': [
            {
                'nome': 'João',
                'idade': 20,
            },
            {
                'nome': 'Maria',
                'idade': 21,
            },
            {
                'nome': 'José',
                'idade': 22,
            },
        ]
    })