"""
Creates a heatmap (matplotlib figure) from a csv file.
Author: Tyler Radke
Date: Aug. 3, 2022

Citation:   Calplot Documentation
            https://calplot.readthedocs.io/en/latest/

Citation:   Calplot Customization
            https://thiago-bernardes-carvalho.medium.com/calendar-heatmaps-with-pythons-calplot-b4dec29ee805
"""

import csv
import pandas as pd
import calplot

def main():

    # Load data from csv.
    dict_date_racecount = csv_extract()
    
    # Create heatmap.
    create_heatmap(dict_date_racecount)
        
    return

def csv_extract():
    """
    Organizes data from a CSV into a dictionary (date:race)
    Return: Dict (str:int)
    """

    # Set filename and the column number of date.
    filename = 'race-date-time.csv'
    col = 1

    # Load csv data into dictionary.
    dict_date_racecount = {}
    with open(filename, newline='') as f:
        reader = csv.reader(f)

        # Skip first "header" row.
        next(reader)
        for row in reader:
            dict_date_racecount[row[col]] = dict_date_racecount.setdefault(row[col], 0) + 1

    return dict_date_racecount

def create_heatmap(dict_date_racecount):
    """
    Adjusts datatypes to be compatible with Calplot
    Customize and save heatmap (matplotlib figure)
    Return: None
    """

    # Split dictionary into lists.
    values = []
    dates = []
    for key in dict_date_racecount.keys():
        dates.append(key)
        values.append(dict_date_racecount[key])

    # Dates must be a DatetimeIndex object for pandas.Series().
    dti = pd.DatetimeIndex(dates)
    events = pd.Series(values, index=dti)

    # Customize heatmap.
    grey = '#646464'
    title_str = "Races Heatmap"
    title_args = {"color":"white", "fontsize":36, "y":1.1}
    yearlabel_args = {'color': 'white'}
    fig_args = {"facecolor":grey}
    colormap = 'viridis'

    # Calplot constructs & returns heatmap (matplotlib figure, axes).
    fig, axes = calplot.calplot(events,
                                yearlabel_kws=yearlabel_args,
                                suptitle=title_str,
                                suptitle_kws=title_args,
                                fig_kws=fig_args,
                                edgecolor="black",
                                linewidth=1,
                                cmap=colormap
                                )

    # Customize axes lables.
    for ax in axes:
        ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], color='w')
        ax.set_yticklabels(["Mon","","","","","",""],color='w')
    
    # Save Figure.
    fig.savefig("./figs/heatmap.png", bbox_inches="tight", transparent=False)

    return


main()
