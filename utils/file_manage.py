import tempfile
import os

def create_temp_file(data, suffix=None):
    """Create a temporary file with the given data and suffix."""
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as temp_file:
        if callable(data):
            data(temp_file.name)  # If data is a callable (like tts.save)
        else:
            temp_file.write(data)
        return temp_file.name

def delete_temp_file(file_path):
    """Delete the specified file if it exists."""
    if os.path.exists(file_path):
        os.unlink(file_path)
