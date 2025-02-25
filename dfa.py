# Copyright 2025 Mango182
import graphviz
from collections import defaultdict

class DFA:
    def __init__(self,
                 states: set[str],
                 alphabet: set[str],
                 transition_fucntion: dict[str, dict[str, str]],
                 start_state: str,
                 accepting_states: set[str]):
        """
        Creates a DFA.

        Args:
            states (list[str]):
                Set of states in the DFA
            alphabet (list[str]):
                Alphabet for DFA
            transition_fucntion (dict[str, dict[str, str]]): 
                Dictionary of all possible transitions
            start_state (str):
                Starting state of a DFA
            accepting_states (list[str]): 
                Set of accepting states
        """
        self._states = sorted(set(states))
        self._alphabet = set(alphabet)
        self._transitions = defaultdict(lambda: defaultdict(str))
        self._start = str(start_state)
        self._accepting = set(accepting_states)

        for start, transitions in transition_fucntion.items():
            for symbol, end in transitions.items():
                self._transitions[start][symbol] = end

    @property
    def states(self) -> set[str]:
        return self._states

    @property
    def alphabet(self) -> set[str]:
        return self._alphabet
    
    @property
    def transitions(self) -> defaultdict[str, defaultdict[str, str]]:
        return self._transitions

    @property
    def start(self) -> str:
        return self._start 

    @property
    def accepting(self) -> list[str]:
        return self._accepting
    
    def is_accepted(self, string: str) -> bool:
        """
        Check if a string is accepted by the DFA.

        Returns:
            bool: True if the string is accepted, False otherwise.
        """
        current = self._start
        for char in string:
            # checks to see if you can move to a new state
            for symbol, next_state in self._transitions.get(current, {}).items():
                found_transition = False

                # different cases in the alphabet
                if symbol == "1-9" and char.isdigit and 1 <= int(char) <= 9:
                    current = next_state
                    found_transition = True
                    break
                elif symbol == "0-9" and char.isdigit():
                    current = next_state
                    found_transition = True
                    break
                elif symbol == char:
                    current = next_state
                    found_transition = True
                    break
            
            # If at any character you cannot find an edge that takes you to a state, the string is not accepted
            if not found_transition:
                return False
        
        # Return true if the current state is in the list of accepting states
        return current in self._accepting

    
    def render(self, title: str = "DFA") -> None:
        """ Generate a dfa using a 5 tuple. """
        # Creates directed graph
        dfa = graphviz.Digraph(format="png")
        dfa.attr(rankdir="LR", label=title,  labelloc="t", fontsize="20")

        # Creates the states for the DFA
        for state in self._states:
            if state in self._accepting:
                dfa_node = dfa.node(state, shape="doublecircle")
            else:
                dfa_node = dfa.node(state, shape="circle")

        # Creates the transitions for the DFA by either using a list of strings or a dictionary
        for start, transitions in self._transitions.items():
            for symbol, end in transitions.items():
                dfa.edge(start, end, label=symbol)

        # Creates the image for the DFA
        dfa.render("diagrams/" + title.replace(" ", "_"))

    
    def print_transitions(self):
        """ Print transitions."""
        for start, transitions in self._transitions.items():
            for symbol, end in transitions.items():
                print(f"{start} -> {end} : {symbol}")
        print()

def make_states(num_states: int) -> set[str]:
    """ Generate states from a number of states."""
    return [f"q{i}" for i in range(num_states)]
