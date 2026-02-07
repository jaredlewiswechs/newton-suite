# Docker: install and run

Windows (Docker Desktop):

1. Install Docker Desktop for Windows (WSL2 backend recommended):
   - Download from https://www.docker.com/products/docker-desktop
   - Enable WSL2 and install a WSL distro if prompted
   - Start Docker Desktop and ensure it's running

2. From a PowerShell terminal in the repository root (c:\Users\jnlew\newton-suite):

```powershell
# Build and run with Docker Compose (recommended)
docker compose up --build

# Or build and run manually:
docker build -t newton-nina .
docker run --rm -p 8000:8000 -v ${PWD}:/app newton-nina
```

3. Open the desktop UI at http://localhost:8000/index.html

Notes:
- The container uses Python and will install requirements listed in `adan_portable/requirements.txt` if present.
- For active development, the repository is mounted into the container so code changes reflect immediately.
