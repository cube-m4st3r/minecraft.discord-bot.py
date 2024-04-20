from sqlalchemy.orm import sessionmaker

from classes import World
from database import engine
from utils.render import render_world_full

Session = sessionmaker(bind=engine)
session = Session()

# add new world to db
world = World(name="Test", owner="TestUser")
session.add(world)
session.commit()

from commands.generate import generate_world

# start generate process
generate_world(session=session, world_id=world.id)

# render full world and store it in /test_output
render_world_full(world_id=world.id, session=session)