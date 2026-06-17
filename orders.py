def create_order(
user,
cart
):

total=sum(
item["price"]
for item in cart
)

if total>5000:

raise Exception(
"OrderSyncFailed"
)

return {
"status":"confirmed"
}
