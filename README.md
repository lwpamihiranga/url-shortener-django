![Workflow Status](https://github.com/lwpamihiranga/url-shortener-django/actions/workflows/run-tests.yml/badge.svg)

# URL Shortener - Django REST Framework 

## Introduction
Welcome to the **URL Shortener**!

This implement a **simple URL shortener API** using **Django** and **Django REST Framework (DRF)**. This application allows users to submit a long URL and receive a shortened URL. When a user accesses the short URL, they should be redirected to the original URL.  

---

## Scenario
Imagine you're building a **miniature version of bit.ly** or **TinyURL**. Users should be able to:  

1. Submit a long URL via an API endpoint and receive a shortened version.  
2. Use the short URL to be redirected to the original long URL.  
3. (Bonus) View basic statistics about the shortened URL (e.g., number of times accessed).  

---

## Requirements
You need to implement the following features:  

* **Shorten a URL**: Accept a long URL via an API endpoint and return a unique short URL.  
* **Redirect to Original URL**: When a user visits the short URL, they should be redirected to the original long URL.  
* **Validation**: Ensure the input is a valid URL.  
* **Database Storage**: Store the original and shortened URLs in SQLite.  
* **API Implementation**: Use Django REST Framework (DRF) to expose the necessary endpoints.  
* **Code Structure & Best Practices**: Follow Django’s best practices for project structure, error handling, and API design.  

### Bonus (Optional)
* Track the number of times a short URL has been accessed.  
* Implement rate limiting to prevent abuse.  
* Allow users to specify a custom short URL (e.g., `https://yourshortener.com/mycustomlink`).  

---

## Project Setup & Installation

**1. Clone the Repository**
```bash
git clone https://github.com/your-org/url-shortener.git
cd url-shortener
```

**2. Create & Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

**3. Install the Requirements**
```bash
pip install -r requirements.txt
```

**4. Apply Migrations & Start the Server**
```bash
python manage.py migrate
python manage.py runserver
```
## 5. API Endpoints

| Method  | Endpoint              | Description |
|---------|-----------------------|-------------|
| `POST`  | `/api/shorten/`       | Submit a long URL and receive a short URL. |
| `GET`   | `/short/<short_code>/` | Redirect to the original long URL. |
| (Bonus) `GET`  | `/api/stats/<short_code>/` | Retrieve stats for a short URL (e.g., access count). |

## **Screenshots**:
- Using Makefile commands

![1-make-file-in-action](https://github.com/user-attachments/assets/5f54e322-e4a7-4348-a9e1-a6314232c769)

- Generate short URL

![2-generate-short-url](https://github.com/user-attachments/assets/6c006040-aa71-4b6b-90d6-6b8fb680957b)

- Generate short URL with custom code

![3-generate-short-url-with-custom](https://github.com/user-attachments/assets/8bbc54be-6758-41c1-a7e8-20ca68bb904a)

- Redirect to URL

![4-redirect-to-url](https://github.com/user-attachments/assets/a77feff0-de5b-4668-9e12-286118721de6)

- Get stats

![5-get-stats](https://github.com/user-attachments/assets/a4860c90-08d5-4cb2-b976-75f04adf4647)

- GitHub Actions run tests on PR Open (Tested on a personal private repo)

![6-workflow-test-run-on-pr](https://github.com/user-attachments/assets/a63c0bd8-e139-4fcf-97c6-9c4bea4f3386)

- GitHub Actions run tests on PR merge to main (Tested on a personal private repo)

![7-workflow-test-run-on-merge](https://github.com/user-attachments/assets/5ff9b972-875b-47da-8a05-709b8a1c7993)

- Workflow Status Badge (Screenshot is from a personal private repo)

![8-workflow-status-badge](https://github.com/user-attachments/assets/e9627804-24e6-42c3-ab3d-510886438e30)
