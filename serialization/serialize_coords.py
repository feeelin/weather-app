from pydantic import BaseModel

class Coord(BaseModel):
coord: str
lon = coord['lon']
lat = coord['lat']

coord = Coord(coord='coord')
print(coord.coord)
print(coord.lon)
print(coord.lat)
