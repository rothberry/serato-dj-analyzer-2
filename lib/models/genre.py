from lib.models.db_init import db


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)

    def __repr__(self): return f'''id: {self.id} / name: {self.name}'''


print("genre")
