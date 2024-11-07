from flask import *
import sqlite3
from threading import *
from multiprocessing import *
import requests
import time
import asyncio
import os
import logging


# Disable flask logging
logging.getLogger('werkzeug').disabled = True


app = Flask(__name__)

@app.errorhandler(500)
def error500(e):
    return '<meta http-equiv="refresh" content="0; url=https://www.youtube.com/watch?v=cmMXp2taRXc" />', 500
@app.errorhandler(404)
def error404(e):
    return '<meta http-equiv="refresh" content="0; url=https://www.youtube.com/watch?v=cmMXp2taRXc" />', 404

@app.route(f'/capes/<user>.png')
def cape(user):
    if(user.isalnum()==False):
        return '<meta http-equiv="refresh" content="0; url=https://www.youtube.com/watch?v=cmMXp2taRXc" />'
    db = sqlite3.connect("db.db")
    cursor = db.cursor()
    user = request.path[7:]
    user = user[:-4]
    cape = cursor.execute(f'SELECT cape FROM users WHERE nick = "{user}"').fetchone()
    db.commit()
    db.close()
    if(cape != None):
        return send_file(f'capes/{cape[0]}.png', mimetype='image/png')
    else:
        img = requests.get(f'http://s.optifine.net/capes/{user}.png', headers={'User-Agent':'Java/1.8.0_51'})
        if('found' in img.text):
            return '<meta http-equiv="refresh" content="0; url=https://www.youtube.com/watch?v=cmMXp2taRXc" />'
        else:
            open(f'cached_capes/{user}.png', 'wb').write(img.content)
            return send_file(f'cached_capes/{user}.png', mimetype='image/png')


Thread(target=lambda: app.run(host='0.0.0.0', port=80, debug=False, use_reloader=False)).start()