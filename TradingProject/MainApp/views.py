# views.py
import csv
import asyncio
import json
from django.shortcuts import render, HttpResponse
from .models import Candle

def read_csv(file):
    with open(file.path) as f:
        reader = csv.reader(f)
        next(reader)  # skip the header
        return list(reader)

async def convert_candles(candles, timeframe):
    converted_candles = []
    # logic to convert candles into the given timeframe
    # ...
    return converted_candles

def store_json(candles, filename):
    with open(filename, 'w') as f:
        json.dump(candles, f)

def upload_csv(request):
    if request.method == 'POST':
        file = request.FILES['file']
        timeframe = int(request.POST['timeframe'])
        csv_data = read_csv(file)
        candles = [Candle(open=row[0], high=row[1], low=row[2], close=row[3], date=row[4]) for row in csv_data]
        candles = [candle.__dict__ for candle in candles]
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        converted_candles = loop.run_until_complete(convert_candles(candles, timeframe))
        filename = f'converted_candles_{timeframe}.json'
        store_json(converted_candles, filename)
        with open(filename, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/json')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            return response
    return render(request, 'upload_csv.html')