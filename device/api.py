from django.db.models import QuerySet
from .models import Dispositivo, PingResult
from rest_framework import  viewsets, permissions, status
from rest_framework.response import Response
from .serializers import DispositivoSerializer, PingResultSerializer
from nmap import PortScanner, nmap
from rest_framework.views import APIView

class EscanearRedViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()  # Define el queryset para obtener todos los dispositivos
    serializer_class = DispositivoSerializer  # Especifica el serializador a utilizar

    def list(self, request):
        
        # Inicializar el objeto de escaneo de red de Nmap
        scanner = PortScanner()

        # Realizar un escaneo de red para descubrir dispositivos y servicios
        scan_result = scanner.scan(hosts='192.168.1.0/24', arguments='-sn')

        # Crear objetos de dispositivo a partir de los resultados del escaneo
        dispositivos = []
        for ip, info in scan_result['scan'].items():
            dispositivo_data = {
                'ip': ip,
                'estado': info['status']['state'],
                'nombre': info['hostnames'][0]['name'] if 'hostnames' in info and info['hostnames'] else 'Desconocido',
                'puertos': list(info['tcp'].keys()) if 'tcp' in info else []
            }
            dispositivos.append(dispositivo_data)

        # Crear los dispositivos en la base de datos (opcional)
        for dispositivo_data in dispositivos:
            Dispositivo.objects.create(**dispositivo_data)

        # Obtener los dispositivos creados
        queryset = self.get_queryset()

        # Serializar los dispositivos y devolverlos como una respuesta
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

# class PingCheckViewSet(APIView):
#     def get(self, request):
#         params = request.query_params
#         ip = params.get('ip')

#         if not ip:
#             return Response({'error': 'Se requiere una direccion IP valida.'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             scanner = nmap.PortScanner()
#             scan = scanner.scan(hosts=ip, arguments='-sn')
#             result = scan['status']

#             # Opcionalmente, guardar el resultado del ping en la base de datos
#             ping_result = PingResult(ip=ip, status=result)
#             ping_result.save()

#             return Response({'result': result})
        
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                

# class GetValueAPIView(APIView):
#     def get(self, request):
#         # Obtener el valor del parámetro 'valor' de la consulta GET
#         valor = request.GET.get('valor', None)

#         if valor is not None:
#             # Devolver el valor en formato JSON
#             return Response({'valor': valor})
#         else:
#             # Si no se proporciona el parámetro 'valor', devolver un error
#             return Response({'error': 'No se proporciono el parametro "valor".'}, status=400)
           

        