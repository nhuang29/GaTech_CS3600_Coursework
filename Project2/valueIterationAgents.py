# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        "*** YOUR CODE HERE ***"
        for i in range(0, self.iterations):
          Vals = util.Counter()
          stateList = self.mdp.getStates()
          for curr in stateList:  
            if self.mdp.isTerminal(curr):
              Vals[curr] = 0
            else:
              maxVal = -1 * float('inf')
              for x in self.mdp.getPossibleActions(curr):
                  if not maxVal > self.getQValue(curr, x):
                    maxVal = self.getQValue(curr, x)
              Vals[curr] = maxVal
          self.values = Vals


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        score = 0
        stateList = self.mdp.getTransitionStatesAndProbs(state,action)

        if not stateList:
          return score
        else:
          for transition in stateList:
            transState, val = transition[0], transition[1]
            r = self.mdp.getReward(state,action,transState)
            discount = self.discount * self.values[transState]
            score =  score + val * (r + discount)
        return score

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        bestPol = None
        bestVal = -1 * float('inf')
        
        if not self.mdp.isTerminal(state) or not self.mdp.getPossibleActions(state):
          for action in self.mdp.getPossibleActions(state):
            
            if self.computeQValueFromValues(state, action) == bestVal:
              bestPol = action
              bestVal = self.computeQValueFromValues(state, action)
              
            if not self.computeQValueFromValues(state, action) < bestVal:
              bestPol = action
              bestVal = self.computeQValueFromValues(state, action)
              
          return bestPol
        return bestPol

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
