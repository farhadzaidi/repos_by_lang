from flask import render_template, url_for, request
from src import app
import requests as r

@app.route('/', methods=['GET', 'POST'])
def home():

	if request.method == 'POST':
		language = request.form['languages']
		results = r.get(f"https://api.github.com/search/repositories?q=language:{language}&sort=stars").json()
		top_ten = results['items'][0:10]

		return render_template('results.html', top_ten=top_ten)

	return render_template('home.html')