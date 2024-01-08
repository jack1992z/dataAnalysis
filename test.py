import pandas as pd
import vaex as vs
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
# import vaex as vx
import seaborn as sns 
import numpy as np
from scipy.stats import norm #使用直方图和最大似然高斯分布拟合绘制分布
import warnings 
warnings.filterwarnings('ignore') # 不发出警告
plt.rcParams["patch.force_edgecolor"] = True

import matplotlib as mpl
mpl.rcParams['lines.linewidth'] = 1
mpl.rcParams['lines.color'] = 'black'
mpl.rcParams['patch.linewidth'] = 1
mpl.rcParams['patch.edgecolor'] = 'black'
mpl.rcParams['axes.linewidth'] = 1
mpl.rcParams['axes.edgecolor'] = 'black'

# 设置y轴直方图，注意需要orientation参数
from scipy import stats

