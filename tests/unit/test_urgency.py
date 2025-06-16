import pytest
import sys
sys.path.append('../../tinytroupe/')
sys.path.append('../../')
sys.path.append('..')

from tinytroupe.examples import create_oscar_the_architect
from tinytroupe.environment import TinyWorld
from testing_utils import *


def test_mention_triggers_action(setup):
    agent = create_oscar_the_architect()
    world = TinyWorld("Test", [agent])
    world.broadcast(f"Oi {agent.name}, tudo bem?")
    actions_over_time = world.run(1, return_actions=True)
    actions = actions_over_time[0][agent.name]
    assert contains_action_type(actions, "TALK"), "O agente deveria agir quando mencionado."


def test_irrelevant_message_skips_action(setup):
    agent = create_oscar_the_architect()
    world = TinyWorld("Test", [agent])
    world.broadcast("Hoje o tempo está ótimo para futebol.")
    actions_over_time = world.run(1, return_actions=True)
    actions = actions_over_time[0][agent.name]
    assert actions == [], "O agente não deveria agir em mensagem irrelevante."
