import pandas as pd
import deepdiff

def get_removed_objects(file1, file2):
    df1 = pd.read_json(file1)
    df2 = pd.read_json(file2)

    list1 = df1.to_dict(orient='records')
    list2 = df2.to_dict(orient='records')

    result = deepdiff.DeepDiff(list1, list2, ignore_private_variables=False, ignore_order=True, cutoff_distance_for_pairs=1, cutoff_intersection_for_pairs=1)

    removed_objects = []
    
    print (result)

    if 'iterable_item_removed' in result:
        for key, removed_object in result['iterable_item_removed'].items():
            removed_objects.append(removed_object)  

    return removed_objects

# Usage:
removed_objects = get_removed_objects('friendsList.json', 'friendsList copy.json')
if removed_objects:
    print("Friends removed:")
    for obj in removed_objects:
        print()
else:
    print("No objects removed.")


if removed_objects:
    for obj in removed_objects:
        name = obj.get('name')  
        if name:
            print(name)
            
