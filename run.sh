#!/bin/bash
docker run -p 8000:80 sergio/tengine:2.3.0
python3 /Users/sergey/PycharmProjects/untitled/Server.py
pytest -v -k "test_server_connect" /Users/sergey/PycharmProjects/untitled/test_second_try.py
pytest -v -k "test_server_data_check_true" /Users/sergey/PycharmProjects/untitled/test_second_try.py
pytest -v -k "test_server_data_check_false" /Users/sergey/PycharmProjects/untitled/test_second_try.py
