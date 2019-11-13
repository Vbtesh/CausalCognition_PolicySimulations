from random import randint


class Neighbourhood():

    def __init__(self):
        self.crime = randint(50, 100)
        self.crimeRate = 1.3

        self.sat = randint(50, 100)
        self.satRate = self.calcSatRate() # A decrease equivalent to a third of the crime increase
    

    # Policy actions

    def calcNewState(self, repress, surveil, support):
        self.applyRepress(repress)
        self.applySupport(support)
        self.applySurveil(surveil)

        self.boundValues()

        # Arbitrary threshold for growth rate
        if self.crimeRate < 1.05:
            self.crimeRate = 1.05


    def applyRates(self):
        self.crime = self.crime * self.crimeRate
        self.sat = self.sat * self.satRate
        self.satRate = self.calcSatRate()

        self.boundValues()

    # 1. Repress: Armed police is sent to location to catch criminals by all means necessary
    #    - Strongly reduces Crime but increases its growing rate (e.g. 1 Repress = -1 Crime and +0.01 Crime rate)
    #        => Logic: armed forces catch criminals but leave the field free for new one to take over
    #    - Strongly reduces PopSat (e.g. 1 Repress = -1 PopSat)
    #        => Logic: having armed forces roaming the street is not a pleasant living condition 
    def applyRepress(self, amount, outcome=False):
        crime = self.crime
        crimeRate = self.crimeRate
        sat = self.sat

        newCrime = crime - (amount * 1) # 1 is the repress to crime ratio
        newCrimeRate = crimeRate + (amount * 0.01)
        newSat = sat - (amount * 1) # 1 is the repress to satisfaction ratio

        if outcome:
            return newCrime, newCrimeRate, newSat
        else:
            self.crime = newCrime
            self.crimeRate = newCrimeRate
            self.sat = newSat


    # 2. Surveil: Send police to patrol the area to generate presence and gather information
    #    - Moderately decreases Crime and its growing rate (e.g. 1 Surveil = -0.5 Crime and -0.005 Crime rate)
    #        => Logic: detters petty criminals from acting out and information gathered allows the police to prevent future crime
    #    - Moderately decreases PopSat (e.g. 1 Repress = -0.5 PopSat)
    #        => Logic: constant police presence is not a pleasant living condition (though not as bad as armed forces)
    def applySurveil(self, amount, outcome=False):
        crime = self.crime
        crimeRate = self.crimeRate
        sat = self.sat

        newCrime = crime - (amount * 0.1) # is the surveil to crime ratio
        newCrimeRate = crimeRate - (amount * 0.002)
        newSat = sat - (amount * 0.1) # is the surveil to satisfaction ratio

        if outcome:
            return newCrime, newCrimeRate, newSat
        else:
            self.crime = newCrime
            self.crimeRate = newCrimeRate
            self.sat = newSat


    #3. Support: Send funding for local communities (e.g Job support, basic education, etc.)
    #    - Strongly dampers the growing rate of Crime but no effect on its current level (e.g. 1 Support = -0.01 Crime rate)
    #        => Logic: new social initiatives don't affect crime but will help future potential criminals to find another path through community support
    #    - Strongly increases PopSat (e.g. 1 Support = 1 PopSat)
    #        => Logic: generates local activity and builds up the community's well-being and cohesion
    def applySupport(self, amount, outcome=False):
        crimeRate = self.crimeRate
        sat = self.sat

        newCrimeRate = crimeRate - (amount * 0.002)
        newSat = sat + (amount * 0.5) # is the support to satisfaction ratio

        if outcome:
            return newCrimeRate, newSat
        else:
            self.crimeRate = newCrimeRate
            self.sat = newSat

    
    def calcSatRate(self):
        return 1 - (self.crimeRate - 1) / 3


    def boundValues(self):
        if self.crime < 0:
            self.crime = 0
        elif self.crime > 100:
            self.crime = 100
        
        if self.sat < 0:
            self.sat = 0
        elif self.sat > 100:
            self.sat = 100


    def printState(self):
        print(f"Crime: {self.crime}")
        print(f"Crime changing rate: {self.crimeRate}")
        print(f"Satisfaction: {self.sat}")
        print(f"Satisfaction changing rate: {self.satRate}")


