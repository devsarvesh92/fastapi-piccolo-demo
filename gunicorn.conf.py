"""Gunicorn configuration."""


import multiprocessing as mp


# set basic options
bind = "0.0.0.0:8000"
workers = 2 * mp.cpu_count() + 1
worker_class = "uvicorn.workers.UvicornWorker"
accesslog = "-"
errorlog = "-"
forwarded_allow_ips = "*"
graceful_timeout = 90
keepalive = 380
preload_app = True
