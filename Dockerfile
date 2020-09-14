FROM tiangolo/uvicorn-gunicorn-starlette:python3.7

RUN pip install --no-cache-dir jinja2 aiofiles

COPY ./app /app/app
