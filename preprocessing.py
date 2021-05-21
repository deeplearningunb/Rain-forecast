def derive_nth_day_feature(df, feature, N):
    rows = df.shape[0]
    nth_prior_measurements = [None] * N + [df[feature][i - N] for i in range(N, rows)]
    col_name = "{}_{}".format(feature, N)
    df[col_name] = nth_prior_measurements


def dataframe_sort(df):
    # make list of original features without meantempm, mintempm, and maxtempm
    to_remove = [feature
                 for feature in df
                 if feature not in ['Precipitacao', 'TempBulboSeco', 'TempBulboUmido', 'TempMaxima', 'TempMinima',
                                    'UmidadeRelativa', 'PressaoAtmEstacao', 'PressaoAtmMar', 'DirecaoVento',
                                    'VelocidadeVento', 'Insolacao', 'Nebulosidade', 'Evaporacao Piche',
                                    'Temp Comp Media', 'Umidade Relativa Media', 'Velocidade do Vento Media']]

    # make a list of columns to keep
    to_keep = [col for col in df.columns if col not in to_remove]

    # select only the columns in to_keep and assign to df
    df = df[to_keep]

    for feature in df:
        if feature != 'Data':
            for N in range(1, 4):
                derive_nth_day_feature(df, feature, N)

    return df
