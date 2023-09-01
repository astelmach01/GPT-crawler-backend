from app.web.api.tasks.core import create_reminder

function_names = {
    "create_reminder": create_reminder,
}


function_descriptions = [
    {
        "name": "create_reminder",
        "description": "This function handles the logic for creating a reminder for a "
        "generic task at a given date and time for a specific user. ",
        "parameters": {
            "type": "object",
            "properties": {
                "task": {
                    "type": "string",
                    "description": "The task to be reminded of, such as 'clean the "
                    "house'",
                },
                "date": {
                    "type": "datetime.datetime",
                    "description": "The date and time to be reminded at as a datetime "
                    "in the format %Y-%m-%d %H:%M:%S, such as "
                    "'2021-08-01 12:00:00'",
                },
                "user_id": {
                    "type": "integer",
                    "description": "The user_id of the user to be reminded, such as "
                    "1. Keep as 2 for testing purposes.",
                },
                "required": ["task", "date", "user_id"],
            },
        },
    },
]