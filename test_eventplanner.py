import pytest
from eventplanner import add_task, view_tasks, delete_task
from datetime import datetime
import csv
import os
from contextlib import redirect_stdout
import io

def test_add_task():
    # Call the function and get the returned task
    task = add_task("tasks.txt", "finish homework", "do all assignment", "2025-08-12")
    # Check if the task is written in the file
    with open("tasks.txt", "r") as file:
        content = file.read().strip()
        assert "finish homework" in content
        assert "do all assignment" in content
        assert "2025-08-12" in content


def test_view_tasks():
    with open("tasks.txt", "w") as f:
        f.write("finish homework|do all assignment|2025-08-12\n")
    f = io.StringIO()
    with redirect_stdout(f):
        view_tasks("tasks.txt")
    output = f.getvalue()
    assert "finish homework" in output
    assert "do all assignment" in output
    assert "2025-08-12" in output 


pytest.main(["-v", "--tb=line", "-rN", __file__])