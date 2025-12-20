from aiohttp import web
import asyncio
import aiohttp

async def fetch_cat_facts(amount):
    url = f'https://catfact.ninja/facts?limit={amount}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data['data']

async def get_cat_facts(request):
    facts = await fetch_cat_facts(10)
    return web.json_response({"facts": facts})

async def get_cat_facts_by_amount(request):
    amount = int(request.match_info['amount'])
    facts = await fetch_cat_facts(amount)
    return web.json_response({"facts": facts})

app = web.Application()
app.router.add_get('/cats', get_cat_facts)
app.router.add_get('/cat/{amount}', get_cat_facts_by_amount)

if __name__ == '__main__':
    web.run_app(app, port=8086)
