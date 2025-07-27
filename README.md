# 🛠️ Interactive Python + MySQL CLI DBMS

A terminal-based Database Management System (DBMS) tool written in **Python 3** with **MySQL Connector**. This CLI application enables full database and table management: create/use/drop databases, handle tables, CRUD operations, structure modification, CSV export, and more.

---

## 🚀 Features

- ✅ User authentication (username/password)
- 🗂️ View, create, select, and drop databases
- 📋 View and describe tables within the current database
- 🛠️ Create, insert, update, delete records
- 🔄 Alter table structure: add, modify, rename, or drop columns
- 📥 Export table data to `.csv` format
- 🧹 Drop tables or the entire database
- 🧩 Robust input validation and error handling

---

## 📌 Menu Overview

- **0** – Database menu: use, create, list, or quit  
- **1** – Show current database  
- **2** – Show all tables  
- **3** – Create a new table  
- **4** – Describe table structure  
- **5** – Insert records into a table  
- **6** – Update records in a table  
- **7** – Alter table schema (add/modify/rename/drop columns)  
- **8** – Display all records in a table  
- **9** – Export table to CSV  
- **10** – Delete rows based on conditions  
- **11** – Drop a table or database  
- **12** – Quit the app  

---

## 🛠️ Technologies & Dependencies

- **Language**: Python 3.x  
- **Database**: MySQL (default database: `loki` unless changed via menu)  
- **Library**: `mysql-connector-python`  
- **CSV Handling**: Python’s built-in `csv` module  

---

## 🧭 Installation & Usage

1. Ensure **MySQL Server** is installed and running.
2. In your terminal, install MySQL Python connector:
   ```bash
   pip install mysql-connector-python
Clone this repository:

bash
Copy
Edit
git clone <your-repo-url>
cd <your-repo-folder>
Run the script:

bash
Copy
Edit
python dbms_cli.py
Follow the on-screen prompts to log in and use the interactive menu.

📁 Example Folder Structure
bash
Copy
Edit
dbms_cli_project/
│
├── dbms_cli.py            # Main script
├── README.md              # This documentation
├── sample_export.csv      # Example CSV output
└── requirements.txt       # Optional dependencies

⚙️ Usage Examples
Create & switch databases: Navigate menu option 0 → create to add a new database automatically switched to.

Export tables: Use option 9 to save table data as a .csv file.

Drop operations: Option 11 allows dropping a selected table or an entire database.

📋 Contributing
Contributions are welcome! Please open an issue or submit a pull request. For significant changes, discuss via an issue first.

❓ Trouble & FAQ
MySQL errors or permission issues: Verify your user credentials and database permissions.

Crash or unexpected termination: Ensure your syntax when entering SQL operations is correct and escape commas/quotes properly.

Missing database or table: Use the database or table menu options to check names and existence.

📜 License
This project is provided for learning and academic purposes. No commercial rights are granted.

🙋‍ Author
Logesh Waran
CSE Student,beginner

Enjoy using this CLI-based DBMS tool!
