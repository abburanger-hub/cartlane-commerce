rom orders import create_order

def process_checkout(user,cart):

if not cart:
raise Exception(
"CheckoutError"
)

return create_order(
user,
cart
)
