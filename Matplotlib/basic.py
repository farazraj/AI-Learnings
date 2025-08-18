'''
I have created this file to learn the basics of matplotlib library of python. 
Where i have included keypoints in terms of different functions. 
You can call the particular function to see the particular output.

'''

#Common imports
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


#to check the version of matplotlib
def version():
    """Prints the version of matplotlib."""
    print("Matplotlib version:")
    print( matplotlib.__version__)



#to draw a line in a plot
#x and y points
def st_line():
    print("This is a line function")
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])

    plt.plot(xpoints, ypoints)
    plt.show()


def st_line2():
    print("This is a line function with more points")
    xpoints = np.array([0, 1, 2, 3, 4, 5, 6])
    ypoints = np.array([0, 3, 1, 4, 3, 5, 6])

    plt.plot(xpoints, ypoints)
    plt.show()



#to put only markers in a plot
def st_markers():
    print("This is a marker function")
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])

    plt.plot(xpoints, ypoints,'o')
    plt.show()


#for default x points
#if we don't mention x points, it will take default x points as incremental values starting from 0
def st_default_x():
    print("This is a default x points function")
    ypoints = np.array([3, 8, 1, 10, 5, 7, 6])

    plt.plot(ypoints)
    plt.show()


#to display markers with the line 
def st_default_x2():
    print("This is a default x points function with more points")
    ypoints = np.array([3, 8, 1, 10, 5, 7, 6, 2, 4])

    plt.plot(ypoints, marker = 'o')
    plt.show()



#to display markers with the line and marker as a *
def st_default_x3():
    print("This is a default x points function with more points")
    ypoints = np.array([3, 8, 1, 10, 5, 7, 6, 2, 4])

    plt.plot(ypoints, marker = '*')
    plt.show()


#to give a shortcut for the marker we have fmt method
def fm_marker():
    print("This is to display the marker in shortcut")

    y_pts = np.array([0, 1, 0, 2, 1, 3, 2, 4])

    plt.plot(y_pts, '*:g') #where * is the marker, : is the line type and g is th color or line and marker
    plt.show()

"""
Markers in matplotlib:

'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline


Line styles in matplotlib:

'-'	Solid line	

':'	Dotted line	

'--'	Dashed line	

'-.'	Dashed/dotted line


colors in matplotlib:

'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White

"""

#to use shortcut for marker|line|color and also give marker size
def mkr_size():
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, 's--k', ms = 7)
    plt.show()

#to show marker, size and marker edge color differently
def mkr_size2():
    ypoints = np.array([3, 8, 1, 10])
    jpoints = np.array([1, 2, 3, 4])
    fpoints = np.array([5, 8, 4, 2])
    plt.plot(ypoints, marker = 's', ms = 10, mec = 'r', mfc = 'k', linestyle = '--')
    plt.plot(jpoints, marker = '*', ms = 10, mec = '#4CAF50', mfc = '#4CAF50', linestyle = ':', color = 'k')
    plt.plot(fpoints, marker = 'o', ms = 10, mec = 'hotpink', mfc = 'hotpink', linestyle = '-', color = 'g')
    
    plt.show()

#to set labels and title
def lables_title():
    ypoints = np.array([2, 4, 6, 8, 10])
    plt.plot(ypoints, marker = 'o', ls = '-', color = 'cyan', ms = 15, lw = 5 )

    #to set the font style of the labels and title
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}
    
    #loc can be use to positions title and labels
    #loc = 'left' | 'right' | 'center' | 'top'
    plt.title("Show Titles", fontdict = font1, loc='center')
    plt.xlabel("X-axis Label", fontdict = font2, loc='center')
    plt.ylabel("Y-axis Label", fontdict = font2, loc='center')
    plt.show()


#to show grid in the plot
def grid():
    fpoints = np.array([2, 4, 6, 8, 10])
    jpoints = np.array([1, 3, 5, 7, 9])
    plt.plot(fpoints, jpoints, marker = 'o', ls = '-', color = 'cyan', ms = 15, lw = 2 )

    #to set the font style of the labels and title
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}
    
    plt.title("Show Titles", fontdict = font1, loc='center')
    plt.xlabel("X-axis Label", fontdict = font2, loc='center')
    plt.ylabel("Y-axis Label", fontdict = font2, loc='center')

    #to show grid
    plt.grid(color = 'red', ls = '-.', lw = 1) #color, linestyle, linewidth, alpha
    
    plt.show()


#to add subplots in a single plot
#where in plt.subplot(1, 4, 1) 1st is number of rows, 2nd is columns and 3rd is on what position the plot will be.
def subplots():
    ypoints = np.array([2, 6, 7, 1, 4, 3])
    plt.subplot(1, 4, 1)
    plt.plot(ypoints, color = 'red',  lw = 2 )

    spoints = np.array([1, 8, 4, 2, 5, 4])
    plt.subplot(1, 4, 2)
    plt.plot(spoints, color = 'green', lw = 2 )

    dpoints = np.array([1, 8, 4, 2, 5, 4])
    plt.subplot(1, 4, 3)
    plt.plot(dpoints, color = 'blue', lw = 2 )

    tpoints = np.array([1, 8, 4, 2, 5, 4])
    plt.subplot(1, 4, 4)
    plt.plot(tpoints, color = 'yellow', lw = 2 )

    plt.show()


#to show the scatter plot
#where x and y are the points to be plotted
'''
The observation in the example above is the result of 13 cars passing by.

The X-axis shows how old the car is.

The Y-axis shows the speed of the car when it passes.

'''
def scatter():
    print("This is a scatter plot function")
    #example of scatter plot
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    plt.scatter(x,y)
    
    plt.title("Diffrence b/w car's age and speed", loc='center')
    plt.xlabel("Age of Cars", loc='center')
    plt.ylabel("Speed of Cars", loc='center')
    
    plt.show()


'''
In the example above, there seems to be a relationship between speed and age, 
but what if we plot the observations from another day as well? 
Will the scatter plot tell us something else?

'''
def scatter2():
    #day one, the age and speed of 13 cars:
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    plt.scatter(x, y, marker = 'o', color = 'blue', label = 'Day 1')

    #day two, the age and speed of 15 cars:
    x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
    y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
    plt.scatter(x, y, marker = 'o', color = 'red', label = 'Day 2')

    plt.title("Diffrence b/w car's age and speed", loc='center')
    plt.xlabel("Age of Cars", loc='center')
    plt.ylabel("Speed of Cars", loc='center')

    plt.show()


#displaying each dot with different colors
def multi_color_scatter():
    print("This is a scatter plot function")
    #example of scatter plot
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
    
    plt.scatter(x,y, c=colors)
    
    plt.title("Diffrence b/w car's age and speed", loc='center')
    plt.xlabel("Age of Cars", loc='center')
    plt.ylabel("Speed of Cars", loc='center')
    
    plt.show()


'''
The Matplotlib module has a number of available colormaps.

A colormap is like a list of colors, where each color has a value that ranges from 0 to 100.

'''
def colormap():

    #day one, the age and speed of 13 cars:
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    colors1 = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
    plt.scatter(x, y, marker = 'o', c = colors1, cmap='viridis', label = 'Day 1') # 'viridis' is a colormap, you can change it to other colormaps like 'plasma', 'inferno', 'magma', etc.

    #day two, the age and speed of 15 cars:
    x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7])
    y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91])
    colors2 = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
    plt.scatter(x, y, marker = 'o', c = colors2, cmap='inferno', label = 'Day 2') # 'inferno' is a colormap, you can change it to other colormaps like 'viridis', 'plasma', 'inferno', 'magma', etc.

    plt.title("Diffrence b/w car's age and speed", loc='center')
    plt.xlabel("Age of Cars", loc='center')
    plt.ylabel("Speed of Cars", loc='center')

    plt.colorbar() #to add and show the color bar with the drawing
    plt.legend() #to show the legend of the plot - means the label of the plot
    
    plt.show()

'''
colomaps in matplotlib:

Name		 	Reverse	

Accent		 	Accent_r	
Blues		 	Blues_r	
BrBG		 	BrBG_r	
BuGn		 	BuGn_r	
BuPu		 	BuPu_r	
CMRmap		 	CMRmap_r	
Dark2		 	Dark2_r	
GnBu		 	GnBu_r	
Greens		 	Greens_r	
Greys		 	Greys_r	
OrRd		 	OrRd_r	
Oranges		 	Oranges_r	
PRGn		 	PRGn_r	
Paired		 	Paired_r	
Pastel1		 	Pastel1_r	
Pastel2		 	Pastel2_r	
PiYG		 	PiYG_r	
PuBu		 	PuBu_r	
PuBuGn		 	PuBuGn_r	
PuOr		 	PuOr_r	
PuRd		 	PuRd_r	
Purples		 	Purples_r	
RdBu		 	RdBu_r	
RdGy		 	RdGy_r	
RdPu		 	RdPu_r	
RdYlBu		 	RdYlBu_r	
RdYlGn		 	RdYlGn_r	
Reds		 	Reds_r	
Set1		 	Set1_r	
Set2		 	Set2_r	
Set3		 	Set3_r	
Spectral		Spectral_r	
Wistia		 	Wistia_r	
YlGn		 	YlGn_r	
YlGnBu		 	YlGnBu_r	
YlOrBr		 	YlOrBr_r	
YlOrRd		 	YlOrRd_r	
afmhot		 	afmhot_r	
autumn		 	autumn_r	
binary		 	binary_r	
bone		 	bone_r	
brg		 	    brg_r	
bwr		 	    bwr_r	
cividis		 	cividis_r	
cool		 	cool_r	
coolwarm		coolwarm_r	
copper		 	copper_r	
cubehelix		cubehelix_r	
flag		 	flag_r	
gist_earth		gist_earth_r	
gist_gray		gist_gray_r	
gist_heat		gist_heat_r	
gist_ncar		gist_ncar_r	
gist_rainbow	gist_rainbow_r	
gist_stern		gist_stern_r	
gist_yarg		gist_yarg_r	
gnuplot		 	gnuplot_r	
gnuplot2		gnuplot2_r	
gray		 	gray_r	
hot		 	    hot_r	
hsv		 	    hsv_r	
inferno		 	inferno_r	
jet		 	    jet_r	
magma		 	magma_r	
nipy_spectral	nipy_spectral_r	
ocean		 	ocean_r	
pink		 	pink_r	
plasma		 	plasma_r	
prism		 	prism_r	
rainbow		 	rainbow_r	
seismic		 	seismic_r	
spring		 	spring_r	
summer		 	summer_r	
tab10		 	tab10_r	
tab20		 	tab20_r	
tab20b		 	tab20b_r	
tab20c		 	tab20c_r	
terrain		 	terrain_r	
twilight		twilight_r	
twilight_shifted	twilight_shifted_r	
viridis		 	viridis_r	
winter		 	winter_r


'''

#tells you how to add size and alpha(tranparency) of the scatter points
def size_and_alpha():
    print("This is a scatter plot function")
    #example of scatter plot
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
    sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
    
    plt.scatter(x,y, c=colors, cmap = 'plasma', s = sizes, alpha = 0.5, label = 'Test') #s is the size of the marker, alpha is the transparency of the marker
    
    plt.title("Diffrence b/w car's age and speed", loc='center')
    plt.xlabel("Age of Cars", loc='center')
    plt.ylabel("Speed of Cars", loc='center')

    plt.colorbar() #to add and show the color bar with the drawing
    plt.legend() #to show the legend of the plot - means the label of the plot

    plt.show()





