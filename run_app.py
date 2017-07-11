#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config.routes import App


if __name__ == '__main__':
    App.run(host='0.0.0.0', debug=True)
