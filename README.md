实体和关系用localname或globalname表示

query为"gulf war"的字符串形式

通过mention查找实体
python run.py --fe "gulf war"

查看实体的关系
python run.py --qr m.0b1g9d

查找实体和query相关的关系
python run.py --fr m.0b1g9d "found"

查看主语关系的谓词
python run.py --qo m.0cm03 royalty.noble_person.titles 

查看主语关系所有谓词的一跳子图
python run.py --qohber m.0cm03 government.politician.government_positions_held

配置:
sparql.py中的sparql_util_conf['sparql_url']配置为sparql的http终端
sparql_util_conf['proxies']配置为本地代理的地址
sparql_util_conf['entity_link_conf']['key']配置为google-api的key
