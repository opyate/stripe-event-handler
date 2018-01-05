# Intro

A Stripe event handler.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


# Usage

    curl -X POST -d '{"type":"foo"}' http://0.0.0.0:5000/stripe -H 'Content-Type: application/json'
    
STDOUT:

    Handling event type=foo
    {'type': 'foo'}


