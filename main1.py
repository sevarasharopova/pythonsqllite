import sqlite3 as sql
boglanish = sql.connect("odam.db")

malumot = boglanish.cursor()

malumot.execute("""
CREATE TABLE IF NOT EXISTS Student(
    ism TEXT,
    familiya TEXT,
    yonalish TEXT,
    kurs INTEGER

)

""")

malumot.execute("""
CREATE TABLE IF NOT EXISTS Programist(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER,
    dastur TEXT

)

""")

malumot.execute("""
CREATE TABLE IF NOT EXISTS Bekorchi(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER,
    turi TEXT

)
""")

malumot.execute("""
CREATE TABLE IF NOT EXISTS Teacher(
    ism TEXT,
    familiya TEXT,
    toifa TEXT,
    fan TEXT
)

""")

malumot.execute("""
CREATE TABLE IF NOT EXISTS Mexanik(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER,
    mashina TEXT
)
""")

