import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('state_trans.csv', low_memory=False)
fig = go.Figure(data=go.Choropleth(
    locations=df['state'], # 设置位置，各州的编号（缩写）
    z = df['transaction'].astype(float), # 设置填充色数据
    locationmode = 'USA-states', # 设置国家名称
    colorscale = 'algae', # 图例颜色
    colorbar_title = "总金额", # 图例标题
))

fig.update_layout(
    title_text = '美国各州捐款总金额', # 地图标题
    geo_scope='usa', # 设置地图的范围为美国
)
fig.write_image("US.jpg")

# 所有可用颜色
# ['aggrnyl'深绿色》黄色,
# 'agsunset'紫色》肉色,
# 'algae',浅绿色》深绿色
# 'amp',淡红色》深红色
# 'armyrose',土黄色》肉色》桃粉色
# 'balance',深蓝色》浅蓝色》浅红色》深红色
# 'blackbody',深红色》黄色》浅蓝色
# 'bluered',蓝色》红色
# 'blues',淡蓝的》深蓝色
# 'blugrn',
# 'bluyl',
# 'brbg',
# 'brwnyl',
# 'bugn',
# 'bupu',
# 'burg',
# 'burgyl',
# 'cividis',
# 'curl',
# 'darkmint',
# 'deep',
# 'delta',深蓝色》透明》黄色》深绿色
# 'dense',
# 'earth',
# 'edge',
# 'electric',
# 'emrld',
# 'fall',
# 'geyser',
# 'gnbu',
# 'gray',
# 'greens',
# 'greys',
# 'haline',
# 'hot',
# 'hsv',
# 'ice',
# 'icefire',
# 'inferno',
# 'jet',
# 'magenta',
# 'magma',
# 'matter',
# 'mint',
# 'mrybm',
# 'mygbm',
# 'oranges',
# 'orrd',
# 'oryel',
# 'oxy',
# 'peach',
# 'phase',
# 'picnic',
# 'pinkyl',
# 'piyg',
# 'plasma',
# 'plotly3',
# 'portland',
# 'prgn',
# 'pubu',
# 'pubugn',
# 'puor',
# 'purd',
# 'purp',
# 'purples',
# 'purpor',
# 'rainbow',
# 'rdbu',
# 'rdgy',
# 'rdpu',
# 'rdylbu',
# 'rdylgn',
# 'redor',
# 'reds',
# 'solar',
# 'spectral',
# 'speed',
# 'sunset',
# 'sunsetdark',
# 'teal',
# 'tealgrn',
# 'tealrose',
# 'tempo',
# 'temps',
# 'thermal',
# 'tropic',
# 'turbid',
# 'turbo',
# 'twilight',
# 'viridis',
# 'ylgn',
# 'ylgnbu',
# 'ylorbr',
# 'ylorrd'].