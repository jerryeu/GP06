import pandas as pd
import matplotlib.pyplot as plt

class calUtils:
    def visit(self):
        #dictionary for total amount of visitors in countries
        dict = {"country": ['United Kingdom','Germany','France','Italy','Netherlands','Greece','Belgium & Luxembourg','Switzerland','Austria','Scandinavia','CIS & Eastern Europe'],
                "sum": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}


        newDf = pd.DataFrame(dict, columns=['country', 'sum'])
        # Import the IMVA.csv data to df
        df = pd.read_csv('IMVA.csv')
        visitor = df['Periods'].str.split(' ', n=2, expand=True)
        # assign new column called year
        df = df.assign(year=visitor[1])
        # set year as index
        df.index = df['year']
        # delete periods column
        del df['Periods']
        # delete year column
        del df['year']
        #select european countries
        df = df[df.columns[18:29]].head(400)
        # select year 1988 to 1997
        df = df.iloc[122:240]

        df = df.replace(' na ', 0)
        print(df)

        #Add visitors data for span of 10 years
        uk = df[' United Kingdom '].sum()
        germany = df[' Germany '].sum()
        france = df[' France '].sum()
        italy = df[' Italy '].sum()
        netherlands = df[' Netherlands '].sum()
        greece = df[' Greece '].sum()
        belguim = df[' Belgium & Luxembourg '].sum()
        switzerland = df[' Switzerland '].sum()
        austria = df[' Austria '].sum()
        scandinavia = df[' Scandinavia '].sum()
        cIS = df[' CIS & Eastern Europe '].sum()

        #input into dataFrame
        newDf['sum'] = newDf['sum'].replace(1, germany)
        newDf['sum'] = newDf['sum'].replace(2, france)
        newDf['sum'] = newDf['sum'].replace(3, italy)
        newDf['sum'] = newDf['sum'].replace(4, netherlands)
        #df['sum'] = df['sum'].replace(5, 0)
        #df['sum'] = df['sum'].replace(6, 0)
        newDf['sum'] = newDf['sum'].replace(7, switzerland)
        #df['sum'] = df['sum'].replace(8, 0)
        newDf['sum'] = newDf['sum'].replace(9, scandinavia)
        newDf['sum'] = newDf['sum'].replace(10, cIS)

        #Sort by top3 most visited countries
        newDf.sort_values(by=['sum'], inplace=True, ascending=False)
        #reset index
        newDf.reset_index(drop=True, inplace=True)

        #filter top3 from dataframe
        top3 = newDf.nlargest(3, 'sum')
        print(top3)

        #plot graph to show top 3
        ax = top3.plot(kind='bar', x='country', y='sum', title="Number of Visitors in Countries",
                        ylabel="Number of Tourists (in millions) ", rot=0, legend=False, figsize=(15, 15))
        for p in ax.patches:
            ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
        plt.savefig("Top3.png")
        # plt.show()

        # All countries in Europe
        ax = newDf.plot(kind='bar', x='country', y='sum', title="Number of Visitors in Countries",
                     ylabel="Number of Tourists (in millions) ", rot=45, legend=False, figsize=(25, 25))
        for p in ax.patches:
            ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
        plt.savefig("Country_comparison.png")
        # plt.show()




k = calUtils()
k.visit()

