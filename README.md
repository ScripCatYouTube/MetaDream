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

SERVER_ICON = 'https://raw.githubusercontent.com/ScripCatYouTube/asbg_server_1/main/icon.png' # Icon isn't used
parent_dir = os.getcwd() + '\\'

server = Server(SERVER_ICON, parent_dir + 'user.py', parent_dir + 'server.py')

start(server, is_run = True)
```
