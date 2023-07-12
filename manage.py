#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
sys.path.append("../")

from app import create_app

env = "production"

app = create_app(env)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=65512, debug=False)