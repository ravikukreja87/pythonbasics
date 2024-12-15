email_database = {'Jon': 'jon@test.in',
                  'Mark': 'mark@test.in',
                  'Tom': 'tom@test.in'}

jon_email_title = email_database['Jon'].title()  # Store value of Key Jon in variable jon_email
jon_email = email_database['Jon']
# print(f'Jon\'s email is : {jon_email}')
# print(f'Jon\'s email (title) is : {jon_email_title}')

#get()

print(email_database.get('Jon','Provided key does not exists in email_database dictionary'))
print(email_database.get('jon','Provided key does not exists in email_database dictionary'))

