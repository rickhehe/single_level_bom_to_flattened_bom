import pandas as pd
import re
import os 

def aio(raw='raw_sample'):
    '''It reads individule csv file to a DataFrame, inserts a parent columns, then put all records into to one csv file.
       aio stands for all-in-one. 
    '''
    def rs(stream):
        '''my first generator
        '''
        for i in stream:
            df = pd.read_csv(f'{raw}\{i}')
            df.insert(0, 'parent', i.replace('.csv', ''))
            yield df

    return pd.concat( rs(os.listdir(raw)) )

def transform(df):

    reference = df.copy()
    ap_container = []

    count = 0
    while 1:
        # If a child columns doesn't appear in the parent column, it's unbreakable.
        # Those unbreakables shall be sent to the container.
        breakables = df[df.child.isin(reference.parent)]

        ap_container.append( df[~df.child.isin(reference.parent)] )

        if breakables.empty:
            return pd.concat(ap_container)

        # expansion
        merged = breakables.merge(reference, left_on = 'child', right_on = 'parent')
        merged['quantity'] = merged['quantity_x'] * merged['quantity_y']
        merged.drop(columns = ['child_x', 'quantity_x', 'parent_y', 'quantity_y'], inplace = True)
        merged.columns = ['parent', 'child', 'quantity']

        df = merged

def get_pcq(df):

    grouped = df.groupby(['parent', 'child']).sum()
    grouped.reset_index(inplace = True)

    return grouped

transformed = transform(aio())
pcq = get_pcq(transformed) #pcq stands for parent-child-quantity

if __name__ == '__main__':
    print(pcq)
    pcq.to_csv('flattened.csv', index=None)
