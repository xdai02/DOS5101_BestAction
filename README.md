# DOS5101_BestAction
### Description

- `data.xlsx` contains all the rules (actions + events) and initial data for this program.



### Usage

1. Open `action_analyzer.py`.
2. Run `action_analyzer.py`.



### Notes

- `ACTIONS_HAPPENED` (at the beginning of the code) indicates the actions already happened. Update it to get the latest optimal solution.

    ```python
    ACTIONS_HAPPENED = [
        (4, 11, 13),  # year 1
        (2, 9, 16),  # year 2
        None,  # year 3
        None,  # year 4
        None,  # year 5
        None,  # year 6
    ]
    ```

- `EVENTS_HAPPENED` (at the beginning of the code) indicates the events already happened. Update it to get the latest optimal solution.

    ```python
    EVENTS_HAPPENED = [
        5,  # year 1
        None,  # year 2
        None,  # year 3
        None,  # year 4
        None,  # year 5
        None,  # year 6
    ]
    ```

- The parameter `verbose` (at the end of the code)  is used to control whether to output detail trail info. Set it to `True` will generate a complete detailed info, otherwise only the best actions will be printed.

    ```python
    best_actions = action_analyzer.analyze(verbose=True)
    ```
