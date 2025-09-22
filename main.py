from fastapi import FastAPI,HTTPException,Response



app=FastAPI()

users_list = []



@app.get("/users")
async def get_all_users():
    if len(users_list) == 0:
        return Response(
        "Not content",
        status_code=204
    )
    return users_list

@app.post("/users/{nome}")
async def add_new_user(nome:str):
   users_list.append(nome)
   return Response(
       "Usuário adicionado com sucesso!",
       status_code=201
   )

@app.get("/user/{id}")
async def get_user_by_id(id:int):
    try:
        return users_list[id]
    except:
        raise HTTPException(404,"User Not Found")
    

@app.delete("/users/{id}")
async def adicionar_usuario(id:int):
    users_list.pop(id)
    Response(200,"Usuário deletado com sucesso!")
  

@app.put("/users")
def atualizar_usuario():
   pass