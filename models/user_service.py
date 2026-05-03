# services/user_service.py
from models.user import User
from models.base import BaseModel
from flask import flash

class UserService:
    
    @staticmethod
    def create_user(username, role):
        """Create a new user with validation"""
        if User.query.filter_by(username=username).first():
            flash("Username already taken!")
            return None
        
        new_user = User(username=username, role=role)
        new_user.save_to_db()
        flash("Profile created successfully! Please log in.")
        return new_user
    
    @staticmethod
    def authenticate_user(username):
        """Authenticate user by username"""
        user = User.query.filter_by(username=username).first()
        if not user:
            flash("Username not found!")
            return None
        return user
    
    @staticmethod
    def get_user_profile(user_id):
        """Get user profile data"""
        user = User.get_by_id(user_id)
        if not user:
            return None
        
        total_likes = sum(len(post.likes) for post in user.posts)
        total_comments = sum(len(post.comments) for post in user.posts)

        return {
            'username': user.username,
            'role': user.role,
            'bio': user.bio,
            'posts': [post.to_feed_dict() for post in user.posts],
            'post_count': len(user.posts),
            'total_likes': total_likes,
            'total_comments': total_comments,
            'member_since': user.created_at
        }
    
    @staticmethod
    def update_user_role(user_id, new_role):
        """Update user's role"""
        user = User.get_by_id(user_id)
        if user:
            user.update(role=new_role)
            return True
        return False