import artist
import genre
from lib.models.db_init import db
from ipdb import set_trace

print("MAIN")

# set_trace()


class Playlist(db.Model):
    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f"Name: {self.name}"
