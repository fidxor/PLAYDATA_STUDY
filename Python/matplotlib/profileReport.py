import seaborn as sns
# import pandas_profiling as pp
# 2023.4 부터 pasdas_profiling 대신 ydata_profiling 을 사용한다.
import ydata_profiling as yp

tips = sns.load_dataset('tips')

profile = yp.ProfileReport(tips)

profile.to_widgets() #jupyternotebook 에서는 to_widgets으로 아라에 표가 보여지지만.

profile.to_file('ypReport.html') # py파일에서는 데이터로 익스포트 한다음에 브라우저로 볼수 있다.