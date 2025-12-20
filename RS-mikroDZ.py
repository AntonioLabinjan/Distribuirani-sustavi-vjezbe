''' Prvi i drugi zadatak'''
'''
from aiohttp import web
import json

proizvodi = [
    {"naziv": "Pašareta", "cijena": 10.0, "količina": 100},
    {"naziv": "Tablete za demenciju", "cijena": 20.0, "količina": 50},
    {"naziv": "Žbula", "cijena": 15.0, "količina": 75}
]

async def get_proizvodi(request):
    return web.json_response(proizvodi)


async def add_proizvod(request):
    data = await request.json()
    print("Primljeni podaci:", data)
    proizvodi.append(data)

    return web.json_response(proizvodi)

app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_post('/proizvodi', add_proizvod)

web.run_app(app, port=8081)
'''
'''Treći zadatak'''
'''
from aiohttp import web

korisnici = [
    {"ime": "Ivo", "godine": 25},
    {"ime": "Ana", "godine": 17},
    {"ime": "Marko", "godine": 19},
    {"ime": "Maja", "godine": 16},
    {"ime": "Iva", "godine": 22}
]

async def get_punoljetni(request):
    punoljetni = [korisnik for korisnik in korisnici if korisnik['godine'] > 18]
    return web.json_response(punoljetni)

app = web.Application()
app.router.add_get('/punoljetni', get_punoljetni)

web.run_app(app, port=8082)
'''
''' Červrti
from aiohttp import web
import json
import asyncio
import aiohttp

proizvodi = [
    {"id": 1, "naziv": "Pašareta", "cijena": 10.0, "količina": 100},
    {"id": 2, "naziv": "Tablete za demenciju", "cijena": 20.0, "količina": 50},
    {"id": 3, "naziv": "Žbula", "cijena": 15.0, "količina": 75}
]


async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def get_proizvod_by_id(request):
    proizvod_id = int(request.match_info['id'])

    proizvod = next((p for p in proizvodi if p['id'] == proizvod_id), None)
    
    if proizvod:
        return web.json_response(proizvod)
    else:
        return web.json_response({'error': 'Ni tega ča išćeš'}, status=404)

async def test_server():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8081/proizvodi') as response:
            print("GET /proizvodi odgovor:", await response.text())

        async with session.get('http://localhost:8081/proizvodi/1') as response:
            print("GET /proizvodi/1 odgovor:", await response.text())

        async with session.get('http://localhost:8081/proizvodi/999') as response:
            print("GET /proizvodi/999 odgovor:", await response.text())


app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_get('/proizvodi/{id}', get_proizvod_by_id)


async def start_server():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8081)
    await site.start()

    await test_server()


if __name__ == '__main__':
    asyncio.run(start_server())
'''
'''Peti
from aiohttp import web
import json
import asyncio
import aiohttp

proizvodi = [
    {"id": 1, "naziv": "Pašareta", "cijena": 10.0, "količina": 100},
    {"id": 2, "naziv": "Tablete za demenciju", "cijena": 20.0, "količina": 50},
    {"id": 3, "naziv": "Žbula", "cijena": 15.0, "količina": 75}
]

narudzbe = []

async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def get_proizvod_by_id(request):
    proizvod_id = int(request.match_info['id'])

    proizvod = next((p for p in proizvodi if p['id'] == proizvod_id), None)
    
    if proizvod:
        return web.json_response(proizvod)
    else:
        return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)

async def post_narudzba(request):
    data = await request.json()

    proizvod_id = data.get('proizvod_id')
    proizvod = next((p for p in proizvodi if p['id'] == proizvod_id), None)

    if not proizvod:
        return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)
    
        narudzba = {
        'proizvod_id': proizvod_id,
        'naziv': proizvod['naziv'],
        'cijena': proizvod['cijena'],
        'količina': data.get('količina', 1)
    }
    narudzbe.append(narudzba)
    
    return web.json_response(narudzbe, status=201)

async def test_server():
    async with aiohttp.ClientSession() as session:

        async with session.get('http://localhost:8081/proizvodi') as response:
            print("GET /proizvodi odgovor:", await response.text())


        async with session.get('http://localhost:8081/proizvodi/1') as response:
            print("GET /proizvodi/1 odgovor:", await response.text())


        async with session.get('http://localhost:8081/proizvodi/999') as response:
            print("GET /proizvodi/999 odgovor:", await response.text())

        narudzba = {
            'proizvod_id': 1,
            'količina': 2
        }
        async with session.post('http://localhost:8081/narudzbe', json=narudzba) as response:
            print("POST /narudzbe odgovor:", await response.text())

        narudzba_invalid = {
            'proizvod_id': 999,
            'količina': 1
        }
        async with session.post('http://localhost:8081/narudzbe', json=narudzba_invalid) as response:
            print("POST /narudzbe (nevalidan ID) odgovor:", await response.text())

app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_get('/proizvodi/{id}', get_proizvod_by_id)
app.router.add_post('/narudzbe', post_narudzba)

async def start_server():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8081)
    await site.start()

    await test_server()

if __name__ == '__main__':
    asyncio.run(start_server())
'''