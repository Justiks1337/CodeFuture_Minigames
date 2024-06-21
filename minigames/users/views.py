import os

from adrf.decorators import api_view
from asgiref.sync import sync_to_async
from rest_framework.request import Request
from rest_framework.response import Response

from users.utils import in_database
from users.models import Users
from common.utils import authorization


@api_view(['GET'])
@authorization
async def new_user(request: Request, **kwargs):
    user_id = await sync_to_async(request.query_params.get)("user_id")

    if await in_database(user_id):
        return Response({"in_database": True})

    username = await sync_to_async(request.query_params.get)("username")

    user = Users(user_id=user_id, username=username)
    await user.asave()

    return Response({"in_database": False})


@api_view(['POST'])
@authorization
async def download_avatar(request: Request):
    file = request.FILES["file"]
    file_name = request.query_params.get("file_name")
    with open(os.path.join(os.getenv("PATH_TO_AVATARS"), file_name), "wb") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return Response({"status": 200})
