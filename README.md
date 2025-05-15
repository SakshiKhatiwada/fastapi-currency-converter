# fastapi-currency-converter

Currency Converter App Created with FastAPI under Fuse Machines AI Fellowship Assignment I. The Project is made to follow most of the 12-Factor-App Principles.

---

## Prerequisites

1. Python 3.10+ installed (if running locally)
2. Docker installed (if running with Docker)
3. `.env` file with required environment variables set (reference `.env.example`)

---

## Running Locally (Without Docker)

1. Clone the Repository

   ```bash
    git clone https://github.com/SakshiKhatiwada/fastapi-currency-converter.git
    cd fastapi-currency-converter
   ```

2. Create and activate a virtual environment

   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install Dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Setup _.env_ file (create from .env.example and fill in required variables)

5. Start the FastAPI Server

   ```bash
   uvicorn app.main:app --reload

   **The app will be available at http://localhost:8000**
   ```

---

## Running with Docker

1. Clone the repo

   ```bash
   git clone https://github.com/SakshiKhatiwada/fastapi-currency-converter.git
    cd fastapi-currency-converter
   ```

2. Create a _.env_ file in the project root with required variables (refer: .env.example).

3. Build the docker image

   ```bash
   docker build -t fastapi-currency-converter .

   ```

4. Run the docker container

   ```bash
   docker run -p 8000:8000 fastapi-currency-converter
   ```

**The app will be available at http://localhost:8000**

**Note:** To stop the Docker container, use docker ps to find the container ID and then docker stop <container_id>

---

## Formatting and Linting Code

```pre-commit install```

1. ruff check / ruff check --fix / ruff format
2. black .
3. pre-commit run --all-files

## Running Tests

```bash
pytest -v -s
```
