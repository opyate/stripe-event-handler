<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Intro](#intro)
- [Adding handlers](#adding-handlers)
- [Usage](#usage)

<!-- markdown-toc end -->


# Intro

A Stripe event handler.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


# Adding handlers

If the Stripe event is called `foo.bar`, add the following module:

    mkdir -p handlers/foo/bar
    touch handlers/foo/bar/__init__.py


Add a function to this new script:

    def handle(event_json):
        print('A foo.bar event handler!')

# Usage

    curl -X POST -d '{"type":"foo.bar", "other": "stuff"}' http://0.0.0.0:5000/stripe -H 'Content-Type: application/json'
    
STDOUT:

    Handling event type=foo.bar
    {'type': 'foo.bar', 'other': 'stuff'}
    A foo.bar event handler!

