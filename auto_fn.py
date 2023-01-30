# brand, speed, max speed, engine
# start engine, sop engine, speed up, slow down

bmw = {
    'model': 'e46',
    'speed': 0,
    'max speed': 160,
    'engine': False
}

fiat = {
    'model': 'tipo',
    'speed': 0,
    'max speed': 240,
    'engine': False
}

def auto_initialazer(model, max_speed):
    return {
        'model': model,
        'speed': 0,
        'max speed': max_speed,
        'engine': False
    }

def start_engine():
    if not car['engine']
        car['engine'] = True
        print('silnik odpalony')
    else:
        print('silnik już był odpalony')

def stop_engine(car):
    if car['speed'] == 0:
        car['engine'] = False
        print('silnik zgaszony')
    else
        print('Zatrzymaj wieprw auto')

def speed_up(car, amount):
    if car['engine']:
        car['speed'] = min(car['speed'] + amount, car['max_speed'])
        print(f'Jedziesz z predzkoscią {car["speed"]}')
    else:
        print("Odpal silnik wpierw")

def slow_down(car, amount):
    car['speed'] = max(ca['speed'] - amount, 0)
    print(f"Jedziesz z predkością {car["speed"]}'")

speed_up(bmw, 200)
start_engine(bmw)
speed_up(bmw, 50)
