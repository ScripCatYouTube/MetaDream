# apiServerBase
A library for ASB server

# Example Create Server

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

Create custom user class

```
# user.py

from library.basic_user import User

class User(User):
	def __init__(self, fabric_user, app, server, vault):
		super().__init__(fabric_user, app, server, vault)
```

Create custom server class

```
# server.py

from library.fabric_server import FabricServer

class Server(FabricServer): 
	def __init__(self, server):
		super().__init__(server)
```
