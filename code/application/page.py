from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def delete_columns(file_path, columns):
    df = pd.read_csv(file_path)
    df.drop(columns=columns, inplace=True)
    df.to_csv(file_path, index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(file.filename)
    return 'File uploaded successfully'

@app.route('/delete', methods=['POST'])
def delete():
    file_path = request.form['file_path']
    columns = request.form.getlist('columns')
    delete_columns(file_path, columns)
    return 'Columns deleted successfully'

if __name__ == '__main__':
    app.run(debug=True)
