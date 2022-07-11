# %%
import pandas as pd
import os


class LenColumnsException(Exception):
    pass


class DataColumnsException(Exception):
    def __init__(self, month):
        self.month = month


class DataColumnsException(Exception):
    pass


# %%
# Compruebe que el fichero existe y que tiene 12 columnas, una para cada mes
#  del año.
try:
    df = pd.read_csv(os.getcwd()+'\\finanzas2020[1].csv', sep='\t')
except FileNotFoundError:
    print('El archivo no existe en la dirección especificada. Por favor, \
ingrese la dirección correcta.')

try:
    if len(df.columns) != 12:
        raise(LenColumnsException)
except LenColumnsException:
    print('El archivo no contiene 12 columnas')


# Para cada mes compruebe que hay contenido.
try:
    nulls = df.notnull().sum()
    months = [nulls.index[x]
              for x in range(len(df.columns)) if nulls[x] == 0]
    if len(months) > 0:
        raise(DataColumnsException(months))
except DataColumnsException as ex:
    month = ex.args[0]
    if len(month) == 1:
        print('La columna del mes de', month[0], 'no tiene datos.')
    else:
        string = ', '.join(month[:-1]) + ' y ' + month[-1]
        print('Las columnas de los siguientes meses no tienen datos: ', string)


# Compruebe que todos los datos son correctos. De no haber un dato correcto,
#  el programa debe saber actuar en consecuencia y continuar con su ejecución.

df = df.apply(lambda columna: pd.to_numeric(columna, errors='coerce'))
# df.fillna(0, inplace=True)
nans = df.isna().any()
months = [nans.index[x] for x in range(len(df.columns)) if nans[x]]

if len(months) > 0:
    print('La/s columna/s contine/n valores no numéricos: ', ' - '.join(months))
    print('Los datos serán ignorados en el cálculo. Por favor corregirlos.')

# %%
# ¿Qué mes se ha gastado más?
gastos = df[df < 0]  # df.clip(upper=0)
mes_mas_gasto = gastos.sum().sort_values(ascending=True)
print(f'El mes que más gastó fue {mes_mas_gasto.index[0]} gastando \
${abs(mes_mas_gasto.values[0])}')


# %%
# ¿Qué mes se ha ahorrado más?
mes_mas_ahorro = df.sum().sort_values(ascending=False)
print(f'El mes que más ahorró fue {mes_mas_ahorro.index[0]} ahorrando $\
{abs(mes_mas_ahorro.values[0])}')

# %%
# ¿Cuál es la media de gastos al año?
gastos = df[df < 0]
media_gastos = gastos.stack().dropna().mean()
print(f'La media de gastos fue de ${abs(media_gastos): .2f}')

# %%
# ¿Cuál ha sido el gasto total a lo largo del año?
print(f'Los gastos totales en el año fueron ${abs(gastos.sum().sum()): .2f}')


# %%
# ¿Cuál ha sido el gasto total a lo largo del año?
ingresos = df[df > 0].sum()
print(f'Los ingresos totales en el año fueron ${abs(ingresos.sum()): .2f}')

pd.DataFrame(ingresos, columns=['Ingresos']).plot.bar(
    color='g', figsize=(10, 6))


# %%
