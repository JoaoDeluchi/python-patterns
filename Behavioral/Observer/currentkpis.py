from observer.abs_observer import AbsObserver


class CurrentKPIs(AbsObserver):
    _open_tickets = -1
    _closed_tickets = -1
    _new_tickets = -1

    def __init__(self, kpis) -> None:
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis._closed_tickets
        self.new_tickets = self._kpis._new_tickets
        self.display()

    def display(self):
        print(f'Open Tickets: {self.open_tickets}')
        print(f'Closed Tickets: {self.closed_tickets}')
        print(f'New Tickets: {self.new_tickets}')
        print(f'****\n' * 3)
