    # ----------------builder stage --------------------------

    From python:3.12 As builder

    WORKDIR /wheels

    COPY requirements.txt .
    
    RUN pip install --upgrade pip wheel
    
    RUN pip wheel --no-cache-dir --no-deps -r requirements.txt
    
    # -----------------------RUN TIME STAGE ----------------------
    
    FROM python:3.12-slim
    
    COPY --from=builder /wheels /wheels
    
    RUN pip install --no-cache-dir --no-index --find-links=/wheels /wheels/*.whl
    
    COPY . .
  
    RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

    CMD ["sh","-c","while ! nc -z mysql 3306; do sleep 2; done && python manage.py runserver 0.0.0.0:8000"]
