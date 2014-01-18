class Crosstab(object):
    """Compute a simple cross-tabulation of two (or more) factors.

    Parameters
    ----------
    df : dataframe object to be crosstabulated
    rows : list of values to group by in the rows
    cols : list of values to group by in the columns
    values : list values to aggregate
    """
    def __init__(self, df, rows, cols, values):
        dataframe = df.groupby(rows + cols).sum()[values].unstack(cols)
        self.dataframe = dataframe
