#!/bin/bash
docker run -p 8000:80 sergio/tengine:2.3.0 &
python3 /Users/sergey/PycharmProjects/untitled/Server.py &
pytest -v /Users/sergey/PycharmProjects/untitled/test_with_class.py::TestClass1 &
pytest -v /Users/sergey/PycharmProjects/untitled/test_with_class.py::TestClass2 &
pytest -v /Users/sergey/PycharmProjects/untitled/test_with_class.py::TestClass3 &
