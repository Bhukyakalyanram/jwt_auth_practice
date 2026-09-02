from flask import Flask, request

from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    JWTManager,
)

app = Flask(__name__)

database = [
    {"email": "Kalyan@gmail.com", "password": 123456789},
    {"email": "Kalyan2@gmail.com", "password": 1234567890},
]


app.config["JWT_SECRET_KEY"] = "kalyan ram"
jwt = JWTManager(app)


@app.post("/login")
def handle_login():
    email = request.json.get("email")
    password = request.json.get("password")

    items = list(
        filter(
            lambda x: x["email"] == email and x["password"] == int(password), database
        )
    )
    if items:
        access_token = create_access_token(identity=email)
        return {
            "data": "some important data",
            "access-token": access_token,
            "success": True,
            "status": 200,
        }
    else:
        return {"data": "Invalid credentials", "success": False, "status": 400}


@app.get("/safe")
@jwt_required()
def handle_safe():
    email = get_jwt_identity()
    return {"email": email}


@app.get("/test")
def handle_test():
    return "working"


if __name__ == "__main__":
    app.run(debug=True)
