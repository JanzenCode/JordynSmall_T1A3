import matplotlib.pyplot as plt 
import numpy as np
import datetime
from matplotlib.backends.backend_pdf import PdfPages
# import main

def fig_barh(ylabels, xvalues, title='User Investment Data Graphed'):
    # create a new figure
    fig = plt.figure()

    # plot to it
    yvalues = 0.1 + np.arange(len(ylabels))
    plt.barh(yvalues, xvalues, figure=fig)
    yvalues += 0.4
    plt.yticks(yvalues, ylabels, figure=fig)
    if title:
        plt.title(title, figure=fig)

    # return it
    return fig

def write_pdf(fname, figures):
    doc = PdfPages(fname)
    for fig in figures:
        fig.savefig(doc, format='pdf')
    doc.close()

def main():
    a = fig_barh(['a','b','c'], [1, 2, 3], 'Test #1')
    b = fig_barh(['x','y','z'], [5, 3, 1], 'Test #2')
    write_pdf('test.pdf', [a, b])

if __name__=="__main__":
    main()



# time = datetime.datetime.now()
# timestr = input("Input years: ")
# timeint= int(timestr)
# years = time.year + timeint






