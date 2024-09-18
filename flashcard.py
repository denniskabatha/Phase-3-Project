import sqlite3

def add_card(question, answer):
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO flashcards (question, answer) VALUES (?, ?)', (question, answer))
    conn.commit()
    conn.close()

def view_cards():
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM flashcards')
    cards = cursor.fetchall()
    conn.close()
    return cards

def delete_card(card_id):
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM flashcards WHERE id = ?', (card_id,))
    conn.commit()
    conn.close()

def update_card(card_id, question, answer):
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE flashcards SET question = ?, answer = ? WHERE id = ?', (question, answer, card_id))
    conn.commit()
    conn.close()

def get_progress():
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM flashcards')
    total = cursor.fetchone()[0]
    cursor.execute('SELECT SUM(correct_count) FROM flashcards')
    correct = cursor.fetchone()[0] or 0
    conn.close()
    return total, correct
