from flask import Flask, render_template, redirect, url_for
import stripe
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

stripe.api_key = os.getenv('secret_key')

YOUR_DOMAIN = 'http://localhost:5000'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Puppy Donation',
                    },
                    'unit_amount': 1999,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=YOUR_DOMAIN + '/thankyou',
            cancel_url=YOUR_DOMAIN + '/',
        )
        return redirect(session.url, code=303)

    except Exception as e:
        return str(e)


@app.route('/thankyou')
def thankyou():
    return "<h1>Gracias por tu donación 🐶</h1>"


if __name__ == '__main__':
    app.run(debug=True)