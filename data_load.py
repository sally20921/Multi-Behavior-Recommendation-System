import tensorflow as tf

'''
Column 
event_time When event is was happened (UTC)
event_type Event type: one of [view, cart, remove_from_cart, purchase]
product_id Product ID
category_id Product category ID
category_code Category meaningful name (if present)
brand Brand name in lower case (if present)
price Product price
user_id Permanent user ID
user_session User session ID
'''

with open('../raw_data/', '') as f:
 
