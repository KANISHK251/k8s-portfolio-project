# ----------------builder stage --------------------------

    From Python:3.14 As builder

    WORKDIR /wheels
    
    RUN pip install --upgrade pip wheel
    
    RUN pip wheel --no-cache-dir --no-deps -r requirements.txt
    
    # -----------------------RUN TIME STAGE ----------------------
    
    FROM Python:3.14-slim
    
    COPY --from=builder /wheels /wheels
    
    RUN pip install --no-cache-dir --no-index --find-links=/wheels
    
    COPY backend/ .

    CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]