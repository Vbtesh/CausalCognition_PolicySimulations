# PolicySimulations

Basic simulations of policy decision making in a given setting.

Examples:
    - Crime fighting
    - Health policy

CRIME FIGHTING

PURPUSE:
    - Fight crime and manage population satisfaction in a city by making policy choices. 
    - The game is implemented through a turn based resource allocation paradigm
    - The aim is to minimise crime while maximising satisfaction

GAME LOOP:
    - Initial situation => map of city with patches of red to indicate crime intensity
    - (Advice given (or not) => advisor provides a recommended split of resources OR a estimation of the result of the policy choice)
    - Player decision => allocate resources between actions 1 to 3
    - Resulting situation (feedback loop)

VARIABLE ADJUSTEMENT ORDER (over a turn):
    - Begin Phase: no change, presents output of last turn's calculations
    - Decision Phase: no change, retrieve player input for resource allocation
    - Increment phase: apply the change resulting from player choice:
        Order: Repress, support then surveil
    - Compute phase: compute new values for next turn from new variable values 

OUTCOMES:
    Population Satisfaction / Happiness (PopSat): Positive Social Impact => 1 to 100
        - Dimension 1: current level => 1 to 100 (1 is min satisfaction and 100 is maximum satisfaction)
        - Dimension 2: changing rate => 1.0 to ?? (is negatively correlated to Crime changing rate)
            Logic: safety and livelyhood in a neighbourhood decrease when crime is high

    Criminality Rate (Crime): Indicator of policy efficiency 
        - Dimension 1: current level => 1 to 100 (1 is almost no crime and 100 is maximum crime)
        - Dimension 2: changing rate => 1.0 to ?? (1.0 is no growth)
            Logic: crime increases on its own if nothing is done to fight it due to criminal groups becoming more and more powerful and having access to more resources
        

ALLOCATIONS => 100 "resource" points to allocate in a chosen split between the three policy measures
    1. Repress: Armed police is sent to location to catch criminals by all means necessary
        - Strongly reduces Crime but increases its growing rate (e.g. 1 Repress = -1 Crime and +0.01 Crime rate)
            => Logic: armed forces catch criminals but leave the field free for new one to take over
        - Strongly reduces PopSat (e.g. 1 Repress = -1 PopSat)
            => Logic: having armed forces roaming the street is not a pleasant living condition 

    2. Surveil: Send police to patrol the area to generate presence and gather information
        - Moderately decreases Crime and its growing rate (e.g. 1 Surveil = -0.5 Crime and -0.005 Crime rate)
            => Logic: detters petty criminals from acting out and information gathered allows the police to prevent future crime
        - Moderately decreases PopSat (e.g. 1 Repress = -0.5 PopSat)
            => Logic: constant police presence is not a pleasant living condition (though not as bad as armed forces)
    
    3. Support: Send funding for local communities (e.g Job support, basic education, etc.)
        - Strongly dampers the growing rate of Crime but no effect on its current level (e.g. 1 Support = -0.01 Crime rate)
            => Logic: new social initiatives don't affect crime but will help future potential criminals to find another path through community support
        - Strongly increases PopSat (e.g. 1 Support = 1 PopSat)
            => Logic: generates local activity and builds up the community's well-being and cohesion