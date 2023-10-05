from models import User


def get_permissions(user: User):
    """
    Function that return the permissions of the user

    is_superuser : has all permissions

    is_manager has permissions to :
        - create and update users ( #NOTE even self ?)
        - create and update any contract
        - filter event dashboard
        - add a support to an event ( #NOTE can he update the event ?)

    is_commercial has permissions to :
        - create and update his clients
        - create and update his clients's contracts
        - filtering contract dashboard
        - create an event for a client that has signed a contract

    is_support has permissions to :
        - filter event dashboard ( #NOTE only his events ?)
        - update his events

    """
    print(user.__dict__)

    if user.is_superuser:
        return "superuser"
    elif user.is_manager:
        return "manager"
    elif user.is_commercial:
        return "commercial"
    elif user.is_support:
        return "support"
    else:
        # TODO add exception
        return "user"
