from users.models import Users


async def in_database(user_id: int):

    try:
        await Users.objects.aget(user_id=user_id)
        return True

    except Users.DoesNotExist:
        return False
