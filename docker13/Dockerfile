FROM ubuntu:latest

RUN apt update && apt install -y python3

COPY app.py /app.py

# ENTRYPOINT [ "python3" ] Podría usarse para que reemplace el bash

CMD ["python3", "/app.py"]
