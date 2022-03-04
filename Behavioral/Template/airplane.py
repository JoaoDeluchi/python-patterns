from abs_transport import AbsTransport


class AirPlane(AbsTransport):
    def start_engine(self):
        print('Starting the Rolls-Royce gas-turbine engines')

    def leave_terminal(self):
        print('Leaving the terminal')
        print('taxiing to runway')

    def travel_to_destinantion(self):
        print('Flying...')

    def entertainment(self):
        print('playing in flight movie!')

    def arrive_at_destination(self):
        print(f'Landing at {self._destination}')
