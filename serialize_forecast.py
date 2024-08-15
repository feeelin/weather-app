from pydantic import BaseModel
import json


def read_input_json(filename: str) -> dict:
    with open(file=filename, encoding="UTF-8") as file:
        output = json.load(file)
    return output


class Main(BaseModel):
    weather: list

class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str


if __name__ == "__main__":
    example_data = read_input_json('data.json')
    test = Main(**example_data)
    print(test)