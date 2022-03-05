"""Main module"""
{% set mainclass = cookiecutter.project_slug|title %}
from copy import copy

{% if cookiecutter.addon_type == 'db_connection' %}
from pydantic import validate_arguments
from df_engine.core import Context, Actor
from df_engine.core.types import ActorStage


class {{ mainclass }}:
    """{{ mainclass }}"""
    def __init__(self) -> None:
        pass

    def __deepcopy__(self, *args, **kwargs):
        return copy(self)

    @validate_arguments
    def _update_handlers(self, actor: Actor, stage: ActorStage, handler) -> Actor:
        actor.handlers[stage] = actor.handlers.get(stage, []) + [handler]
        return actor

    def update_actor_handlers(self, actor: Actor, *args, **kwargs):
        self._update_handlers(actor, ActorStage.FINISH_TURN, self.handler)

    @validate_arguments
    def handler(self, ctx: Context, actor: Actor, *args, **kwargs) -> None:
        return
{% elif cookiecutter.addon_type == 'messenger_connection' %}
from df_engine.core import Context, Actor

class {{ mainclass }}:
    """{{ mainclass }}"""
    def __init__(self) -> None:
        pass
{% else %}
from df_engine.core import Context, Actor

class {{ mainclass }}:
    """{{ mainclass }}"""
    def __init__(self) -> None:
        pass
{% endif %}


def main():
    """Main module script"""
    return

if __name__ == "__main__":
    main()