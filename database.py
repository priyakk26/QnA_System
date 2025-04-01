import sqlite3
import os

DB_PATH = os.path.join(os.getcwd(), "qna_db.sqlite3")  # Path to SQLite DB file

def connect_db():
    """Connect to SQLite3 Database"""
    return sqlite3.connect(DB_PATH)

def create_table():
    """Create the QnA table if it doesn't exist"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS qna (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_qna():
    """Insert some default QnA data"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO qna (question, answer) VALUES (?, ?)
    ''', [
        ("What is AI?", "AI stands for Artificial Intelligence, which enables machines to mimic human intelligence."),
        ("What is LangChain?", "LangChain is a framework for building applications powered by language models."),
        ("What is Machine Learning?", "Machine Learning is a subset of AI that enables computers to learn from data and improve their performance without being explicitly programmed."),
        ("What is NLP?", "NLP (Natural Language Processing) is a branch of AI that helps computers understand, interpret, and generate human language."),
        ("What is a Large Language Model?", "A Large Language Model (LLM) is an AI model trained on vast amounts of text data to generate human-like text responses."),
        ("What is OpenAI?", "OpenAI is an AI research company that develops advanced language models like GPT-4o."),
        ("What is FastAPI?", "FastAPI is a modern web framework for building APIs with Python, known for its speed and efficiency."),
        ("What is SQLite?", "SQLite is a lightweight, self-contained database engine that does not require a separate server."),
        ("What is SQL?", "SQL (Structured Query Language) is used to manage and query relational databases."),
        ("What is Python?", "Python is a popular programming language known for its simplicity, versatility, and strong AI/ML ecosystem."),
        ("What is a chatbot?", "A chatbot is an AI-powered software that interacts with users through text or voice."),
        ("What is the difference between AI and ML?", "AI is a broad field that enables machines to mimic human intelligence, while ML is a subset of AI that focuses on learning from data."),
        ("What is an API?", "An API (Application Programming Interface) allows different software systems to communicate with each other."),
        ("What is OpenAI GPT-4o?", "GPT-4o is OpenAI's latest language model, optimized for faster responses and improved reasoning capabilities."),
        ("What is the use of LangChain in AI?", "LangChain helps developers integrate Large Language Models (LLMs) into applications by providing structured tools and workflows.")
    ])
    conn.commit()
    conn.close()

def fetch_qna():
    """Fetch all QnA pairs from SQLite"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM qna")
    qna_data = [{"id": row[0], "question": row[1], "answer": row[2]} for row in cursor.fetchall()]
    conn.close()
    return qna_data

# Create table and insert data (only needs to be run once)
create_table()
insert_qna()