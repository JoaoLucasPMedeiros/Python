# CALCULO DE DATAS

# datetime - data e minutos

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


# CALCULO DE DIFERENÇA
fmt   = '%d-%m-%Y'

dataAtual = datetime.today()
dataFim    = (dataAtual - timedelta(days=60))
diferenca  = dataAtual - dataFim
delta = relativedelta(dataAtual, dataFim )
print(f'{delta.days} dias')
print(f'{delta.months} mes')
