import csv
from io import StringIO

from flask import send_file

from app import app
from app.models import CVSData
from app.models.UserModel import User
from app.responseBuilder import response_ok
from db.queries.users import users_count

#TODO: я запутался в cvs файлике хахахах
@app.route('api/get_cvs/', methods=['GET'])
async def get_cvs_data() -> CVSData:

    users = await users_count()

    column_names = [column.name for column in User.__table__.columns]

    csv_data = StringIO()

    csv_writer = csv.writer(csv_data)

    for user in users:
        csv_writer.writerow([
            user["user_id"],
            user["fio"].upper(),
            user["email"].lower(),
            user["city"],
            user["school"],
            "Finished" if user["is_finished"] else "Not Finished",
            user["type_mk"]
        ])

    csv_data.seek(0)
    temp_csv_file = StringIO(csv_data.getvalue())
    temp_csv_file.seek(0)

    result = send_file(temp_csv_file, mimetype='text/csv', download_name='user_data.csv', as_attachment=True)

    temp_csv_file.close()

    return CVSData(**response_ok(result))


