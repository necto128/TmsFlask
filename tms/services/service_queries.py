from sqlalchemy import func, update

from models.models import Idea, User


def get_how_many_ideas_users_have():
    """
        Calculate how many ideas each user has
    """
    return db.session.query(
        User,
        func.count(Idea.id).label('total_idea')
    ).join(Idea.user).group_by(User).all()


def get_how_max_ideas_users_have():
    """
        Which user has the maximum number of ideas
    """
    return db.session.query(
        User,
        func.count().label('total_ideas')
    ).join(Idea.user).group_by(User).order_by(func.count(Idea.id).desc()).first()


def get_ideas_start_with():
    """
        Filter out ideas that have the word  "подставить свое"
    """
    return Idea.query.filter(Idea.activity.ilike("подставить свое%")).all()


def get_users_have_idea():
    """
        Get users who have more than 5 ideas
    """
    return User.query.join(Idea.user).group_by(User).having(func.count(Idea.id) > 5).all()


def update_user_have_idea():
    """
        Update user name with id=1
    """
    update_query = update(User).where(User.id == 1).values(username='XMolotX')
    db.session.execute(update_query)
    db.session.commit()


def delete_idea_where_word():
    """
        Delete all ideas that have the word "подставить свое"
    """
    ideas_to_delete = Idea.query.filter(Idea.type.icontains("подставить свое")).all()
    for idea in ideas_to_delete:
        db.session.delete(idea)
    db.session.commit()


if __name__ == "__main__":
    from app import app, db

    with app.app_context():
        result = delete_idea_where_word()
        print(result)
