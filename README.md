# apiServerBase
A library for ASB server

# Example create project

Create in directory there have folder 'library' create file: 'main.py', 'server.py', 'user.py'

Create main server

```
# main.py

import os

from library.flask_app import start
from library.server import Server

parent_dir = os.getcwd() + '\\'
server = Server(SERVER_ICON, parent_dir + 'user.py', parent_dir + 'server.py')

start(server, is_run = True)
```
