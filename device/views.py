from django.shortcuts import render
from .models import Dispositivo, PingResult
from django.http import JsonResponse
from nmap import PortScanner

# Create your views here.


#SHODAN

# def shodan_search(request):
#     # clave de API
#     api_key = 'SE0YJmT38W7Xd7UNxwa8OfdgiAR6446U'

#     # Término de búsqueda 
#     query = 'apache'

#     # Inicializar el cliente de Shodan con tu clave de API
#     api = shodan.Shodan(api_key)

#     try:
#         # Realizar la búsqueda en Shodan
#         results = api.search(query)

#         # Pasar los resultados a la plantilla
#         return render(request, 'resultados.html', {'results': results['matches']})

#     except shodan.APIError as e:
#         # Manejar errores de la API de Shodan
#         return render(request, 'error.html', {'error_message': e})
    
#     #ESCANEAR DISPOSITIVOS EN LA RED 
    
#     def escanear_red(request):
#         # Configura el objeto de escaneo de Nmap
#         scanner = PortScanner()

#         # Realiza un escaneo de red para descubrir dispositivos y servicios
#         scan_result = scanner.scan(hosts='192.168.1.0/24', arguments='-sn')

#         # Extrae los resultados del escaneo
#         dispositivos = []
#         for ip, info in scan_result['scan'].items():
#             dispositivo = {
#                 'ip': ip,
#                 'estado': info['status']['state'],
#                 'nombre': info['hostnames'][0]['name'] if info['hostnames'] else 'Desconocido',
#                 'puertos': list(info['tcp'].keys()) if 'tcp' in info else []
#             }
#             dispositivos.append(dispositivo)

#         # Devuelve los resultados como una respuesta JSON
#         return JsonResponse({'dispositivos': dispositivos})
    

# def escanear_red(request):
#     dispositivos = Dispositivo.objects.all()
#     return render(request, 'polls/vistaDevice.html', {'dispositivos': dispositivos})

def ping_check(request):
    pingResult = PingResult.objects.all()
    return render(request, 'polls/', {'resultado': pingResult})

