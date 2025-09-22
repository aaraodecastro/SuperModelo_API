
from fastapi import FastAPI,HTTPException,Response

from fastapi.responses import HTMLResponse

app = FastAPI()

users_list = []

@app.get("/users",status_code=200)
async def get_all_users():
    if len(users_list) == 0:
        return Response(
            "Not Content",
            status_code=204
            )

    return users_list

@app.get("/user/{id}")
async def get_user_by_id(id:int):
    try :
        return users_list[id]
    except:
        raise HTTPException(404,"User Not Found")


@app.post("/users/{nome}")
async def add_new_user(nome:str):
    users_list.append(nome)
    return Response(
        "Usuário adicionado com sucesso!",status_code=201
        )


@app.get("/home")
async def read_root():
    return HTMLResponse("<h1>Olá Mundo!</h1>")


@app.delete("/users/{id}")
async def deletar_usuario(id:int):
    users_list.pop(id)
    Response(200,"Usuário deletado com sucesso!")
    

@app.put("/users")
async def atualizar_usuario():
    pass
