# 💳 Bank Management System

A complete bank management system with customer, account, and transaction management using Python, SQLite for backend, and Streamlit for interactive UI. Includes CSV export and admin features.

This is a **full-stack database project** developed using Python, SQLite, and Streamlit. It offers a complete Bank Management experience — from customer and account creation to transaction management and reporting.

---

## 🚀 Project Overview

This project simulates a mini banking system that can be used by bank staff to:

- Manage customer data
- Create and manage multiple accounts
- Perform deposits, withdrawals, and transfers
- View and export transaction history
- Use either a **Command-Line Interface (CLI)** or a **Streamlit-based web UI**

---

## 📚 Project Phases

### 🧱 Phase 1: Database & Core Logic

- Designed database schema using SQLite.
- Created helper files:
  - customer.py – customer creation, viewing, deleting
  - account.py – account creation, deletion, listing
  - transaction.py – deposit, withdraw, transfer, transaction history

### 💻 Phase 2: CLI App

- Built main.py to interact with all modules via command-line.
- Integrated colorama for clean, color-coded UX.
- Added features like clearing the screen, CSV export, summary dashboard.

### 🌐 Phase 3: Web UI with Streamlit

- Created app.py using **Streamlit**.
- Each operation (create customer, deposit, export) got a dedicated sidebar option.
- Live form validation, success messages, and data tables.
- Included real-time transaction viewing and CSV export.

---

## 🛠️ Tech Stack

| Layer        | Tech Used     |
|--------------|---------------|
| Frontend     | Streamlit (Python) |
| Backend      | Python         |
| Database     | SQLite         |
| CLI Features | colorama, os |
| Versioning   | Git & GitHub   |

---

## 🧑‍💻 How to Run the Project

### 🔹 Option 1: Streamlit UI
pip install streamlit
streamlit run app.py

Option 2: Command-Line Interface (CLI)
python main.py

# Project Structure.
├── app.py                # Streamlit UI
├── main.py               # Command-Line Interface
├── customer.py           # Customer logic
├── account.py            # Account logic
├── transaction.py        # Transactions logic
├── db.py                 # Database connection
├── schema.sql            # Optional schema
├── bank.db               # SQLite DB
├── transactions.csv      # Exported CSV
├── README.md             # Project overview
├── assets/               # Image assets
│   └── Streamlit_ui.png
└── __pycache__/          # Compiled files
