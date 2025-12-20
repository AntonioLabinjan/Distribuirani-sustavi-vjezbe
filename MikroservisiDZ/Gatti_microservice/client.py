import aiohttp
import asyncio

async def get_cat_facts(url, port, amount):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://localhost:{port}{url}/{amount}') as response:
            return await response.json()

async def check_facts(url, port, facts):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'http://localhost:{port}{url}', json={"facts": facts}) as response:
            return await response.json()

async def main():
    facts_response = await get_cat_facts('/cat', 8086, 5)
    print("Prvi:", facts_response)

    if 'facts' in facts_response:
        facts = facts_response['facts']

        check_response = await check_facts('/facts', 8087, facts)
        print("Drugi:", check_response)

# Pokreni main korutinu
if __name__ == '__main__':
    asyncio.run(main())
