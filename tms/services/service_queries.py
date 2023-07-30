from sqlalchemy import func, update

from models.models import Idea, User


def get_how_many_ideas_users_have():
    """
        Вычислить сколько у каждого пользователя идей
    """
    return db.session.query(
        User,
        func.count(Idea.id).label('total_idea')
    ).join(Idea.user).group_by(User).all()


def get_how_max_ideas_users_have():
    """
        У какого пользователя максимальное количество идей
    """
    return db.session.query(
        User,
        func.count().label('total_ideas')
    ).join(Idea.user).group_by(User).order_by(func.count(Idea.id).desc()).first()


def get_ideas_start_with():
    """
        Отфильтровать идеи, в которых есть слово "подставить свое"
    """
    return Idea.query.filter(Idea.activity.ilike("подставить свое%")).all()


def get_users_have_idea():
    """
        Получить пользователей, у которых количество идей больше 5
    """
    return User.query.join(Idea.user).group_by(User).having(func.count(Idea.id) > 5).all()


def update_user_have_idea():
    """
        Обновить имя пользователя с id=1
    """
    update_query = update(User).where(User.id == 1).values(username='XMolotX')
    db.session.execute(update_query)
    db.session.commit()


def delete_idea_where_word():
    """
        Удалить все идеи, в которых есть слово "подставить свое"
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
