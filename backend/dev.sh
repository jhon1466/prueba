PORT="${PORT:-8080}"
<<<<<<< HEAD
uvicorn version_prueba.main:app --port $PORT --host 0.0.0.0 --forwarded-allow-ips '*' --reload
=======
uvicorn open_webui.main:app --port $PORT --host 0.0.0.0 --forwarded-allow-ips '*' --reload
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
