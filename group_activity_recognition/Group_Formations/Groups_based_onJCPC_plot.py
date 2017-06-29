from bokeh.plotting import figure, output_file, show, ColumnDataSource,save
from bokeh.models import HoverTool
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import numpy as np
import os
from glob import glob
from bokeh.io import output_notebook
from bokeh.palettes import inferno

f = open('ProximityData\\groups_05242013.txt','r')
lines = []
lines.append(f.readlines())
textlines = []
for i in range(len(lines[0])): 
    textlines.append( lines[0][i].split("|"))
    
# Reading data from the file

time = []
for i in range(len(textlines)):
    time.append((int(textlines[i][0])))    # Storing the time index

group = [[] for h in range(len(time))]
for i in range(len(textlines)):
    for p in range(1,len(textlines[i])-1):
        group[i].append((textlines[i][p]))  # Storing the groups that were formed inside a list.
        
for k in range(len(group)):
    for p in range(len(group[k])):
        group[k][p] = group[k][p].replace('u','')
        
f.close()

na = [i for i in range(60)]
use= []
for j in range(len(na)):       # user ids are like 08, 09. We convert it to u08, u09
    if(len(str(na[j])) == 1):
        use.append('0'+ str(na[j]))
    else:
        use.append(str(na[j]))        

for k in range(len(use)):
    use[k] = 'u' + use[k]  


color_palette = inferno(60)         # Adding colors to the plot 
colors = {use[u] : color_palette[u] for u in range(len(use))}

i = 0    
output_file('toolbar.html')
user_group = ''
for kj in range(len(group[i])):
    user_group += ',' + group[i][kj]

h =  user_group.split(",")   
totaluser = len(h) - 1

# processing done for x_Axis
ck= []
ck.append(time[i])
v = ck * totaluser

xaxis = [j for j in range(1,len(group[i]) + 1)]  # x_axis as an array - denotes the no of groups formed at that time


yaxis = [len(group[i][hj].split(",")) for hj in range(len(group[i]))]  # denotes the member of a particular group at that time.




yt = [range(yaxis[k]) for k in range(len(yaxis))]

s = yt[0]
for hg in range(1,len(yt)):
    s += yt[hg]
xax = []   
for bh in range(len(xaxis)):
    cp = []
    cp.append(xaxis[bh])
    vp = cp * yaxis[bh]
    xax.append(vp)
# Processing data for x and y axis in the plot.
xs = xax[0]
for hg in range(1,len(xax)):
    xs += xax[hg]
for g in range(len(h)):
    h[g] = h[g].replace(" ","")
#userlok.append([h[kl] for kl in range(1,len(h))])
source = ColumnDataSource(
        data=dict(
            x= xs,  # xaxis
            y= s,  # yaxis
            #desc=['A', 'b', 'C', 'd', 'E'],
            fill_color= [colors['u'+ h[kl]] for kl in range(1,len(h))], # giving unique color to each member of a group
            User_groups=[h[kl] for kl in range(1,len(h))]  # denoting the usergroups (members of the group)
        )
    )

# Hover options for Interactive Plot
hover = HoverTool(
        tooltips=[  
            ("User_groups", "@User_groups"),
            ("fill color", "$color[hex, swatch]:fill_color"),
            ("time", "$x"),

        ]
    )

p = figure(plot_width=400, plot_height=400, tools=[hover],
           title="Mouse over the dots", x_axis_label = 'At Time ' + str(time[i]))


p.circle('x', 'y', size=15, source=source,fill_color = 'fill_color')



#p.yaxis.visible = False


show(p)
save(p)
