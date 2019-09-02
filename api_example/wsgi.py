#!/bin/env python3
from application import app
import providers.routes
# import areas.routes

if __name__ == '__main__':
    app.run(host='0.0.0.0')
