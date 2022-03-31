from fastapi import FastAPI, HTTPException

api = FastAPI(
    title="Mon API pour les NOV21CDE",
    version="0.1"
)


@api.get('/')
def get_index():
    return {
        "Hello": "World"
    }


@api.get('/health')
def get_health():
    return {
        "status": 1
    }


@api.post('/health')
def post_health():
    return {
        "status": 1,
        "comment": "ceci est une requete POST"
    }


@api.get('/objects',
         tags=["default", "objects"],
         responses={
             200: {
                 "description": "Objet retourné correctement"
             },
             404: {
                 "description": "L'objet demandé n'existe pas!"
             }
         })
def get_object(object_id: int):
    """Returns an object identified by the object_id
    """
    if object_id > 500:
        raise HTTPException(
            status_code=404,
            detail=f"Object with '{object_id}' id does not exist")
    return {
        "status": 1,
        "object_id": object_id
    }


@api.get('/users')
def get_users():
    return {
        "status": 1,
        "users": [
            {
                "name": "Paul"
            },
            {
                "name": "Lara"
            }
        ]
    }
