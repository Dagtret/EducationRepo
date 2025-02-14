LIST_USERS_DATA_SCHEMA = {
    "type" : "object",
    "properties" : {
        "id": {"type" : "integer"},
        "email": {"type" : "string"},
        "first_name": {"type" : "string"},
        "last_name": {"type" : "string"},
        "avatar": {"type" : "string"},
    },
    "required" : ["id", "email", "first_name", "last_name", "avatar"]
}

LIST_DATA_SCHEMA = {
    "type" : "object",
    "properties" : {
        "id" : {"type" : "integer"},
        "name" : {"type" : "string"},
        "year" : {"type" : "integer"},
        "color" : {"type" : "string"},
        "pantone_value" :  {"type" : "string"}
    },
    "required" : ["id", "name", "year", "color", "pantone_value"]
}

CREATE_USER_SCHEMA = {
    "type" : "object",
    "properties" : {
        "name" : {"type" : "string"},
        "job" : {"type" : "string"},
        "id" : {"type" : "string"},
        "createdAt" : {"type" : "string"}
    },
    "required" : ["id", "createdAt"]
}

UPDATE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"}
    },
    "required": ["updatedAt"]
}

REGISTER_USER_SCHEMA_SUCCESSFUL = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "token": {"type": "string"}
    },
    "required": ["id", "token"]
}

LOGIN_AND_REGISTER_USER_SCHEMA_UNSUCCESSFUL = {
    "type": "object",
    "properties": {
        "error": {"type": "string"}
    },
    "required": ['error']
}

LOGIN_USER_SCHEMA_SUCCESSFUL = {
    "type": "object",
    "properties": {
        "token": {"type": "string"}
    },
    "required": ["token"]
}