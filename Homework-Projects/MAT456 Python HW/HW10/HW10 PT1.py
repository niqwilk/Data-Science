import numpy as np
import csv


from bokeh.plotting import figure, show, output_file, vplot

def main():
    
    compsci = getData("Computer Science")
    
    mathstat = getData("Math and Statistics")
    
    year = getData("Year")
    
    


    output_file("Math and Comp Sci Majors.html", title="stocks.py example")

    p1 = figure(title_text_font_size='14pt')

    p1.line(year, compsci, color='#B3DE69', legend='Comp. Sci.',line_width=2)
    p1.line(year, mathstat, color='firebrick', legend='Math and Stat',line_width=2)


    p1.title = "Percent of Math/Comp Sci Degrees Earned by Women"
    p1.grid.grid_line_alpha=0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Percentage'
    p1.legend.orientation = "top_left"
    



    window_size = 30
    window = np.ones(window_size)/float(window_size)
    show(p1)  # open a browser

def getData(specific):
    f = open("percent-bachelors-degrees-women-usa.csv")
    reader = csv.DictReader(f)
    coord = [float(row[specific]) for row in reader]
    f.close()
    return coord


main()

'''
p2.title = "AAPL One-Month Average"
p2.grid.grid_line_alpha=0
p2.xaxis.axis_label = 'Date'
p2.yaxis.axis_label = 'Price'
p2.ygrid.band_fill_color="olive"
p2.ygrid.band_fill_alpha = 0.1'''


