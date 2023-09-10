import pandas as pd
from sqlalchemy import create_engine

# 读取Excel数据
excel_file = r'C:\Users\开心\Desktop\2023赛题\fj2.xlsx'
df = pd.read_excel(excel_file)

# 连接到MySQL数据库
db_uri = 'mysql://root:123456@localhost:3306/excel1'
engine = create_engine(db_uri)

# 将数据插入MySQL数据库
table_name = 'ex'
df.to_sql(table_name, engine, if_exists='replace', index=False)

# 关闭数据库连接
engine.dispose()