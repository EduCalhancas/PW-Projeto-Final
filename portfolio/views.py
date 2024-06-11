from django.shortcuts import render
import requests

def landing_page(request):
    # Global ID para Lisboa
    global_id_lisboa = 1110600
    url_previsao = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_lisboa}.json"
    response_previsao = requests.get(url_previsao)
    if response_previsao.status_code == 200:
        previsao = response_previsao.json()['data'][0]
        icon_path = f"meteo/w_ic_d_{previsao['idWeatherType']:02d}anim.svg"
        weather_data = {
            'temp_min': previsao['tMin'],
            'temp_max': previsao['tMax'],
            'descricao_tempo': previsao['idWeatherType'],
            'icon_path': icon_path,
        }
    else:
        weather_data = None

    return render(request, 'portfolio/landing_page.html', {'weather_data': weather_data})
