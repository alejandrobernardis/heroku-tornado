# Heroku-Tornado

A Tornado Skeleton for Heroku Platform.


### Running Locally

You need to install [Python 2.7.x](http://install.python-guide.org/) and [Heroku Toolbelt](https://toolbelt.heroku.com/).

    $: git clone git@github.com:alejandrobernardis/heroku-tornado.git
    $: cd heroku-tornado
    $: pip install -r requirements.txt
    $: python server.py


### Deploying

    $: heroku create
    $: git push heroku master
    $: heroku open

