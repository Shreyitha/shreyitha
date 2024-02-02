from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        task = request.form.get('task')
        tasks.append({'title': task, 'completed': False})
    return render_template('index.html', tasks=tasks)

@app.route('/complete/<int:index>')
def complete(index):
    tasks[index]['completed'] = True
    return redirect(url_for('home'))

@app.route('/delete/<int:index>')
def delete(index):
    tasks.pop(index)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)