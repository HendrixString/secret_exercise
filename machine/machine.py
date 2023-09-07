from typing import List

class Machine(object):
    """
    A simple state machine, that can be modeled with any object.
    Also, if state is a callable object, then it will be triggered
    to call side effects.

    Example:
    ```python
    m = Machine("state_1")
    m.add("state_1", "event_1", "state_2")
    m.add("state_2", "event_2", "state_3")

    for state in m.iterate_input(["event_1", "event_2"]):
        print(state)

    This should print: state_2, state_3
    ```
    """

    def __init__(self, state: object = None):
        """
        Args:
        ----
            state (object):
                initial state of the machine
        """
        self._states_dict = {}
        self._state = state

        Machine.__call_state_if_callable(state)

    @staticmethod
    def __call_state_if_callable(state: object):
        if callable(state) is True:
            state()



    def add(self, from_state: object, event: object, to_state: object):
        """
        Model a state machine transition in the form of (State1 --Event--> State2)

        Args:
        ----
        from_state (object):
            The pre state transition
        event (object):
            The event object that induces transition
        to_state (object):
            The post state transition
        """
        events_dict = self._states_dict.get(from_state, {})
        events_dict.update({ event : to_state })
        self._states_dict.update({from_state : events_dict})

        return self
    
    def iterate_input(self, input: List[object]):
        """
        A generator to iterate over input events sequence

        Args:
        ----
        input (List[object]):
            Sequence of events

        Raises Exception if state transition is invalid (incomplete)
        """
        index = 0
        len_input = len(input)

        while(index < len_input):
            eval = input[index]
            events_dict = self._states_dict.get(self._state, None)

            if events_dict is None:
                raise Exception(f'No state registered for {self._state}')
            
            sync_state = events_dict.get(eval, None)

            if sync_state is None:
                raise Exception(f'No sync state registered for event {eval}')

            self._state = sync_state
            Machine.__call_state_if_callable(self._state)

            yield self._state

            index+=1