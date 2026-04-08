from flask import flask, request, Flask

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):

    kokonaisluku = int(luku)
    for x in range(2, kokonaisluku):
        if kokonaisluku % x == 0:
            onko_alkuluku = False
            break



   vastaus  = {
       "Number" : luku,
       "isPrime" : onko_alkuluku
   }
   return vastaus

app.run(use_reloader=True, host='127.0.0.1', port=3000)
