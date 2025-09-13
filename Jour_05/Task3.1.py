# Task 3.1

student = {}

student["player"] = 12
student["team"] = 20
# print(student)


# Task 3.2

superheroes = {
    "Batman": {
        " id ": 1,
        " aliases ": [" Bruce Wayne ", " Dark knight "],
        " location ": {
            " number ": 1007,
            " street ": " Mountain Drive ",
            " city ": " Gotham ",
        },
    },
    "Superman": {
        "id": 2,
        " aliases ": [" Kal - El ", " Clark Kent ", " The Man of Steel "],
        "location": {
            " number ": 344,
            " street ": " Clinton Street ",
            " apartment ": "3D",
            "city": "Metropolis",
        },
    },
}
x = superheroes["Superman"]["location"]["city"]
print(x)
