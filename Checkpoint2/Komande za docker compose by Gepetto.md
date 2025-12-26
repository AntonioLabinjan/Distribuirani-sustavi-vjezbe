# 1️⃣ Stopaj i ugasi sve kontejnere
docker-compose down

# 2️⃣ (Opcionalno) Force stop i remove svih starijih kontejnera ako je nešto još gore
docker ps -a -q | xargs -r docker rm -f

# 3️⃣ Remove sve stare image-e iz composea (da nema cache-a)
docker-compose images -q | xargs -r docker rmi -f

# 4️⃣ Očisti Docker build cache (da se ništa ne reuse-a)
docker builder prune -a -f

# 5️⃣ Rebuildaj sve servise iz docker-compose.yml
docker-compose build --no-cache

# 6️⃣ Upaj sve servise u detach modu
docker-compose up -d

# 7️⃣ Provjeri logove da sve radi
docker-compose logs -f
