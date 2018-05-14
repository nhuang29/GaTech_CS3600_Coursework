# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
import game

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    stack1 = util.Stack()
    stack1.push((problem.getStartState(), None, 1))
    visitSet = []
    stepList = []

    while (stack1.isEmpty() == False):
        poppedState = stack1.pop()
        visitSet.append(poppedState[0])

        if (poppedState[2] <= len(stepList)):
            # replaces the step
            stepList[poppedState[2] - 1] = poppedState[1]
        else:
            # only goes here at the beginning
            stepList.append(poppedState[1])

        if problem.isGoalState(poppedState[0]):
            if not (stepList[0] == None):
                return stepList
            else:
                # this basically removes the front if "None" is the first direction
                stepList.pop(0)
                return stepList

        for element in problem.getSuccessors(poppedState[0]):
            if element[0] not in visitSet:
                # increment the steps that are being pushed on
                # in order to work with the placement in the stepList
                stack1.push((element[0], element[1], poppedState[2] + 1))
    
def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    queue1 = util.Queue()
    visitSet = []
    stepList = []
    queue1.push((problem.getStartState(), stepList))

    while (queue1.isEmpty() == False):
        latestPop = queue1.pop()
        popped = latestPop[0]
        steps = latestPop[1]

        if problem.isGoalState(popped):
            return steps

        if not (popped in visitSet):
            visitSet.append(popped)
            for element in problem.getSuccessors(popped):
                queue1.push((element[0], steps + [element[1]]))


def uniformCostSearch(problem):
    "Search the node of least total cost first."
    queue1 = util.PriorityQueue()
    priorNum = 0
    visitSet = []
    stepList = []
    queue1.push((problem.getStartState(), stepList), priorNum)

    while (queue1.isEmpty() == False):
        latestPop = queue1.pop()
        popped = latestPop[0] 
        steps = latestPop[1] 
        
        if problem.isGoalState(popped):
            return steps

        if not (popped in visitSet):
            visitSet.append(popped)
            for element in problem.getSuccessors(popped):
                queue1.push((element[0], steps + [element[1]]), problem.getCostOfActions(steps + [element[1]]))

        
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    queue1 = util.PriorityQueue()
    visitSet = []
    stepList = []
    queue1.push((problem.getStartState(), stepList), heuristic(problem.getStartState(), problem))

    while (queue1.isEmpty() == False):
        latestPop = queue1.pop()
        popped = latestPop[0]
        steps = latestPop[1] 
        
        if problem.isGoalState(popped):
            return steps

        if not (popped in visitSet):
            visitSet.append(popped)
            for element in problem.getSuccessors(popped):
                queue1.push((element[0], steps + [element[1]]), problem.getCostOfActions(steps + [element[1]]) + heuristic(element[0], problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
