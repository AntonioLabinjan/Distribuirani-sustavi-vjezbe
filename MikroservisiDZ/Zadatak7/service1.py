from aiohttp import web
import json

async def zbroj(request):
    try:
        data = await request.json()
        brojevi = data.get('brojevi')
        
        if not brojevi:
            return web.json_response({'error': 'Nisi posla brojeve stupido'}, status=400)
        
        rezultat = sum(brojevi)
        return web.json_response({"zbroj": rezultat})
    
    except Exception as e:
        return web.json_response({'error': str(e)}, status=400)

app = web.Application()
app.router.add_post('/zbroj', zbroj)


if __name__ == '__main__':
    web.run_app(app, port=8083)
