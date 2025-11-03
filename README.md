# Fake News Detection (Flask Edition)

Fake News Detection using NLP and Machine Learning — Collected and preprocessed a large corpus of online news articles, applied TF-IDF vectorization and trained multiple classifiers (Logistic Regression, SVM, Passive Aggressive Classifier and Random Forest) to distinguish fake from legitimate news. Achieved over 95% accuracy with robust cross-validation.

## Project Structure

- `script.py` — Flask app entry point
- `templates/` — HTML templates (`index.html`, `detect1.html`)
- `static/` — CSS/JS/images
- `Datasets/` — Sample or training datasets (not required to run the app)
- `model.ipynb` — Notebook used to build/train the model
- `requirements.txt` — Python dependencies
- `Fake_News_Detector(LogesticRegression).pkl` — Pretrained model file (expected in project root)

## Prerequisites

- Python 3.9–3.12 (recommended 3.10+)
- Windows/macOS/Linux with internet access (for link fetching)

## Setup

1. Create and activate a virtual environment
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Place the model file
   - Ensure a file named `Fake_News_Detector(LogesticRegression).pkl` exists in the project root.
   - If you trained your own model, export it with joblib using the same filename or update the path in `script.py`.

## Run the App

- Start the development server:
  ```bash
  python script.py
  ```
- Open http://127.0.0.1:5000/ in your browser.

## Usage

- Home (`/`): Landing page with form.
- Detect (`/detect`, POST):
  - Provide either:
    - `web-link` — a URL to a news page. The app will scrape text from the `<article>` tag and combine `<p>` paragraphs.
    - `in-text` — paste news content directly.
  - If both are submitted, the app shows an error; provide only one input.
  - The app returns:
    - "Vraies Nouvelles" for real news
    - "Fausses Nouvelles" for fake news
    - Also shows class probabilities.

## Notes

- The app currently imports `newspaper3k` and `Flask-SQLAlchemy`, but the routes use `requests` + `BeautifulSoup` for scraping and don’t use a database. They remain in `requirements.txt` because they are imported.
- Scraping depends on the target site’s structure; if there’s no `<article>` element, the app cannot extract text and will show an error.
- For production, disable `debug=True` in `script.py` and consider using a proper WSGI server (e.g., gunicorn/uwsgi) behind a reverse proxy.

## Troubleshooting

- Model file not found: Ensure the `.pkl` exists at the project root or update the path in `script.py`.
- SSL/cert errors on requests: Upgrade certifi or try a different network.
- Windows PowerShell execution policy: If activation fails, run PowerShell as Admin and `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
