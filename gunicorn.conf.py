# WSGI config for production

bind = "0.0.0.0:8000"
workers = 4
threads = 2
timeout = 120
worker_class = "sync"
accesslog = "-"   # log to stdout
errorlog = "-"    # log to stdout
loglevel = "info"