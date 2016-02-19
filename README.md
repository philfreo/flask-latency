Flask-Latency
=============

Flask-Latency is middleware to simulate latency in a Flask development environment. Useful for debugging race conditions and other production-like scenarios while on localhost.

By default it will only ever apply latency if `app.debug` is on, and if you have the config variables below set to a non-zero value.

## Installation

- In your main application file, install the latency app as follows:

```python
from flask_latency import Latency
Latency(app)
```

- Add the configuration variables mentioned below to `app.config`.

- Finally, you'll likely want to run a development server that can properly handle multiple HTTP requests in parallel, even while one is sleeping. If you're using Flask's `app.run()` or [Flask-Script](http://flask-script.readthedocs.org/en/latest/)'s `Server` command, be sure to pass `threaded=True` as a kwarg. 

For example, change from:

`app.run()` OR `server = Server(host="0.0.0.0", port=9000)` 

To:

`app.run(threaded=True)` OR `server = Server(host="0.0.0.0", port=9000, threaded=True)`

## Configuration

### `FAKE_LATENCY_BEFORE` and `FAKE_LATENCY_AFTER`

Amount of latency, in seconds, to apply before and after the request, respectively. Can be specified as a number, or as a 2 entry tuple of numbers to act as a range of possible values (a value between those numbers will be chosen at random).

Example:

```python
# 300ms of latency, before the request is executed
FAKE_LATENCY_BEFORE = 0.3

# Between 500ms and 1s of latency, after the request is executed
FAKE_LATENCY_AFTER = (0.5, 1)
```

## License

MIT License

Author: [Phil Freo](http://philfreo.com/)
