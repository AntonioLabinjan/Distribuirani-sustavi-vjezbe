from aiohttp import web
import json

async def kolicnik(request):
    try:
        data = await request.json()
        zbroj = data.get('zbroj')
        umnozak = data.get('umnozak')
        
        if zbroj is None or umnozak is None:
            return web.json_response({'error': 'Nedostaju podaci za zbroj ili umnožak'}, status=400)
        
        if zbroj == 0:
            return web.json_response({'error': 'Vrajno slabo, nemoj mi dijelit z nulon'}, status=400)
        
        rezultat = umnozak / zbroj
        return web.json_response({"kolicnik": rezultat})
    
    except Exception as e:
        return web.json_response({'error': str(e)}, status=400)

app = web.Application()
app.router.add_post('/kolicnik', kolicnik)


if __name__ == '__main__':
    web.run_app(app, port=8085)
