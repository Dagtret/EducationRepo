LIST_USERS_DATA_SCHEMA = {
    "type" : "object",
    "properties" : {
        "id": 7,
        "email": "michael.lawson@reqres.in",
        "first_name": "Michael",
            "last_name": "Lawson",
            "avatar":
    }
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