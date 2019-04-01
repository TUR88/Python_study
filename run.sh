#!/bin/bash
docker run -p 8000:80 sergio/tengine:2.3.0 &
python3 /Users/sergey/PycharmProjects/untitled/Server.py &
pytest /Users/sergey/PycharmProjects/untitled/test_with_class.py &
