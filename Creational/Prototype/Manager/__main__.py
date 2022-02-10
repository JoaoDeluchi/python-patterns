from prototype_manager import PrototypeManager
from laptop import Laptop
from tower import Tower, MainBoard

manager = PrototypeManager()
l1 = Laptop('L1', 'Intel', '32gb', '2TB SSD', 'onboard', '1920x1080')
l1.display()
manager |= {'L1': l1}
l2 = manager['L1'].clone()
l2.model = 'L2'
l2.processor = 'AMD'
l2.display()


t1 = Tower('T1', MainBoard('Asus', 'game'), 'AMD',
           '32gb', '2TB SSD', 'onboard', '1920x1080')
t1.display()
manager |= {'T1': t1}
t2 = manager['T1'].clone()
t2.model = 'T2'
t2.mainboard.model = 'Business'
t2.display()
t1.display()
