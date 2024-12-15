# Provision computer accessories to employees
# If accessory is available in store, we will provision
# Else we will give message that  accessory is not available

store = ['mouse', 'keyboard', 'monitor', 'headset', 'phone', 'usbhub', 'touchpen']
# store=[]
requested_items = ['mouse', 'keyboard', 'pendrive', 'headset','touchpen']
# requested_items = []
if store and requested_items:  # List null check - Python interpreter check the len of store list. If len=0 it return false
    for requested_item in requested_items:
        if requested_item in store:
            if requested_item == 'touchpen':
                print('special approval required for provisioning touchpen')
            else:
                print(f'Provisioned: {requested_item}')
        else:
            print(f'Item not available: {requested_item}')
else:
    print('Store and/or Request List is empty')
