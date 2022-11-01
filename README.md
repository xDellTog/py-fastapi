# FastAPI

## Scripts

### Create and activate env

```bash
python -m venv venv  # create env
. venv/bin/activate  # activate env
```

### Install dependencies

```bash
. venv/bin/activate              # activate env
pip install -r requirements.txt  # install dependencies
```

### Run application

```bash
. venv/bin/activate                 # activate env
uvicorn app.main.main:app --reload  # run application
```