import pandas as pd
import numpy as np

contacts = pd.read_excel (FILE PATH HERE)

cols_to_change = ['Names_Catchall','Title_Degree_Salutation_Catchall','Email_Catchall']
contacts[cols_to_change] = contacts[cols_to_change].applymap(lambda x: x.upper())

#Depending on the flavor of messy data, the delims may need to be switched out! Always watch out for ampersands (:
delims = [' OR ',' "OR" ',' AND ','/',',','-']

def swap_it_out(x, y, z):
    for elem in y:
        if elem in x:
            x = x.replace(elem, z)
    return x
    
contacts[cols_to_change] = contacts[cols_to_change].applymap(lambda x: swap_it_out(x, delims, ';'))

#Refactor for less repetition!
sep_names = contacts['Names_Catchall'].str.split(';', expand = True)
sep_titles = contacts['Title_Degree_Salutation_Catchall'].str.split(';', expand = True)
sep_emails = contacts['Email_Catchall'].str.split(';', expand = True)

#Refactor for less repetition, too!
contacts['Name1'] = sep_names[0]
contacts['Name2'] = sep_names[1]
contacts['Title1'] = sep_titles[0]
contacts['Title2'] = sep_titles[1]
contacts['Email1'] = sep_emails[0]
contacts['Email2'] = sep_emails[1]

contacts = pd.wide_to_long(contacts, stubnames=['Name','Email','Title'], i=['Partner', 'AgencyID'], j='Org_Contact_Count')

contacts = contacts.drop(['Names_Catchall','Email_Catchall','Phone','PhoneExt','Title_Degree_Salutation_Catchall'], axis=1)
contacts = contacts.dropna(subset=['Name'])

salutations = ['DR.','MR.','MS.','MRS']

def get_salutations(g,h):
    for elem in h:
        if elem in g:
            return g[:3]
        else:
            return 'NoSal'

contacts['Salutation'] = contacts['Name'].apply(lambda x: get_salutations(x, salutations))

def pop_name(t,l):
    if t == 'NoSal':
        return l
    else:
        return l[3:]
    
contacts['NameTest'] = contacts.apply(lambda row: pop_name(row['Salutation'], row['Name']), axis=1)
