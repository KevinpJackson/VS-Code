from flask import Flask, render_template, request, flash
import random

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def home():
        decision = None
        error_message = None
        
        if request.method == 'POST':
            user_input = request.form.get('question')
            if '?' not in user_input:
                responses_1 = [ 
                    "Please add a question mark (?) at the end of a question or are you illiterate?"
                ]
                decision = random.choice(responses_1)
                return render_template('index.html', user_input=user_input, decision=decision)
            
            else:
                responses_2 = [
                    "Yes, Absolutely!",
                    "No, Not today.",
                    "Yeah i guess...",
                    "Are you crazy?",
                    "Definitely........Not.",
                    "Dumb question, yes.",
                    "Ugh, no.",
                    "Yeah do whatever :P",
                    "No idea, but you look kinda cute :3",
                    "In a forever growing universe filled with millions of planets and possible life forms, does this really matter?"
                    "I don't wanna answer that.",
                    "Yes definitely. (Maybe)",
                ]
                decision = random.choice(responses_2)
            return render_template('index.html', user_input=user_input, decision=decision)
        
        return render_template('index.html')
    
    return app