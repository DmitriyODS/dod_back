from typing import List, Any, Tuple

from flask import Flask, render_template, request, jsonify, Response, make_response
from flask_mail import Message, Mail
from flask_sqlalchemy import SQLAlchemy

from app import app
from app.models.UserModel import GetUsersCount, GetSelectedUser
from app.responseBuilder import response_ok
from db.queries.users import selected_user, users_count


@app.route('api/users/', methods=['GET'])
async def get_all_users() -> GetUsersCount:
    result = await users_count()

    return GetUsersCount(**response_ok(result))


@app.route('api/user/<int:user_id>', methods=['GET'])
async def get_selected_user(user_id: int) -> GetSelectedUser:
    result = await selected_user(user_id)

    return GetSelectedUser(**response_ok(result))


