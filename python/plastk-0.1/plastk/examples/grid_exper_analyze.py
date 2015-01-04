#!/usr/bin/env python
"""
An analysis script for the grid experiment.  This
script loads the data files generated by grid_exper.py and plots the average
cumulative cost (i.e. episode length) per episode for each of the four
conditions.  The resulting graph shows that for both the large and the
small grids, optimistic initialization, has a higher up-front cost
(due to its greater exploration of the envionment), but lower
cumulative cost in the long term, because the extra exploration allows
it to converge to a cheaper solution in the long term.

$Id: grid_exper_analyze.py 233 2008-03-03 16:50:30Z jprovost $
"""
from grid_exper import exp as grid_exp
from plastk.misc import pkl

from pylab import *
from numpy import array,transpose


def main():
    # Loop over the conditions and read the saved episode length data from
    # each trial in each condition
    for c in grid_exp.conditions:
        print "Condition %s, %s:"%(c['grid_name'],c['init_name']),
        names = pkl.files_matching(grid_exp.filestem(c)+'-*.pkl.gz')
        print "loading",len(names),"files."
        ll = c['length'] = array([pkl.load(n)['length'][:] for n in names])
        # compute the cumulative length for each trial
        c['cost'] = cumsum(c['length'],axis=1)

        plot(average(c['cost'],axis=0),linestyle='-',
                     label='%s, %s'%(c['grid_name'],c['init_name']))
        legend(loc='upper left')
        xlabel('Episodes')
        ylabel('Cumulative Cost')
        title('Cost Comparison, Optimistic v. Pessimistic Init.')
    show()

if __name__=='__main__':
    main()
