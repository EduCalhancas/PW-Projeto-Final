from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PrevisaoSerializer

def index_view(request):
    # Global ID para Lisboa
    global_id_lisboa = 1110600

    # URL do endpoint da previsão
    url_previsao = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_lisboa}.json"

    # URL do endpoint das classes de tempo
    url_classes_tempo = "https://api.ipma.pt/open-data/weather-type-classe.json"

    # URL do endpoint das classes de vento
    url_classes_vento = "https://api.ipma.pt/open-data/wind-speed-daily-classe.json"

    # Obter os dados da API
    response_previsao = requests.get(url_previsao)
    response_classes_tempo = requests.get(url_classes_tempo)
    response_classes_vento = requests.get(url_classes_vento)

    if response_previsao.status_code == 200 and response_classes_tempo.status_code == 200 and response_classes_vento.status_code == 200:
        previsao = response_previsao.json()['data'][0]  # Dados para hoje
        classes_tempo = response_classes_tempo.json()['data']
        classes_vento = response_classes_vento.json()['data']

        # Encontrar a descrição do tempo
        descricao_tempo = next((item for item in classes_tempo if item['idWeatherType'] == previsao['idWeatherType']), None)

        # Encontrar a descrição do vento
        descricao_vento = next((item for item in classes_vento if item['classWindSpeed'] == previsao['classWindSpeed']), None)

        # Construir o caminho do ícone
        icon_path = f"meteo/w_ic_d_{previsao['idWeatherType']:02d}anim.svg"

        context = {
            'cidade': 'Lisboa',
            'temp_min': previsao['tMin'],
            'temp_max': previsao['tMax'],
            'data': previsao['forecastDate'],
            'descricao_tempo': descricao_tempo['descWeatherTypePT'] if descricao_tempo else 'Moderada',
            'descricao_vento': descricao_vento['descClassWindSpeedDailyPT'] if descricao_vento else 'Moderado',
            'pred_wind_dir': previsao['predWindDir'],
            'icon_path': icon_path,
        }

        return render(request, 'meteo/index.html', context)
    else:
        # Em caso de erro na requisição, renderiza uma página de erro
        return render(request, 'meteo/error.html', {'message': 'Erro ao consultar a API do IPMA'})

def previsao_view(request):
    url_cidades = "https://api.ipma.pt/open-data/distrits-islands.json"
    response_cidades = requests.get(url_cidades)
    if response_cidades.status_code == 200:
        cidades = response_cidades.json()['data']
        return render(request, 'meteo/previsao.html', {'cidades': cidades})
    else:
        return render(request, 'meteo/error.html', {'message': 'Erro ao consultar a API do IPMA'})

def previsao_5_dias_view(request):
    global_id = request.GET.get('cidade')
    url_previsao = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id}.json"
    url_classes_tempo = "https://api.ipma.pt/open-data/weather-type-classe.json"
    url_classes_vento = "https://api.ipma.pt/open-data/wind-speed-daily-classe.json"

    response_previsao = requests.get(url_previsao)
    response_classes_tempo = requests.get(url_classes_tempo)
    response_classes_vento = requests.get(url_classes_vento)

    if response_previsao.status_code == 200 and response_classes_tempo.status_code == 200 and response_classes_vento.status_code == 200:
        previsoes = response_previsao.json()['data'][:5]  # Previsões para os próximos 5 dias
        classes_tempo = response_classes_tempo.json()['data']
        classes_vento = response_classes_vento.json()['data']

        for previsao in previsoes:
            descricao_tempo = next((item for item in classes_tempo if item['idWeatherType'] == previsao['idWeatherType']), None)
            descricao_vento = next((item for item in classes_vento if item['classWindSpeed'] == previsao['classWindSpeed']), None)
            previsao['descricao_tempo'] = descricao_tempo['descWeatherTypePT'] if descricao_tempo else 'Moderado'
            previsao['descricao_vento'] = descricao_vento['descClassWindSpeedDailyPT'] if descricao_vento else 'Moderado'
            previsao['icon_path'] = f"meteo/w_ic_d_{previsao['idWeatherType']:02d}anim.svg"

        context = {
            'cidade': request.GET.get('cidade_nome'),
            'previsoes': previsoes,
        }

        return render(request, 'meteo/previsao_5_dias.html', context)
    else:
        return render(request, 'meteo/error.html', {'message': 'Erro ao consultar a API do IPMA'})

class ListaCidades(APIView):
    def get(self, request):
        url_cidades = "https://api.ipma.pt/open-data/locations.json"
        response = requests.get(url_cidades)
        if response.status_code == 200:
            cidades = response.json()['data']
            return Response(cidades)
        return Response({'error': 'Erro ao consultar a API do IPMA'}, status=response.status_code)

class PrevisaoHoje(APIView):
    def get(self, request, global_id):
        url_previsao = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id}.json"
        url_classes_tempo = "https://api.ipma.pt/open-data/weather-type-classe.json"
        url_classes_vento = "https://api.ipma.pt/open-data/wind-speed-daily-classe.json"

        response_previsao = requests.get(url_previsao)
        response_classes_tempo = requests.get(url_classes_tempo)
        response_classes_vento = requests.get(url_classes_vento)

        if response_previsao.status_code == 200 and response_classes_tempo.status_code == 200 and response_classes_vento.status_code == 200:
            previsao = response_previsao.json()['data'][0]
            classes_tempo = response_classes_tempo.json()['data']
            descricao_tempo = next((item for item in classes_tempo if item['idWeatherType'] == previsao['idWeatherType']), None)
            icon_url = f"https://api.ipma.pt/open-data/icons/{previsao['idWeatherType']}.svg"
            data = {
                'cidade': 'Lisboa',  # Trocar pelo nome correto da cidade
                'temp_min': previsao['tMin'],
                'temp_max': previsao['tMax'],
                'data': previsao['forecastDate'],
                'descricao_tempo': descricao_tempo['descWeatherTypePT'] if descricao_tempo else 'Sem informação',
                'precipitacao': previsao.get('precipitaProb', 0),
                'icon_url': icon_url,
            }
            serializer = PrevisaoSerializer(data)
            return Response(serializer.data)
        return Response({'error': 'Erro ao consultar a API do IPMA'}, status=response_previsao.status_code)

class Previsao5Dias(APIView):
    def get(self, request, global_id):
        url_previsao = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id}.json"
        url_classes_tempo = "https://api.ipma.pt/open-data/weather-type-classe.json"
        url_classes_vento = "https://api.ipma.pt/open-data/wind-speed-daily-classe.json"

        response_previsao = requests.get(url_previsao)
        response_classes_tempo = requests.get(url_classes_tempo)
        response_classes_vento = requests.get(url_classes_vento)

        if response_previsao.status_code == 200 and response_classes_tempo.status_code == 200 and response_classes_vento.status_code == 200:
            previsoes = response_previsao.json()['data'][:5]
            classes_tempo = response_classes_tempo.json()['data']

            dados_previsoes = []
            for previsao in previsoes:
                descricao_tempo = next((item for item in classes_tempo if item['idWeatherType'] == previsao['idWeatherType']), None)
                icon_url = f"https://api.ipma.pt/open-data/icons/{previsao['idWeatherType']}.svg"
                dados_previsoes.append({
                    'cidade': 'Lisboa',  # Trocar pelo nome correto da cidade
                    'temp_min': previsao['tMin'],
                    'temp_max': previsao['tMax'],
                    'data': previsao['forecastDate'],
                    'descricao_tempo': descricao_tempo['descWeatherTypePT'] if descricao_tempo else 'Sem informação',
                    'precipitacao': previsao.get('precipitaProb', 0),
                    'icon_url': icon_url,
                })

            serializer = PrevisaoSerializer(dados_previsoes, many=True)
            return Response(serializer.data)
        return Response({'error': 'Erro ao consultar a API do IPMA'}, status=response_previsao.status_code)