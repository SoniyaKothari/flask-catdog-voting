from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
DB = "votes.db"

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS votes (animal TEXT PRIMARY KEY, count INTEGER NOT NULL)")
    for animal in ["cat", "dog"]:
        cur.execute("INSERT OR IGNORE INTO votes (animal, count) VALUES (?, 0)", (animal,))
    conn.commit()
    conn.close()

def add_vote(animal):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("UPDATE votes SET count = count + 1 WHERE animal = ?", (animal,))
    conn.commit()
    conn.close()

def get_votes():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT animal, count FROM votes")
    data = dict(cur.fetchall())
    total = data.get("cat", 0) + data.get("dog", 0)
    cat_percent = int((data.get("cat", 0) / total) * 100) if total > 0 else 0
    dog_percent = 100 - cat_percent if total > 0 else 0
    conn.close()
    return cat_percent, dog_percent, data.get("cat", 0), data.get("dog", 0)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        animal = request.form.get("animal")
        if animal in ["cat", "dog"]:
            add_vote(animal)
    cat_percent, dog_percent, cat_votes, dog_votes = get_votes()
    return render_template("index.html", cat_percent=cat_percent, dog_percent=dog_percent,
                           cat_votes=cat_votes, dog_votes=dog_votes)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
