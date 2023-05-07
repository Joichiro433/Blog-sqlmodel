from sqlmodel import Session, create_engine, select
from rich import print

from models.hero import Hero
from models.team import Team
import settings


engine = create_engine(settings.DB_URL, echo=True)


def exec_query():
    with Session(engine) as session:
        print('Query all rows from the Hero table')
        query = select(Hero)
        result = session.exec(query)
        print(result.all())

        print('Query the Hero table for a specific row with id = 1')
        query = select(Hero).where(Hero.id == 1)
        result = session.exec(query)
        hero = result.one()
        print(hero)
        print(hero.team)

        print('Query all rows from the Team table')
        query = select(Team)
        result = session.exec(query)
        print(result.all())

        print('Query the Team table for a specific row with id = 2')
        query = select(Team).where(Team.id == 2)
        result = session.exec(query)
        team = result.one()
        print(team)
        print(team.heroes)


if __name__ == '__main__':
    exec_query()
