import aiohttp
import asyncio

async def send_request(url, port, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'http://localhost:{port}{url}', json=data) as response:
            return await response.json()

async def sequential_requests():
    data = {'brojevi': [1, 2, 3, 4]}

    response1 = await send_request('/zbroj', 8083, data)
    print("Mikroservis 1 odgovor (zbroj):", response1)

    response2 = await send_request('/umnozak', 8084, data)
    print("Mikroservis 2 odgovor (umnožak):", response2)

    if 'zbroj' in response1 and 'umnozak' in response2:
        response3 = await send_request('/kolicnik', 8085, {
            'zbroj': response1['zbroj'],
            'umnozak': response2['umnozak']
        })
        print("Mikroservis 3 odgovor (količnik):", response3)

async def concurrent_requests():
    data = {'brojevi': [0, 0, 0, 0]} # testira san i s legit podacima, ali stavljan 0 for comedy reasons

    task1 = send_request('/zbroj', 8083, data)
    task2 = send_request('/umnozak', 8084, data)

    response1, response2 = await asyncio.gather(task1, task2)

    print("Mikroservis 1 odgovor (zbroj):", response1)
    print("Mikroservis 2 odgovor (umnožak):", response2)

    if 'zbroj' in response1 and 'umnozak' in response2:
        response3 = await send_request('/kolicnik', 8085, {
            'zbroj': response1['zbroj'],
            'umnozak': response2['umnozak']
        })
        print("Mikroservis 3 odgovor (količnik):", response3)

async def main():
    print("Sekvencijalno slanje zahtjeva:")
    await sequential_requests()

    print("\nKonkurentno slanje zahtjeva:")
    await concurrent_requests()

if __name__ == '__main__':
    asyncio.run(main())
