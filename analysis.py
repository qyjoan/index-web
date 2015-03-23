# Analyze web links results
import re
import pandas as pd

path = './'
fname = 'output'
domain = 'www.capitalone.ca'


j = 0
with open("{path}/{filename}".format(path = path,filename = fname)) as f:
    capone_tags = []
    url_keys = {}
    for line in f:
        line = line.strip()
        if line.startswith('http'):
            capone_domain = False
            url_parts = re.split('/+',line)
            if len(url_parts) > 2:
                key_parts = url_parts[1:-1]
            else:
                key_parts = url_parts[1:]
            parts = '/'.join(key_parts)
            if parts not in url_keys:
                url_keys[parts] = 1
                if key_parts[0] == domain:
                    capone_tag = {}
                    for i in range(len(key_parts)):
                        capone_tag["{}".format(i)] = key_parts[i]
                    capone_tags.append(capone_tag)    
            else:
                url_keys[parts] += 1
        j += 1

df = pd.DataFrame(capone_tags)
df.sort(columns=['0','1','2','3','4','5'],inplace = True)
df.to_csv('website_summary.csv')