# Data Collection
## Running the code
- To run `make_visuals.py`, first ensure that you have a `data/` directory containing the folders `5-core/` and `ratings/`.  These must be in the same parent directory.
    - These folders should contain your 5-core `.json.gz` and rating `.csv` data respectively.
- Also ensure that you have `make_visuals.py` from homework 3. I have included it in this repository.
- Install the dependencies noted in `requirements.txt`.
    - If these dependencies are not installed, run 
    ```get_data
    pip install [dependency]
    ```
    in the terminal to install them.
- In the terminal run
```
python make_visuals.py
```
- If 4 PDFs have been saved, then you have successfully run the code!
    - 2 PDFs will be save in the `data/ratings/` directory.

## Other information
The raw code and full commit history can be found [here](https://github.com/medvidov/dsci510final). Code for this assignment can be found in the folder `HW4`.