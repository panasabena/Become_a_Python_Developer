# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 10:45:02 2022

@author: fsabena
"""


text = '''Your company, Sprocket Sales International (SSI), is a wholesale parts company 
that is transforming into an Intelligent Enterprise to fully leverage existing 
investments in MicroStrategy. This transition enables SSI to successfully deliver 
powerful analytics solutions across the organization. Your role in the Intelligent 
Enterprise is that of the Analytics Architect, which requires oversight over the 
project architecture and design activities in the organization, combined with a 
deep understanding of analytics architect skills, functionalities, and possibilities.
In this course, you take a deeper dive into project architecture, ideal 
normalization strategies, optimized query performance, and related project 
design topics framed through the holistic lens of an Analytics Architect in your 
new Intelligent Enterprise. The course focuses on the key competencies that are 
required to help you establish a high quality, intelligent analytics team. These 
skills help you support your organization to create and maintain standards in 
developing a project architecture that serves as the foundation for the 
organization’s analytics applications.'''

print(text)
#%%
print(len(text))
#%%
print(text.split())
#%%
print(len(text.split()))

#%%
for word in text.split():
    print(word)
#%%
word_count = {}
for word in text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
#%%

import this
import sys
from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'magenta', end=' ')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
