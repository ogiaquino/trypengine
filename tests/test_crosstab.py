import os
import unittest
import pandas as pd
import numpy as np

from pandas.util.testing import assert_frame_equal
from trypengine.crosstab import Crosstab

data_loc = os.path.dirname(os.path.abspath(__file__)) + '/data'


class TestCrosstab(unittest.TestCase):
    def test_crosstab(self):
        df = pd.read_csv('%s/fixture.csv' % data_loc)

        rows = ['region', 'area', 'distributor']
        cols = ['salesrep', 'retailer']
        values = ['sales', 'target']

        ct = Crosstab(df, rows, cols, values).dataframe.sort(axis=0)
        ct = ct.sort(axis=1)
        pv = df.pivot_table(rows=rows, cols=cols, values=values,
                            aggfunc=np.sum).sort(axis=0)
        pv = pv.sort(axis=1)
        assert ct.columns.tolist() == pv.columns.tolist()
        assert ct.index.tolist() == pv.index.tolist()
        assert ct.fillna(0.0).values.tolist() == pv.fillna(0.0).values.tolist()
        assert_frame_equal(ct, pv)
