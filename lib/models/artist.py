from lib.models.db_init import db

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String)

    # created_at = db.Column(db.DateTime, server_default=db.func.now())
    # updated_at = db.Column(
    #     db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self): return f'''id: {self.id} / name: {self.name}'''

print("artist")