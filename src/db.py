
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine


class Movies(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    genre: str
    sensitive: Optional[bool] = False


movie_1 = Movies(name="Fight Club", genre="Thriller",sensitive=True)
print(movie_1)

engine = create_engine("postgresql://postgres:root@localhost:5432/seniority-management", echo=True)


SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.get(Movies, ident=True )