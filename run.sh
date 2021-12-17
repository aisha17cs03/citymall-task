WORKDIR=$PWD
BACKEND_PATH="$PWD"

WORKDIR=$PWD
BACKEND_PATH="$PWD/BackEndApp"
backend_setup() {
    cd "$BACKEND_PATH"
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python app.py
}

backend_setup()