from sqlmodel import Session, SQLModel, create_engine

from models.hero import Hero
from models.team import Team
import settings


engine = create_engine(settings.DB_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    with Session(engine) as session:
        team_preventers = Team(name='Preventers', headquarters='Sharp Tower')
        team_z_force = Team(name='Z-Force', headquarters="Sister Margaret's Bar")

        hero_deadpond = Hero(name='Deadpond', secret_name='Dive Wilson', team=team_z_force)
        hero_rusty_man = Hero(name='Rusty-Man', secret_name='Tommy Sharp', age=48, team=team_preventers)
        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.commit()

        session.refresh(team_preventers)
        session.refresh(team_z_force)
        session.refresh(hero_deadpond)
        session.refresh(hero_rusty_man)

        print(f'Created team: {team_preventers}')
        print(f'Created team: {team_z_force}')
        print(f'Created hero: {hero_deadpond}')
        print(f'Created hero: {hero_rusty_man}')


if __name__ == '__main__':
    create_db_and_tables()
    create_heroes()
