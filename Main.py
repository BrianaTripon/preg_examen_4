from Controller.controller import Controller
from Repository.bus_repository import BusRepo
from Repository.route_repository import RouteRepo
from UI.ui import UI

route_repo = RouteRepo("routes")
bus_repo = BusRepo("buses")
controller = Controller(route_repo, bus_repo)

ui = UI(controller)
ui.start()
