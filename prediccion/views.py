import numpy as np
import pandas as pd
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import calendar
import json

def home(request):
    return render(request, 'prediccion_Vista/home.html')
@csrf_exempt
def predict(request):
    if request.method == 'POST':
        año = int(request.POST.get('año'))
        mes = int(request.POST.get('mes'))

        if año <= 2021:
            return render(request, 'prediccion_Vista/error.html', {'mensaje': 'El año debe ser mayor a 2021.'})

        dias_en_mes = calendar.monthrange(año, mes)[1]
        dias = pd.date_range(start=f'{año}-{mes}-01', periods=dias_en_mes)

        # Generar predicciones base aleatorias
        predicciones_base = np.random.uniform(3000, 6000, dias_en_mes)

        # Añadir tendencia y estacionalidad
        tendencia = np.linspace(0, 1000, dias_en_mes) * np.random.choice([-1, 1])
        estacionalidad = np.sin(np.linspace(0, 2*np.pi, dias_en_mes)) * 500

        predicciones = predicciones_base + tendencia + estacionalidad

        # Añadir algunos picos aleatorios
        picos = np.random.randint(0, dias_en_mes, 3)
        predicciones[picos] += np.random.uniform(500, 1500, 3)

        # Asegurar que las predicciones estén dentro del rango 1000-7000
        predicciones = np.clip(predicciones, 1000, 7000)

        # Crear un diccionario con las predicciones por día
        predicciones_dict = {dia.day: round(pred, 2) for dia, pred in zip(dias, predicciones)}

        # Calcular la predicción total del mes
        prediccion_total_mes = round(predicciones.sum(), 2)

        return render(request, 'prediccion_Vista/result.html', {
            'año': año,
            'mes': mes,
            'predicciones': json.dumps(predicciones_dict),
            'prediccion_total_mes': prediccion_total_mes,
        })

    return render(request, 'prediccion_Vista/error.html', {'mensaje': 'Método no permitido.'})