```markdown
# 🤖 SuiteCRM Automation Framework

Automated end-to-end testing for [SuiteCRM](https://suitecrm.com) using:

- 🐍 Python
- 🎭 Playwright
- 🧪 pytest
- 🧱 Page Object Model (POM)

---

## 📦 Features

- ✅ Login and Logout automation
- ✅ Account creation and verification
- ✅ Scalable Page Object Model
- ✅ Screenshot capturing
- ✅ Environment variable support
- ✅ Extensible test structure

---

## 📂 Project Structure

```

suitecrm-tests/
│
├── pages/
│   ├── base_page.py           # Common reusable page methods
│   ├── login_page.py          # LoginPage class
│   ├── dashboard_page.py      # DashboardPage class
│   └── accounts_page.py       # AccountsPage class
│
├── tests/
│   ├── test_login.py          # Login tests
│   ├── test_create_account.py # Create Account test
│   └── test_logout.py         # Logout test
│
├── conftest.py                # pytest fixtures (browser, page, login, etc.)
├── .env                       # Environment variables (Base URL, credentials)
├── requirements.txt           # Python dependencies
├── pytest.ini                 # pytest configuration
└── README.md                  # This file

````

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/suitecrm-tests.git
cd suitecrm-tests
````

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
playwright install
```

### 5. Set Environment Variables

Create a `.env` file in the root directory:

```env
BASE_URL=http://localhost/suitecrm
USERNAME=admin
PASSWORD=admin123
```

---

## ✅ Running Tests

### Run all tests:

```bash
pytest
```

### Run tests with options:

```bash
pytest -v --headed
```

### Generate HTML report:

```bash
pytest --html=report.html
```

---

## 🧪 Sample Test Example

```python
def test_login_success(login_page, page):
    login_page.navigate("http://localhost/suitecrm/index.php?action=Login")
    login_page.login("admin", "admin123")

    from pages.dashboard_page import DashboardPage
    dashboard = DashboardPage(page)
    assert dashboard.is_logged_in()
```

---

## 🧠 Best Practices Followed

* ✅ Page Object Model (POM) for reusable page logic
* ✅ Custom `BasePage` with helper methods (click, type, wait)
* ✅ Fixtures via `conftest.py` to setup browser and pages
* ✅ Environment-based config using `python-dotenv`
* ✅ Minimal hardcoded values
* ✅ Parametrized and scalable test cases

---

## 📘 Technologies Used

| Tool       | Purpose               |
| ---------- | --------------------- |
| Python     | Programming language  |
| Playwright | Web automation engine |
| pytest     | Test runner           |
| dotenv     | Environment variables |

---

## 📃 requirements.txt

```txt
pytest
playwright
pytest-html
python-dotenv
```

---

## 🧼 To Do

* [ ] Add CI/CD integration (e.g., GitHub Actions)
* [ ] Add data-driven testing
* [ ] Expand coverage (Leads, Contacts, Opportunities)
* [ ] Add visual regression testing

---

## 🔒 Security

Avoid committing `.env` files with credentials to version control. Add `.env` to your `.gitignore`.

---

## 🧾 License

MIT License. Free to use and adapt.

---