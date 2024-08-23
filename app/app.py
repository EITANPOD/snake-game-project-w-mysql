from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host="mysql_db",  # Docker service name
        user="root",
        password="password",
        database="snake_game_db"
    )
    return connection

# Route to submit the score
@app.route('/submit-score', methods=['POST'])
def submit_score():
    data = request.get_json()
    score = data.get('score')
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO scores (score) VALUES (%s)', (score,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Score submitted successfully!"}), 201

# Route to get scores
@app.route('/get-scores', methods=['GET'])
def get_scores():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM scores')
    scores = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(scores)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
