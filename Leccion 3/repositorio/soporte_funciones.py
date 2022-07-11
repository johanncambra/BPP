import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from scipy.stats import multivariate_normal
seed = 22518


def FilterOutliers(df_datos: pd.DataFrame, variables: list,  metodos: dict) -> None:
    """Función para encontrar outliers:
    Se aplican los metodos indicados en df_datos y los resultados se almacenan 
    en df_datos, una columna binaria por cada método aplicado.

    Metodos disponibles a utilizar:
    _ IsolationForest: {'IsolationForest':{ 'contamination': 0.05 }}
    _ AnomaliasMultiGauss: {'AnomaliasMultiGauss':{ 'quantileN': 0.05 }}

    Args:
        df_datos (pd.DataFrame): dataframe con los datos procesar.
        variables (list): lista con las variables a buscar outliers, deben estar
                        incluidas en las columnas de df_data.
        metodos (dict(dict)): dict_1[dict_2]. dict_1 tiene como claves los 
                            los metodos a utilizar y como value tiene el dict_2
                            con los parámetros del metodo. 
    """
    # se chequean si los datos ingresados cumplen con la tipologia declarada
    try:
        assert isinstance(df_datos, pd.DataFrame) == True, 'df_datos: '
        assert isinstance(variables, list) == True, 'variables: '
        assert isinstance(metodos, dict) == True, 'metodos: '
    except Exception as e:
        print(f'{e} revisar los tipos de lo datos ingresados.')
        return

    # se dejan las variables a procesar que se encuentran en el dataframe
    variables = list(set(variables) - set([var for var in variables if var
                                           not in df_datos.columns]))

    # se chequea si hay datos
    if len(variables) == 0:
        print('Las variables ingresadas no se encuentran en el Dataframe.')
        return
    if df_datos.shape[0] < 3:
        print('Insuficientes datos en el Dataframe.')
        return

    # se encuentran los outliers
    for key in metodos.keys():

        if key == 'IsolationForest':
            model = IsolationForest(contamination=metodos[key]['contamination'],
                                    random_state=seed)
            df_datos.loc[:, 'IsolationForest'] = model.fit_predict(
                df_datos[variables].values)
            df_datos['IsolationForest'].replace(
                {-1: True, 1: False}, inplace=True)

        if key == 'AnomaliasMultiGauss':
            mean = np.mean(df_datos[variables])
            sigma2 = 1*np.cov(df_datos[variables], rowvar=False)
            pdfData = multivariate_normal.pdf(
                df_datos.loc[:, variables].values, mean=mean.values,
                cov=sigma2, allow_singular=True)
            pdfDataNorm = pdfData/np.max(pdfData)
            threshold = np.quantile(pdfDataNorm, metodos[key]['quantileN'])
            df_datos['AnomaliasMultiGauss'] = False
            df_datos.loc[pdfDataNorm < threshold, 'AnomaliasMultiGauss'] = True

    return


def Smape(a, f) -> float:
    """Symmetric mean absolute percentage error

    Args:
        a ( 1D numpy array o casteable ): Actual Value
        f (1D numpy array o casteable ): Forescast Value

    Returns:
        float: porcentaje de error entre 0% y 100%
    """
    return 100/len(a) * np.sum(np.abs(f-a) / (np.abs(a) + np.abs(f)))


def PlotDataModel(df_train, df_test, target, showplot=True, path=None) -> None:
    """PlotDataModel:
    Función para graficar sns.countplot(), sns.violinplot(), sns.kdeplot()
    y sns.boxplot() de la variable target. Se grafica un subplot con los 4 graficos.

    Args:
        df_train (pd.DataFrame): Dataframe con los dados de entremaniemto
        df_tets (pd.DataFrame): Dataframe con los dados de tets
        target (str): Variable que se quiere describir
        showplot (bool): True o False si se quiere mostrar los resultados
        path (path, optional): Ruta para guardar resultados. Defaults to None.
    """

    if path == None and showplot == False:
        return

    if target in df_train.columns and target in df_test.columns:
        df = pd.DataFrame({'COT': df_train[target], 'Label': 'Train'}).append(
            pd.DataFrame({'COT': df_test[target], 'Label': 'Test'}))
    elif target in df_train.columns and not target in df_test.columns:
        df = pd.DataFrame({'COT': df_train[target], 'Label': 'Train'})
        print(f'Los datos de test no continen la columna {target}')
    elif target in df_test.columns and not target in df_train.columns:
        df = pd.DataFrame({'COT': df_test[target], 'Label': 'Test'})
        print(f'Los datos de entrenamientos no continen la columna {target}')
    else:
        print(f'No se encontró la columna {target}en los datos pasados.')
        return

    fig, (ax1, ax2) = plt.subplots(ncols=2, nrows=2, figsize=(10, 8))
    plt.ion()
    sns.countplot(data=df, x="Label", ax=ax1[0])
    sns.violinplot(data=df, x='Label', y='COT', linewidth=1.5, ax=ax1[1])
    sns.kdeplot(data=df, x='COT',  hue='Label', multiple="stack", ax=ax2[0])
    sns.boxplot(data=df, y='Label', x='COT', ax=ax2[1])
    plt.suptitle('Descripción datos Train an Test', fontsize=18)
    plt.tight_layout()
    if showplot:
        plt.show()
    plt.close()

    if path is not None:
        fig.savefig(path / 'describe_train_test_data.png', dpi=250)

    return
