from actions.appliance import Appliance
from actions.door import Door
from actions.security import Security

from door_commands import DoorLockCommand, DoorUnlockCommand
from security_command import SecurityArmCommand, SecurityDisarmCommand
from appliance_commands import ApplianceOnCommand, ApplianceOffCommand
from menu_actions import MenuAction

menu_action = MenuAction()
frontdoor = Door('Front Door')
frontdoor_lock = DoorLockCommand(frontdoor)
frontdoor_unlock = DoorUnlockCommand(frontdoor)


menu_action.set_command(frontdoor, frontdoor_lock, frontdoor_unlock)

menu_action.activate(frontdoor)
menu_action.deactivate(frontdoor)
menu_action.deactivate(frontdoor)
menu_action.undo()
menu_action.undo()
menu_action.undo()

menu_action.undo()
