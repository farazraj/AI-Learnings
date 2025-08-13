import matplotlib

def version():
    """Prints the version of matplotlib."""
    print("Matplotlib version:")
    print( matplotlib.__version__)

#common imports
import matplotlib.pyplot as plt
import numpy as np


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
