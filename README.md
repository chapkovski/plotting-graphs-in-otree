# an example of dynamic network graph in oTree

There are three different apps for demonstration how the network information can be received from a participant
and used later in oTree pages and stored in a database.

For plotting data the Cytoscape   plugin (http://js.cytoscape.org/) is used.

## Collecting network info from individual player
### _App_:`networx_individual`

Mostly for demonstration: we ask a player to provide information about possible ties over the set of names.
The resulting network is built in a real time, and then stored in a player's field `network_data` in json format,
readable by Cytoscape.

## Collecting network info based on personal links from a set of players
### _App_:`networx`

Here we store the information about individual links in boolean fields created for each 
individual player. So for set of _N_ names we create _N_ fields with corresponding names.
Later on when people make their choices who they count as their friends, we loop through all fields
to create a network data. The full network info is later stored in a group variable `network_data`.

It is pretty compact method but as the network size grows 
it becomes highly inefficient and the data is difficult to analyze.

## Personal links in custom models
### _App_:`networx_custom`

In order to avoid the limitations of previous approach, in this app the data about network links are stored
in custom model where each player has a set of records about his/her individual connections.  The output 
for final player is the same as in `networx` but no individual fields are required in Player's model.
