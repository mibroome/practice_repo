Commands to install
====================
Navigate into `practice_repo/` and create virtual environment
```
python3 -m venv practice.venv
source practice.venv/bin/activate
```
Then run
```
pip install -e .
```
This will create a local installation of the package (and all of the necessary dependencies with the correct versions, etc.).
This just means we can import it anywhere on our computer as we would e.g., `numpy`.

Try to run our broken function with 
```
python3 practice_code/broken_function.py
```
This should produce a cool 3D plot (as in [here](https://matplotlib.org/stable/gallery/mplot3d/contourf3d_2.html#sphx-glr-gallery-mplot3d-contourf3d-2-py)), but it doesn't! So what do we do!

To the `.vscode/launch.json` file that is created, add the line 
```
"cwd": "${fileDirname}"
```
This just means the debugger will run from the current file.
