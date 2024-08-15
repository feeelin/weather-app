from pydantic import BaseModel
import json


def read_input_json(filename: str) -> dict:
    with open(file=filename, encoding="UTF-8") as file:
        output = json.load(file)
    return output

# with open('data.json', encoding="UTF-8") as f:
#     data = json.load(f)


class Main(BaseModel):
    wind: dict


class Wind(BaseModel):
    speed: float or int
    deg: int or float
    gust: float or int


# wind_data = {'speed': '0.62',
#              'deg': '349',
#              'gust': '1.18'}
#

# wind = Wind(**wind_data)
# print(wind)


if __name__ == "__main__":
    example_data = read_input_json('data.json')
    test = Main(**example_data)
    print(test)
