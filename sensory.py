# Create a sensory object based on the human senses and (for another file) the ability to perceive the world.
# by @nissmogt "Names matter"
#
import logic as lgc


class Sensory:
    def __init__(self, senses):
        self.senses = senses

    def perceive(self, world):
        # Perceive the world using the senses
        # load a perception model from huggingface

        # call a function that returns perception
        # perception = ps.perceptual_space.perceive(world, self.senses)
        perception = 3
        return perception


