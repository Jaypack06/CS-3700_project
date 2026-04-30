from models.database import db
from models.base import BaseModel
from datetime import datetime, timedelta  

class User(BaseModel):
    __tablename__ = 'users' 
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(50))
    posts = db.relationship('Post', back_populates='user')
    
    def __init__(self, username, role):
        self.username = username
        self.role = role


    def __repr__(self):
        return f'<User {self.username}>'
    
    def get_streak(self):
        """Calculates how many consecutive days the user has posted"""
        if not self.posts:
            return 0
        
        #getting dates of all posts by user
        posted_dates = {post.created_at.date() for post in self.posts}
        today = datetime.utcnow().date()
        streak = 0
        current_day = today
        
        #checks if user has posted today, if not then check for yesterday and so on until we find a day where user has not posted
        if today not in posted_dates:
            current_day = today - timedelta(days=1)

        while current_day in posted_dates:
            streak += 1
            current_day -= timedelta(days=1)
            
        return streak


    # One idea to use encapsulation for is protecting data by preventing long bios. New function inside user class that checks length of bio.    
