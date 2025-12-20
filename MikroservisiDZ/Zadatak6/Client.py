import aiohttp
import asyncio

async def send_request(url, port):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://localhost:{port}{url}') as response:
            return await response.json()

async def sequential_requests():
    response1 = await send_request('/pozdrav', 8081)
    print("Mikroservis 1 je reka:", response1)

    response2 = await send_request('/pozdrav', 8082)
    print("Mikroservis 2 je reka:", response2)

async def concurrent_requests():
    task1 = send_request('/pozdrav', 8081)
    task2 = send_request('/pozdrav', 8082)

    response1, response2 = await asyncio.gather(task1, task2)

    print("Mikroservis 1 odgovor:", response1)
    print("Mikroservis 2 odgovor:", response2)

async def main():
    print("Sekvencijalno slanje zahtjeva:")
    await sequential_requests()
    print("  ")
    print("Konkurentno slanje zahtjeva:")
    await concurrent_requests()

if __name__ == '__main__':
    asyncio.run(main())
