from adapters.outbound.database.models.user import User as UserSchema
from domain.entities.user import User
from api.domain.repositories.IUserRepository import IUserRepository
from django.core.exceptions import ObjectDoesNotExist


# Concrete implementation for User Repository
class UserRepository(IUserRepository):
    def create(self, user: User) -> User:
        return self.schemaToUser(
            User.objects.create(
                name=user.name,
                email=user.email,
                password=user.password,
            )
        )

    def update(self, id, newUser: User) -> bool:
        try:
            User.objects.filter(id=id).update(
                name=newUser.name,
                email=newUser.email,
                password=newUser.password,
                groups=newUser.groups,
            )
            return True
        except ObjectDoesNotExist:
            return False

    def delete(self, id) -> bool:
        try:
            User.objects.filter(id=id).delete()
            return True
        except ObjectDoesNotExist:
            return False

    def findById(self, id) -> User:
        try:
            return self.schemaToUser(User.objects.get(id=id))
        except ObjectDoesNotExist:
            return None

    def findAll(self, skip, limit) -> list[User]:
        return map(self.schemaToUser, User.objects.all()[skip:limit])

    def schemaToUser(schema: UserSchema) -> User:
        return User(
            schema.id,
            schema.name,
            schema.email,
            schema.password,
            schema.created_at,
            [group.id for group in schema.groups.all()],
        )
