from flask import Flask, request, render_template

import wikipedia, os

app=Flask(__name__)

summary=[]

@app.route("/",methods=['GET'])
def inputWikipedia():
	return render_template("front.html")

@app.route("/resultwiki",methods=['POST'])
def Search():
		query=request.form.get('query')
		return wikipedia.summary(query)


if __name__=="__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, use_reloader=True, debug=True)
