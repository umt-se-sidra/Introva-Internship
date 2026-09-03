import asyncio

import httpx

from dataclasses import dataclass
@dataclass
class APIResult:
    source: str
    id: int
    name: str

url1="https://jsonplaceholder.typicode.com/todos/1"

url2 ="https://jsonplaceholder.typicode.com/users/1"

async def get_todo():

    async with httpx.AsyncClient() as client:

        response= await client.get(url1)

        data= response.json()

        return data

async def get_user():

    async with httpx.AsyncClient() as client:

        response= await client.get(url2)

        data= response.json()

        return data

async def main() :

    result1,result2= await asyncio.gather(

        get_todo(),

        get_user()

    )

    todo_result=APIResult( 
       source="todo", 
       id=result1["id"], 
       name=result1["name"]
       )
    user_result=APIResult(
        source="user", 
        id=result2["id"], 
        name=result2["name"] 
        )
    print(todo_result) 
    print(user_result)

asyncio.run(main())  
