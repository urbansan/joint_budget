from joint_budget.domain.user import User
from joint_budget.domain.budget import Budget
from joint_budget.domain.transfer import Transfer
import datetime


def prepare_user1():
    user = User("Zigi")
    transfers = {
        Transfer(
            datetime.date(2021, 8, 29),
            100,
            "PLN",
            "dummy transfer1",
            "1010",
            "1011",
            "qwer1",
        ),
        Transfer(
            datetime.date(2021, 8, 23),
            200,
            "PLN",
            "dummy transfer2",
            "2010",
            "2011",
            "qwer2",
        ),
        Transfer(
            datetime.date(2021, 8, 12),
            300,
            "PLN",
            "dummy transfer3",
            "3010",
            "3011",
            "qwer3",
        ),
    }
    user.add_transfers(transfers)


def prepare_user2():
    user = User("Bigi")
    transfers = {
        Transfer(
            datetime.date(2021, 7, 29),
            100,
            "PLN",
            "dummy transfer1",
            "1010",
            "1011",
            "qwer1",
        ),
        Transfer(
            datetime.date(2021, 7, 23),
            200,
            "PLN",
            "dummy transfer2",
            "2010",
            "2011",
            "qwer2",
        ),
        Transfer(
            datetime.date(2021, 7, 12),
            300,
            "PLN",
            "dummy transfer3",
            "3010",
            "3011",
            "qwer3",
        ),
    }
    user.add_transfers(transfers)


def test_create_common_budget():
    user1 = prepare_user1()
    user2 = prepare_user2()


    budget = Budget()

    budget.add_user()