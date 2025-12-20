from aiohttp import web
import json

async def umnozak(request):
    try:
        data = await request.json()
        brojevi = data.get('brojevi')
        
        if not brojevi:
            return web.json_response({'error': 'Nisi posla brojeve trubilo'}, status=400)
        
        rezultat = 1
        for broj in brojevi:
            rezultat *= broj
        return web.json_response({"umnozak": rezultat})
    
    except Exception as e:
        return web.json_response({'error': str(e)}, status=400)

app = web.Application()
app.router.add_post('/umnozak', umnozak)

if __name__ == '__main__':
    web.run_app(app, port=8084)
