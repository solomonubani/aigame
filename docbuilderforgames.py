#!/usr/bin/env python3
import time
import re
import sys

def isTimeFormat(input):
    if re.match('\d{2}:\d{2}', input):
        return True
    else:
       return False
       
import os
x = os.path.dirname(os.path.abspath(__file__))
y = os.path.basename(x)
#print(y)

import csv  
    
# field names  
fields = ['name', 'timestamp', 'transcript', 'source'] 
fields = ['starttime',  'utterance', 'instruction?', 'instruction type', 'speaker']


#print(f.name)

count = 0
counter = 0

# name of csv file  
filename = "out.csv"  
# writing to csv file  
with open(filename, 'a') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    #csvwriter.writerow(fields)  
        
    transcript = ""
    
    files = ["input.txt"]
    for file in files:
        f = open(file, "r")
        for line in f: 
            counter = counter + 1
            if (counter == 1):
                line = "\n"

            try: 
                
                #source = ""
                if line in ['\n', '\r\n']:
                        if (count > 0):
                            
                            import re
                            p = re.compile(r'(?<=\d)\.[0-9]+\b')
                            subst = ""
                            
                            
                            result = re.sub(p, subst, transcript)
                            txt = result
                            #txt = transcript
                            #print(txt)
                            txt = """{t}""".format(t=txt)
                            txt = txt.replace('\n',' ')

                            txt.split('.')
                            transcript_sentences =  [x for x in map(str.strip, txt.split('.')) if x]
                            for i in transcript_sentences:
                               #print(i)
                            
                               #periods, emotions, Sentence, annotation (instruction or not), annotation (instruction type), speaker
                               output = [[time,  i, " ", " ", name]]
                               csvwriter.writerows(output) 
                            
                            
                            transcript = ""
                    
                        #print("name: ", f.next().strip())
                        name = f.next().strip()
                        #print("time: ", f.next().strip())
                        time = f.next().strip()
                        source = y + "/"+ f.name
                        

                else:
                    if (not isTimeFormat(line.strip())):
                        #print("transcript\n", line.strip())
                        transcript += line.strip() + '\n'
                    
                        
                           
                        count = count + 1
                        # writing the data rows              
            except StopIteration: 
            
                pass
                
        # Closing files 
        f.close() 
   
   
'''
count = count + 1
print("Transcript", count)
while(True):
    x = f.next()
    if not x.strip():
        break
    else:
        if (not isTimeFormat(x)):
            sys.stdout.write (x)


print("")
'''
            

