from flask_migrate import Migrate, MigrateCommand
from controller.main_controllers import app
from flask_script import Manager
from Settings.configuration import db

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

