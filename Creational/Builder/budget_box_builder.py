from abs_builder import AbsBuilder


class BudgetBoxBuilder(AbsBuilder):

    def get_case(self):
        self._computer.case = 'Corsair'

    def build_mainboard(self):
        self._computer.mainboard = 'ASUS'
        self._computer.cpu = 'AMD'
        self._computer.memory = '2 x 4gb'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'Seagate'

    def install_video_card(self):
        self._computer.video_card = 'On board'
