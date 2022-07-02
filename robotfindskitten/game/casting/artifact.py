from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    """The responsibility of the artifact is to come in contact with the Actor or cursor"""
    message = None
    """Attributes:
        actor(Actor): the actor or group in which to inherit from
        group(String): Name of group"""

    def __init__(self):
        "constructs an artifact that is inherited from an Actor."
        #self.add_artifact={}
        #self.get_all_actors=
        
    def set_message(self, message):
        self.message = message

    def get_message(self):
        return self.message



    
