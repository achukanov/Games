from models.models import User
from sqladmin import Admin, ModelView


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name, User.email, User.created_date, User.last_login, User.url_profile_image,
                   User.is_active]


def create_admin(app, engine):
    admin = Admin(app, engine)
    admin.add_view(UserAdmin)
