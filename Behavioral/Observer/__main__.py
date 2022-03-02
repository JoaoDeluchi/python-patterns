from kpis import KPIs
from currentkpis import CurrentKPIs
from forecastkpis import ForecastKPIs

with KPIs() as kpis:
    with CurrentKPIs(kpis), ForecastKPIs(kpis):
        kpis.set_kpis(25, 10, 5)
        kpis.set_kpis(100, 50, 30)
        kpis.set_kpis(50, 10, 20)


print('\n**** exited context managers')
kpis.set_kpis(150, 110, 120)
