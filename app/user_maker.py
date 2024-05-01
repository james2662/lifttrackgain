from library.ltgusers.users import LTGUser
from models.usermodels.usermodels import UserCore

LTGUser.user_repo.session.flush()
user = LTGUser.create_user(username='test123', email='james@tunerpreferred.com', password='password123')
#LTGUser.user_repo.session.add(user)
id_for = user.id
LTGUser.user_repo.session.close()
LTGUser.user_repo.new_session(engine_type='sqllite')


user = LTGUser.user_repo.get(model=UserCore, reference=id_for)
if user is None:
    print("User is None")
    LTGUser.user_repo.add(user)
print(f"{user=}")