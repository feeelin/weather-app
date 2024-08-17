from pydantic import BaseModel
import json


def read_input_json(filename: str) -> dict:
    with open(file=filename, encoding="UTF-8") as file:
        output = json.load(file)
    return output


class Wind(BaseModel):
    wind: dict

    def get_wind(self):
        return self.wind


if __name__ == "__main__":
    example_data = read_input_json('data.json')
    wind = Wind(**example_data)
    print(wind)
