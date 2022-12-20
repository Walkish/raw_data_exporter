run:
	python -m venv .venv
	.venv/bin/python -m pip install -r requirements.txt
	.venv/bin/python download_raw_data.py