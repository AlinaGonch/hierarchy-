import pandas as pd

data = pd.read_csv('category_names (1).csv', sep=',')
df = data[['category_level1', 'category_level2', 'category_level3', 'category_id']]
rows = df.iloc[1:6]

# def build_hierarchy(dataframe):
#     hierarchy = {}
#     columns = dataframe.columns.tolist()
#     print(columns)
#     for index, row in dataframe.iterrows():
#         fill_hierarchy(columns, row, hierarchy)
#         # top_category = row['category_level1']
#         # if top_category not in hierarchy:
#         #     hierarchy[top_category] = {}

#         # subhierarchy = hierarchy[top_category]
#         # subcategory = row['category_level2']
#         # if subcategory not in subhierarchy:
#         #     subhierarchy[subcategory] = []

#         # subhierarchy[subcategory].append(row['category_id'])
#     return hierarchy

# def fill_hierarchy(columns, row, hierarchy):
    # for column in range(len(columns)):
    #     key = row[columns[column]]
    #     end_point = len(row.index.tolist())
    #     if  column != end_point:
    #         if key not in hierarchy:
    #             hierarchy[key] = {} 
    #             fill_hierarchy(columns[:end_point], row, hierarchy[key])
    #     else:
    #         if key not in hierarchy:
    #             hierarchy[key] = []
            

def fill_hierarchy(columns, row, hierarchy):
    if isinstance(hierarchy, list):
        first_element = columns.pop(0)
        key = row[first_element]
        hierarchy.append(key)
        
    if len(columns) == 2:
        first_element = columns.pop(0)
        key = row[first_element]
        if key not in hierarchy:
            hierarchy[key] = []
            fill_hierarchy(columns, row, hierarchy[key])


    if len(columns) == 0 or len(columns) == 1:
        return hierarchy

    first_element = columns.pop(0)
    key = row[first_element]
    if key not in hierarchy:
        hierarchy[key] = {}
        fill_hierarchy(columns, row, hierarchy[key])
  

   

def build_hierarchy(dataframe):
    hierarchy = {}
    columns = dataframe.columns.tolist()
    for index, row in dataframe.iterrows():
        print(row)
        new_dict = fill_hierarchy(columns, row, hierarchy)
        print(new_dict)



print(build_hierarchy(rows))

