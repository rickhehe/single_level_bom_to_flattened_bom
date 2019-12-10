What is a flattened BOM?

"Think of a flattened BOM as a list of all the parts from all levels of your BOM listed together and the aggregate total quantities for each part are shown. It¡¯s a great way to see the quantities of ALL Parts (no matter what level of the BOM they appear) with their summed quantities." ( https://help.openbom.com/2018/09/08/bom-single-level-multi-level-flattened/ )

Let's say you have a product a0, consists of 3 sub-assemblies, b1, b2 and b3. And you stroe the single level bom of a0 as a0.csv . 

    a0.csv: child quantity
            b1           1
            b2           2
            b3           3
       
also, b1 and b2 has their own single bom, while b3 is a part at the bottom level.
    
    b1.csv: child quantity
            c1           1
            c2           2

    b2.csv: child quantity
            c1           2
            c2           4

c1 consists of d1 and d2, while c2 is on its own.

    c1.csv: child quantity
            d1           4
            d2           8

In summary you have 4 csv files, or single-level boms, as input, this tool will give you one csv file, a flattened-bom, as output.

    flattened.csv: parent child quantity
                   a0     b3           3
                   a0     c2          10
                   a0     d1          20
                   a0     d2          40
                   b1     c2           2
                   b1     d1           4
                   b1     d2           8
                   b2     c2           4
                   b2     d1           8
                   b2     d2          16
                   c1     d1           4
                   c1     d2           8

If you have a customer, internal or external, who would like a dashboard built on excel spreadsheet (what a supprise) to show and/ or estimate raw material usage, this could easily be integreted using Power Query.
