import abc


class AbstractPersistencePort(abc.ABC):
    def get_all_records(self):
        ...

    def get_records(self, user_id):
        ...

    def get_all_users(self):
        ...

    def get_user(self, user_id):
        ...

    def get_all_budgets(self):
        ...

    def get_budget(self, budget_id):
        ...
