# DFA Generator

## Features

- Define states, alphabet, transitions, start state, and accept states.
- Simulate DFA to check if it accepts or rejects a given input string.

## Requirements

- Python 3.x
- Graphviz

## Installation

To use the DFA rendering feature, you need to have Graphviz installed. You can download and install Graphviz from [here](https://graphviz.org/download/).

Alternatively, you can install it using a package manager:

For Debian/Ubuntu:
```sh
sudo apt-get install graphviz
```

For macOS using Homebrew:
```sh
brew install graphviz
```

For Windows, download the installer from the [Graphviz website](https://graphviz.org/download/).

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/Mango182/dfa_gen
    cd dfa_gen
    ```

2. Run the script:
    ```sh
    python dfa.py
    ```

## Example

Here is an example of how to define a DFA in `dfa.py`:

```python
states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
transitions = {
    'q0': {'0': 'q0', '1': 'q1'},
    'q1': {'0': 'q2', '1': 'q0'},
    'q2': {'0': 'q1', '1': 'q2'}
}
start_state = 'q0'
accept_states = {'q0'}
dfa = DFA(states, alphabet, transitions, start_state, accept_states)
```

To render the DFA:

```python
dfa.render()
```

To simulate the DFA with an input string:

```python
input_string = '101'
result = dfa.simulate(input_string)
print(f'The input string is {"accepted" if result else "rejected"} by the DFA.')
```

## Diagram
![DFA](https://github.com/user-attachments/assets/20b40014-c6f5-44c0-b459-4f7a0cfd514d)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
