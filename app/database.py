import json
import os

DB_FILE = "data.json"

# Initialize database if it doesn't exist
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as db:
        json.dump({"tasks": [], "notes": []}, db)

def _load_database():
    """This will help in Loading  the database content."""
    try:
        with open(DB_FILE, "r") as db:
            return json.load(db)
    except (IOError, json.JSONDecodeError) as e:
        raise Exception("Failed to load the database. Ensure the file is accessible and valid.") from e

def _save_database(data):
    """lets Save the database content."""
    try:
        with open(DB_FILE, "w") as db:
            json.dump(data, db)
    except IOError as e:
        raise Exception("Failed to save data to the database. Ensure write permissions are available.") from e

def get_tasks():
    """timeee to Retrieve the list of tasks."""
    try:
        data = _load_database()
        return data.get("tasks", [])
    except Exception as e:
        raise Exception(f"Error retrieving tasks: {str(e)}")

def add_task(task):
    """letzzzz Add a new task to the database."""
    try:
        if not task:
            raise ValueError("Task cannot be empty.")
        data = _load_database()
        data["tasks"].append(task)
        _save_database(data)
    except Exception as e:
        raise Exception(f"Error adding task: {str(e)}")

def delete_task(task):
    """time to Delete a task from the database."""
    try:
        data = _load_database()
        if task in data.get("tasks", []):
            data["tasks"].remove(task)
            _save_database(data)
        else:
            raise ValueError("Task not found in the database.")
    except Exception as e:
        raise Exception(f"Error deleting task: {str(e)}")

def get_notes():
    """hmmmmm, lets Retrieve the list of notes."""
    try:
        data = _load_database()
        return data.get("notes", [])
    except Exception as e:
        raise Exception(f"Error retrieving notes: {str(e)}")

def add_note(note):
    """Add new note to the db."""
    try:
        if not note:
            raise ValueError("Note cannot be empty.")
        data = _load_database()
        data["notes"].append(note)
        _save_database(data)
    except Exception as e:
        raise Exception(f"Error adding note: {str(e)}")

def delete_note(note):
    """Delete a note from the db."""
    try:
        data = _load_database()
        if note in data.get("notes", []):
            data["notes"].remove(note)
            _save_database(data)
        else:
            raise ValueError("Note not found in the database.")
    except Exception as e:
        raise Exception(f"Error deleting note: {str(e)}")
