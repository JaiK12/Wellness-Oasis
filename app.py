from flask import Flask, request, session, render_template
from twilio.twiml.messaging_response import MessagingResponse
from chatbot import ask, append_interaction

app = Flask(__name__)

app.config['SECRET KEY'] = '019phungalalahuhu019'

@app.route('/chatbot', methods=("GET", "POST"))
def index():
    if request.method == "POST":
        healthmessage = request.form["healthmessage"]
        response = ask()
        return redirect(url_for("index", result=response))

    result = request.args.get("result")
    return render_template("index.html", result=result)



def bot():
    incoming_msg = request.values['BODY']
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction(incoming_msg, answer, chat_log)
    msg = MessagingResponse()
    msg.message(answer)
    return str(msg)





if __name__ == '__main__':
    app.run(debug=True)
