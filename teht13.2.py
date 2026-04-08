from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flight_game"
)

@app.route('/kentta/<icao>', methods=['GET'])
def get_airport(icao):
    cursor = connection.cursor(dictionary=True)

    sql = """
        SELECT ident, name, municipality
        FROM airport
        WHERE ident = %s
    """

    cursor.execute(sql, (icao.upper(),))
    result = cursor.fetchone()

    cursor.close()

    if result is None:
        return jsonify({"error": "Kenttää ei löytynyt"}), 404

    return jsonify({
        "ICAO": result["ident"],
        "Name": result["name"],
        "Municipality": result["municipality"]
    })


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)