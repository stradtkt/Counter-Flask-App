from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'ThisIsASecret'

@app.route('/')
def index():
  if 'count' in session:
    session['count'] += 1
  else:
    session['count'] = 1
  return render_template('index.html', count=session['count'])

@app.route('/increment2', methods=['POST'])
def increment_two():
  session['count'] += 1
  return redirect('/')

@app.route('/reset')
def reset():
  session['count'] = 0
  return redirect('/')

app.run(debug=True)