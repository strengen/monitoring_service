from .database import create_tables
from .services import update_data

# This feature is not going to work in Docker container!
# This file is for updating prices each hour with using systemd timer.
# To use it, you should create a systemd service and timer.
# Run sudo systemctl enable --now <filename>.timer to enable it
# Run sudo systemctl disable --now <filename>.timer to disable it
create_tables()
update_data()