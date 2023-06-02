#!/usr/bin/env python
# coding: utf-8

# In[ ]:

file = open('all_email_provider_domains.txt','r')

free_email_domains = []
for line in file:
    free_email_domains.append(line)

def chunks(chunk):
    emails = chunk['email'].tolist()
    no_of_emails = []
    all_emails = []
    
    for email in emails:
        if ',' in email:
            a = (email.split(','))
            no_of_emails.append(len(a))
            for i in a:
                all_emails.append(i.split('@')[1].replace(']','').replace("'",''))
        else:
            all_emails.append(email.split('@')[1].replace(']','').replace("'",''))
            no_of_emails.append(1)


    name = chunk.index[0]
    df1 = chunk

    
    
    df1.drop(columns = 'email', inplace = True)
    
    df1.insert(5,'email','')
    
    flattened_email_list = []
    
    for email in emails:
        if ',' in email:
            a = (email.split(','))
            for i in a:
                # print(i)
                flattened_email_list.append(i.replace(']','').replace("[",'').replace("'",''))
        else:
            # print(email.replace(']','').replace("[",'').replace("'",''))
            flattened_email_list.append(email.replace(']','').replace("[",'').replace("'",''))
    
    personal_emails = []
    for i,j in enumerate(all_emails):
        if j+'\n' in free_email_domains:
            personal_emails.append(flattened_email_list[i])
        else:
            personal_emails.append('')
    l = 0
    for i,j in enumerate(no_of_emails):
        email = ''
        for k in range(0,j):
            if j > 1:
                if personal_emails[l] == '':
                    email = email 
                else:
                    email = email + personal_emails[l].replace('[','').replace(']','').replace("'",'') 
            else:
                email = email + personal_emails[l].replace('[','').replace(']','').replace("'",'')                 
            # # df1['email'][i] = personal_emails[i]
            # email = email +' '+ personal_emails[i].replace('[','').replace(']','').replace("'",'')
            l += 1
        
        if email.count('@') > 1:
            df1.loc[df1.index[i],'email'] = email.replace(' ',', ')
        elif email.count(' ') == 1:
            df1.loc[df1.index[i],'email'] = email.strip()
        else:
            df1.loc[df1.index[i],'email'] = email.strip()

    df1.to_csv('Chunks1/chunk_'+str(name)+('.csv'),index = False)

