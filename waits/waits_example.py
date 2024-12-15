# Waits
# They sync out script speed with browser execution speed
# Normally our coded scripts runs faster than web actions on browser
# Slow down/sync our script as per specific web action

# Strategies
# 1. After every action we wait for some fixed amount of secs --> Increase overall execution time.
# 2. After specific actions we wait for some fixed amount of secs --> This needs lots of maintenance and increases execution time
# 3. We wait until all elements load up or all actions complete on webpage. --> Dynamic web pages will be limitation
# 4. We wait for specific elements to load until they load.

# 1. time.sleep
# 2. time.sleep
# 3. implicit wait
# 4. explicit wait