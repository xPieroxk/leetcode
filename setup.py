import os
import sys

# python setup.py <easy|medium|hard> <number>
if len(sys.argv) == 3:
    path = os.path.join(sys.argv[1], sys.argv[2])

    os.makedirs(path, exist_ok=True)

    open(os.path.join(path, "README.md"), 'w').close()
    open(os.path.join(path, "solution.py"), 'w').close()