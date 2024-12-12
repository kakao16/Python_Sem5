# Stanisław Kusiak

class FSM:
    def __init__(self, states, transition_fun, true_states, start):
        self.states = states
        self.transition_fun = transition_fun
        self.true_states = true_states
        self.start = start

    def transition(self, current_state, symbol):
        return self.transition_fun.get(current_state, {}).get(symbol)
    
    def is_true(self, state):
        return state in self.true_states
    
    def process(self, input):
        current_state = self.start

        for symbol in input:
            next_state = self.transition(current_state, symbol)
            if next_state is None:
                return False
            
            current_state = next_state

        return self.is_true(current_state)
    

states = {"q0", "q1", "q2"}
transitions = {
    "q0": {"0": "q1", "1": "q0"},
    "q1": {"0": "q2", "1": "q1"},
    "q2": {"0": "q0", "1": "q2"}
}
true_states = "q2"
start_state = "q0"

fsm = FSM(states, transitions, true_states, start_state)

input_sequence = "10101"
results = fsm.process(input_sequence)
print(f"Sequence: '{input_sequence}' ended on {results} state.")