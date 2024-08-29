from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='mysql_db',
        user='root',
        password='password',
        database='snake_game'
    )
# conn = get_db_connection()

@app.route('/score', methods=['POST'])
def submit_score():
    conn = get_db_connection()
    data = request.json
    player_name = data['player_name']
    score = data['score']

    cursor = conn.cursor()
    cursor.execute("INSERT INTO scores (player_name, score) VALUES (%s, %s)", (player_name, score))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Score submitted successfully"}), 201

@app.route('/highscores', methods=['GET'])
def get_highscores():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT player_name, MAX(score) AS highest_score, COUNT(*) AS games_played FROM scores GROUP BY player_name ORDER BY highest_score DESC LIMIT 10;")
    highscores = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("highscores.html", highscores=highscores)

@app.route('/highscores-table', methods=['GET'])
def highscores_table():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT player_name, score FROM scores ORDER BY score DESC LIMIT 10")
    highscores = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('highscores.html', highscores=highscores)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)