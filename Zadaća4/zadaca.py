import requests

#response = requests.get("https://catfact.ninja/fact")
#print(response.text)
#print(response.status_code) # 200

import asyncio
import requests
import aiohttp
'''
def send_request():
  response = requests.get("https://catfact.ninja/fact")
  # deserijalizacija => pretvorimo response u json i dohvatimo fact field
  fact = response.json()["fact"]
  print(fact)

print("Šaljemo 1. zahtjev...")
send_request()

print("Šaljemo 2. zahtjev...")
send_request()

print("Šaljemo 3. zahtjev...")
send_request()

print("Šaljemo 4. zahtjev...")
send_request()

print("Šaljemo 5. zahtjev...")
send_request()
'''
'''
import requests
import time

def send_request():
  response = requests.get("https://catfact.ninja/fact")
  fact = response.json()["fact"]
  print(fact)

start = time.time()

print("Šaljemo 1. zahtjev...")
send_request()

print("Šaljemo 2. zahtjev...")
send_request()

print("Šaljemo 3. zahtjev...")
send_request()

print("Šaljemo 4. zahtjev...")
send_request()

print("Šaljemo 5. zahtjev...")
send_request()

end = time.time()
print(f"Izvršavanje programa traje {end - start:.2f} sekundi.")
'''

'''
import requests
import time

def send_request():
  response = requests.get("https://catfact.ninja/fact")
  fact = response.json()["fact"]
  print(fact)

start = time.time()

for i in range(15):
  print(f"Šaljemo {i + 1}. zahtjev...")
  send_request()

end = time.time()
print(f"Izvršavanje programa traje {end - start:.2f} sekundi.")
'''
'''
import aiohttp
import asyncio
import time

# sesije => with
# context management
# alokacija i dealokacija resursa

with open("datoteka.txt", "r") as file: # otvaramo datoteku za čitanje i koristimo alias "file"
    sadržaj = file.read() # čitamo sadržaj datoteke
    print(sadržaj)
    
file = open("datoteka.txt", "r")
sadržaj = file.read()
print(sadržaj)
file.close() # zatvaramo datoteku    

# ako želimo error handling; try-except
try:
  file = open("datoteka.txt", "r")
  sadržaj = file.read()
  print(sadržaj)
except Exception as e:
  print(f"Greška: {e}")
finally:
  file.close()
  
  '''
  
# clientsession => resurs koji otvaramo/zatvaramo je konekcija s serverom
#session = aiohttp.ClientSession()
#async with aiohttp.ClientSession() as session:
    # rad s HTTP sesijom
    
'''    
# moramo pozvat unutar rutine/korutine
async with aiohttp.ClientSession() as session:
  response = await session.get("https://catfact.ninja/fact")
  print(response)    

'''
''' PUN K SMEĆA U OUTPUTU 
async def main(): # definiramo main korutinu
  async with aiohttp.ClientSession() as session: # otvaramo HTTP sesiju koristeći context manager "with"
    response = await session.get("https://catfact.ninja/fact")
    print(response)

# pokrećemo main korutinu koristeći asyncio.run()
asyncio.run(main())
'''

'''
async def main():
  async with aiohttp.ClientSession() as session:
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json() # dodajemo await
    print(fact_dict) # ispisuje nasumičnu činjenicu

asyncio.run(main())    
'''
''' 5 komada'''
'''
async def main():
  async with aiohttp.ClientSession() as session:
    for i in range(5):
      response = await session.get("https://catfact.ninja/fact")
      fact_dict = await response.json()
      print(fact_dict)

asyncio.run(main())      
'''

''' s redosljedon
'''
'''
# nije konkurentno jer se svaki session.get awaita
async def main():
  async with aiohttp.ClientSession() as session:
    for i in range(5):
      response = await session.get("https://catfact.ninja/fact")
      fact_dict = await response.json()
      print(f"{i + 1}: {fact_dict["fact"]}")

asyncio.run(main())
'''
'''
async def main():
  async with aiohttp.ClientSession() as session:
    for i in range(5):
      response = await session.get("https://catfact.ninja/fact")
      fact_dict = await response.json()
      print(f"{i + 1}: {fact_dict["fact"]}")

asyncio.run(main())
# context manager definiramo u main korutini da smanjimo repeating kod
'''
'''
async def get_cat_fact(session):
  response = await session.get("https://catfact.ninja/fact")
  fact_dict = await response.json()
  print(fact_dict['fact'])

async def main():
  async with aiohttp.ClientSession() as session:
    cat_fact_korutine = [get_cat_fact(session) for i in range(5)]
    
# konkuretno with gather
async def main():
  async with aiohttp.ClientSession() as session:
    cat_fact_korutine = [get_cat_fact(session) for i in range(5)]
    await asyncio.gather(*cat_fact_korutine)    
   '''
'''   
# time noting
import time
async def get_cat_fact(session):
  print("Šaljemo zahtjev za mačji fact")
  response = await session.get("https://catfact.ninja/fact")
  fact_dict = await response.json()
  print(fact_dict['fact'])    
  
async def main():
  start = time.time()
  async with aiohttp.ClientSession() as session:
      cat_fact_korutine = [get_cat_fact(session) for i in range(5)]
      await asyncio.gather(*cat_fact_korutine)
  end = time.time()
  print(f"\nIzvršavanje programa traje {end - start:.2f} sekundi.")

asyncio.run(main())  
'''
'''
# konkurentno is faster nego sekencijalno  
import time
# asyncio task
async def get_cat_fact(session):
  response = await session.get("https://catfact.ninja/fact")
  fact_dict = await response.json()
  return fact_dict['fact']

async def main():
  start = time.time()
  async with aiohttp.ClientSession() as session:
    cat_fact_tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(5)] # pohranjujemo Taskove u listu
    actual_cat_facts = await asyncio.gather(*cat_fact_tasks) # pohranit ćemo rezultate u listu
  end = time.time()
  print(actual_cat_facts)
  print(f"\nIzvršavanje programa traje {end - start:.2f} sekundi.")

asyncio.run(main())
'''
'''
import asyncio
import aiohttp
import time


async def fetch_users(session):
    url = "https://jsonplaceholder.typicode.com/users"
    async with session.get(url) as response:
        return await response.json()


async def main():
    start = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_users(session) for _ in range(5)]
        results = await asyncio.gather(*tasks)

    users = results[0]

    names = [u["name"] for u in users]
    emails = [u["email"] for u in users]
    usernames = [u["username"] for u in users]

    end = time.perf_counter()

    print("Imena:", names)
    print("Emailovi:", emails)
    print("Usernames:", usernames)
    print(f"Vrijeme izvođenja: {end - start:.4f} sekundi")


asyncio.run(main())

'''
'''
import asyncio
import aiohttp


async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    async with session.get(url) as response:
        data = await response.json()
        return data["fact"]


async def filter_cat_facts(facts):
    return [
        fact
        for fact in facts
        if "cat" in fact.lower() or "cats" in fact.lower()
    ]


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [get_cat_fact(session) for _ in range(20)]

        facts = await asyncio.gather(*tasks)

    filtered = await filter_cat_facts(facts)

    print("Filtrirane činjenice o mačkama:")
    for fact in filtered:
        print(f"- {fact}")


asyncio.run(main())
'''
'''
import asyncio
import aiohttp


async def get_dog_fact(session):
    url = "https://dogapi.dog/api/v2/facts"
    async with session.get(url) as response:
        data = await response.json()
        return data["data"][0]["attributes"]["body"]


async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    async with session.get(url) as response:
        data = await response.json()
        return data["fact"]


async def mix_facts(dog_facts, cat_facts):
    mixed = []
    for dog_fact, cat_fact in zip(dog_facts, cat_facts):
        if len(dog_fact) > len(cat_fact):
            mixed.append(dog_fact)
        else:
            mixed.append(cat_fact)
    return mixed


async def main():
    async with aiohttp.ClientSession() as session:
        
        dog_facts_tasks = [get_dog_fact(session) for _ in range(5)]
        cat_facts_tasks = [get_cat_fact(session) for _ in range(5)]
        
        dog_cat_facts = await asyncio.gather(
            *dog_facts_tasks,
            *cat_facts_tasks
        )
    dog_facts = dog_cat_facts[:5]
    cat_facts = dog_cat_facts[5:]

    mixed = await mix_facts(dog_facts, cat_facts)

    print("Mixane činjenice o psima i mačkama:\n")
    for fact in mixed:
        print(fact)

asyncio.run(main())
'''
