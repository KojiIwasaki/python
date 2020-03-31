import python_def
data = [{'name':'山本', 'bill':40000, 'crg':True},
        {'name':'吉田', 'bill':25000, 'crg':False}]

for rec in data:
    bill = rec['bill']
    if rec['crg']:
        bill = python_def.add_charge(bill)
    python_def.create_mail(rec['name'], bill)