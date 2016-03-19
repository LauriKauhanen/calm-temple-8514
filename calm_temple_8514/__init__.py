from flask import Flask
app = Flask(__name__)

# Set secret key for sessions
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

import calm_temple_8514.index
