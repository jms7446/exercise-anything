from celery import Celery


app = Celery(
    'tasks',
    broker='pyamqp://guest@localhost//',
    backend='db+sqlite:///db.sqlite',
)


@app.task
def add(x, y):
    return x + y
