
# Create a new virtual environment with the correct command
#python -m venv .venv  # if python points to 3.11
# or
#python3 -m venv .venv  # if python3 points to 3.11
# or
py -3.11 -m venv .venv  # if py supports version 3.11

pip install -r requirements.txt

.\.venv\Scripts\activate