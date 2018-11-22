from abc import ABC, abstractmethod


# Class Definitions
class User:
    def __init__(self, name, roles, password="changeme"):
        self.name = name
        self.password = password
        self.roles = roles

    def add_role(self, role):
        self.roles.append(role)

    def __repr__(self):
        return repr(("User = {}".format(self.name),
                     "Password = {}".format(self.password),
                     "Roles = {}".format(self.roles)))


class Employee(User):
    def __init__(self, fullname):
        super().__init__(fullname, ['employee'], Employee.construct_user_name(fullname))
        self.fullname = fullname

    @staticmethod
    def construct_user_name(full_name):
        return full_name.lower().replace(' ', '')

    def __repr__(self):
        return repr(f"Name = {self.fullname}, Roles = {self.roles}")


class Repository(ABC):
    @abstractmethod
    def create(self, entity):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity):
        pass


class InMemoryRepository(Repository):

    def __init__(self):
        self.data = []

    def create(self, entity):
        self.data.append(entity)

    def read_all(self):
        return self.data.copy();

    def update(self, entity):
        self.data.remove(entity)

    def delete(self, entity):
        print(f"Deleting {entity}")
        self.data.remove(entity)


# Main
users = User('Muhammad', []), Employee('Muhammad Aathif')
users[0].add_role('admin')
user_repository = InMemoryRepository()
print("Adding users to repository")
for user in users:
    user_repository.create(user)
print(f"Users in repository: {user_repository.read_all()}")
user_repository.delete(users[0])
print(f"Users in repository: {user_repository.read_all()}")
