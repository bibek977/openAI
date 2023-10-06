weather_func = [
    {
        'name' : 'get_current_weather',
        "description" : "Get the current weather in the given locaton",
        "parameters" : {
            "type" : "object",
            "properties":{
                "location" : {
                    "type" : "string",
                    "description" : "The city or district like Kathmandu, Pokhara, Hetuada",
                },
                "format" : {
                    "type" : "string",
                    "enum" : ["celcius","farenheit"],
                    "description" : "The temperature unit to use. Infer this from user location.",
                }
            }

        },
        "required" : ["location","format"],
    },
]