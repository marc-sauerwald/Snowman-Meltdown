"""
ASCII art stages for the Snowman Meltdown game.

This module contains the visual representations of the snowman
at various stages of melting, from fully intact to completely melted.
"""

# Snowman ASCII Art stages (7 stages for smoother melting)
# Index 0 = full snowman, Index 6 = completely melted
STAGES = [
    # Stage 0: Full snowman
    """
       _===_
      / o o \\
     (   "   )
      \\_____/
     /|     |\\
    / |     | \\
      |     |
     _|     |_
    (_|_____|_)
    """,
    # Stage 1: Starting to melt slightly
    """
       _===_
      / o o \\
     (   "   )
      \\_____/
     /|     |\\
    / |     | \\
      |     |
     _|_____|_
    """,
    # Stage 2: Arms drooping
    """
       _===_
      / o o \\
     (   "   )
      \\_____/
      /|   |\\
      |     |
     _|_____|_
    """,
    # Stage 3: Body shrinking
    """
       _===_
      / o o \\
     (   "   )
      \\_____/
       |   |
      _|___|_
    """,
    # Stage 4: Lower body gone
    """
       _===_
      / o o \\
     (   "   )
      \\_____/
       ~~~~~
    """,
    # Stage 5: Only head remains
    """
       _===_
      / o o \\
     (   "   )
      ~~~~~~~
    """,
    # Stage 6: Completely melted - just a puddle
    """

      ~~~~~~~
     ~~~~~~~~~
      ~~~~~~~

    [RIP Snowman]
    """
]
