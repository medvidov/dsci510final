# Data Collection
## Running the code
- To run `get_data.py`, first ensure that you have a `data` directory containing the folders `5-core/` and `ratings/`.  These must be in the same parent directory.
    - These folders should contain your 5-core `.json.gz` and rating `.csv` data respectively.
- Install the dependencies noted in `requirements.txt`.
    - If these dependencies are not installed, run 
    ```
    pip install [dependency]
    ```
    in the terminal to install them.
- In the terminal run
```
python get_data.py
```
- If the output is 3 numbers, then you have successfully run the code!

## Other information
The raw code and full commit history can be found [here](https://github.com/medvidov/dsci510final). Code for this assignment can be found in the folder `HW3`.