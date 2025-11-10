from flask import Flask,render_template, request, url_for, redirect,flash,jsonify
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row # This allows us to access columns by name
    return conn

# Create an instance of the Flask class
app = Flask(__name__)
app.secret_key = '111'

# Define a route for the home page ('/')
@app.route('/', methods=['GET', 'POST'])
def index():
    # A dummy list of messages for now
    conn = get_db_connection()

    if request.method == 'POST':
        # Get form values safely and strip surrounding whitespace
        name = request.form.get('name', '').strip()
        message = request.form.get('message', '').strip()

        # Basic validation: non-empty name/message and message length <= 140
        if name and message and len(message) <= 140:
            conn.execute('INSERT INTO messages (name, message) VALUES (?, ?)',
                         (name, message))
            conn.commit()
            conn.close()
            # flash('Message posted successfully!', 'success')
            return redirect(url_for('index'))  # Redirect to prevent form resubmission
        else:
            # flash('Invalid input. Please ensure all fields are filled and message is under 140 characters.')
            conn.close()
            return redirect(url_for('index'))
    # This code runs for a GET request
    messages = conn.execute('SELECT * FROM messages ORDER BY created_at DESC').fetchall()
    conn.close()
    guest_messages = ["First message!", "Hello from another user."]
    # Pass variables to the template
    return render_template(
        'index.html', 
        page_title='Guestbook Home', 
        messages=messages,  
    )
# def hello_world():
#     return '<h1>Hello, World!</h1>'
@app.route('/movies')
def movies():
    favorite_movies = ["Inception", "The Matrix", "Interstellar"]
    return render_template('movies.html', page_title='My Favorite Movies',
    movies=favorite_movies)

@app.route('/api/messages', methods=['POST'])
def add_message_api():
    data = request.get_json()
    name = data.get('name',"")
    message = data.get('message',"")

    if not name or not message:
        return jsonify({'status': 'error', 'message': 'Name and message are required.'}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO messages (name, message) VALUES (?, ?)',
                 (name, message))
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'success', 'message': 'Message added!'})

# A simple health check route
@app.route('/health')
def health_check():
    return 'Server is running!', 200

@app.route('/about')
def about():
    return '<h1>About Page</h1><p>This is a simple Flask application.</p>'
