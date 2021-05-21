def derive_nth_day_feature(df, feature, N):
    rows = df.shape[0]
    nth_prior_measurements = [None]*N + [df[feature][i-N] for i in range(N, rows)]
    col_name = "{}_{}".format(feature, N)
    df[col_name] = nth_prior_measurements


def dataframe_sort(df):
    for feature in df:
        if feature != 'Data':
            for N in range(1, 4):
                derive_nth_day_feature(df, feature, N)

    return df
