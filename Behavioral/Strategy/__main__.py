from shipping_cost import ShippingCost
from fedex_strategy import FedExStrategy
from postal_strategy import PostalStrategy
from ups_strategy import UPSStrategy

order = None  # should have a instace of Order
strategy = FedExStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0


order = None  # should have a instace of Order
strategy = UPSStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0


order = None  # should have a instace of Order
strategy = PostalStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0


print('Tests Passed')
