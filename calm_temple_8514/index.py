from calm_temple_8514 import app

@app.route('/')
def index():
    return echo 'Hello World!'
