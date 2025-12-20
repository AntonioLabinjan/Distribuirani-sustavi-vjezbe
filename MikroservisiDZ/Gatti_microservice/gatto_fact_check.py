from aiohttp import web
import json

def check_facts_for_cat(facts):
    valid_facts = []
    for fact in facts:
        if 'cat' in fact['fact'].lower() or 'cats' in fact['fact'].lower():
            valid_facts.append(fact)
    return valid_facts

async def check_facts(request):
    try:
        data = await request.json()
        facts = data.get('facts', [])
        if not facts:
            return web.json_response({'error': 'Ne dela API'}, status=400)
        
        valid_facts = check_facts_for_cat(facts)
        return web.json_response({"valid_facts": valid_facts})
    
    except Exception as e:
        return web.json_response({'error': str(e)}, status=400)

app = web.Application()
app.router.add_post('/facts', check_facts)

if __name__ == '__main__':
    web.run_app(app, port=8087)
