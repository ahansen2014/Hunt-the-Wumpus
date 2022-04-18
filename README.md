# Hunt-the-Wumpus
Versions of Greg Yob's 1972 text adventure.  Used as teaching aids for my programming classes.

Hunt the Wumpus was originally written by Gregory Yob in BASIC while attending the Dartmouth campus of the University of Massachusetts in 1972 or 1973.  Out of frustration with all the grid-based hunting games he had seen, such as Snark, Mugwump and Hurkle, Yob decided to create a map-based game.  Hunt the Wumpus was first published in the People's Computer Company journal Vol. 2, No. 1 in mid 1973, and again in Creative Computing in its October, 1975 issue.  This article was later reprinted in the book The Best of Creative Compting, Volume 1.  Yob later developed Wumpus 2 and Wumpus 3 which offered more hazards and other cave layouts.
(Wikipedia, July 2015)

Rather than play on a grid or cube, Yob used a dodecahedron for the cave system.  A dodecahedron is a twelve sided platonic solid.  It has hexagonal faces and twenty vertices or corners.  Each vertex is joined to three neightbouring vertices.

![image](https://user-images.githubusercontent.com/8213325/163767517-5d2f5d4e-0c1d-4e8b-9b58-866987fe4d0a.png)
![image](https://user-images.githubusercontent.com/8213325/163767575-4f70f9ad-c285-4b52-9893-7b45a6547919.png)

The caves contain some hazards.  One cave contains the Wumpus.  If the player enters the Wumpus cave the Wumpus will eat the player and the player will die.  Two caves contain bottomless pits and if the player falls down these then they die.  Lastly, two caves contain giant bats.  If the player goes into these caves the giant bats will carry them to a random cave in the system, which could be the Wumpus cave or a pit cave.

There are some warnings though.  If the player’s current cave neighbours the Wumpus cave they will smell the Wumpus because Wumpuses smell terrible.  If they are in a cave the neighbours a pit cave they will feel a cold breeze coming up from the cave and if the cave neighbours a bat cave they will hear the flapping of wings.
The players goal is to kill the Wumpus with an arrow so the player can shoot into a neighbouring cave and if the Wumpus is in there they will kill it and win.  This is a bit different to the original version which used a “crooked” arrow that could fly through up to five caves.  This application will have a simple one cave arrow to keep the code simple.

