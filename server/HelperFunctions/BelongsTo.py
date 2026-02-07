from config import db

def belongs_to(
    parent_table,
    nullable = False
):
    return db.Column(
        db.Integer, 
        db.ForeignKey(f"{parent_table}.id"), 
        nullable = nullable
    )