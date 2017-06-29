userlok = []
for i in range(600,665):  # class timings are from 600 - 665 minutes
    #output_file('toolbar.html')
    user_group = ''
    for kj in range(len(group[i])):
        user_group += ',' + group[i][kj]

    h =  user_group.split(",")   
    totaluser = len(h) - 1

    ck= []
    ck.append(time[i])
    v = ck * totaluser

    xaxis = [j for j in range(1,len(group[i]) + 1)]


    yaxis = [len(group[i][hj].split(",")) for hj in range(len(group[i]))]




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

    xs = xax[0]
    for hg in range(1,len(xax)):
        xs += xax[hg]
    for g in range(len(h)):
        h[g] = h[g].replace(" ","")
    userlok.append([h[kl] for kl in range(1,len(h))])
    source = ColumnDataSource(
            data=dict(
                x= xs,
                y= s,
                #desc=['A', 'b', 'C', 'd', 'E'],
                fill_color= [colors['u'+ h[kl]] for kl in range(1,len(h))],
                User_groups=[h[kl] for kl in range(1,len(h))]
            )
        )

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


    #show(p)
    #save(p)
    
    
class_attendes = []
for j in range(len(userlok)):
    v = userlok[j][0].split(",")
    for l in range(len(v)):
        class_attendes.append('u' + v[l])
        
        
classmembers  =  list(set(class_attendes))

print(len(classmembers))
