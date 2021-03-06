import pandas as pd
import matplotlib.pyplot as plt

def setGraphProps(datatsetPath):
    global graphsProp
    graphsProp = pd.read_csv(datatsetPath,';')

def noOfVertices():
    verOccu = graphsProp['vertices'].value_counts()
    sixPlus = 0
    #print(type(verOccu))
    for keys in verOccu.keys():
        #print(keys)
        if keys >= 6:
            #print([keys])
            sixPlus = sixPlus + verOccu[keys]
            verOccu = verOccu.drop(keys)

    verOccu = verOccu.sort_index()   
    verOccu['6+'] = sixPlus
    verOccu.plot(kind='bar', 
                 xlabel='Vertices', 
                 ylabel='Occurence',
                 title='Number of vertices by refactoring subgraph')

    
def noOfEdges():
    edgeOccu = graphsProp['edges'].value_counts()
    fivePlus = 0
    # print(type(verOccu))
    for keys in edgeOccu.keys():
    #     print(keys)
        if keys >= 5:
    #         print([keys])
            fivePlus = fivePlus + edgeOccu[keys]
            edgeOccu = edgeOccu.drop(keys)

    edgeOccu = edgeOccu.sort_index()   
    edgeOccu['5+'] = fivePlus
    edgeOccu.plot.bar(xlabel='Edges', ylabel='Occurence', title='Number of edges by refactoring subgraph')
    edgeOccu

def noOfCommits():
    commitOccu = graphsProp['commits'].value_counts()
    fivePlus = 0
    # print(type(verOccu))
    for keys in commitOccu.keys():
    #     print(keys)
        if keys >= 5:
    #         print([keys])
            fivePlus = fivePlus + commitOccu[keys]
            commitOccu = commitOccu.drop(keys)

    commitOccu = commitOccu.sort_index()   
    commitOccu['5+'] = fivePlus
    commitOccu.plot.bar(xlabel='Commits', ylabel='Occurence', title='Number of commits by refactoring subgraph')
    commitOccu

def ageRefactorinmgGraph():
    slimedProp = graphsProp[['project','age_days']].copy()
    slimedProp.groupby('project').boxplot(column='age_days', figsize=(25,25))

# # (RQ4) Which Refactorings Compose the Refactoring Sub-graphs?

# With the generated data from the previous scripts by authors it is not possible to count the frequency of the refactoring operations.

# # (RQ5) Are the Refactoring Subgraphs Created by the Same or Multiple Developers?

# Dosent seems to work at the moment

# proDevProp = graphsProp[['project','developers']].copy()

# devProDict = {}
# for index, row in proDevProp.iterrows():
#     if row['developers'] > 1:
        
#         if row['project'] not in devProDict: 
#             devProDict[row['project']] = {}
#             devProDict[row['project']]['m'] = 0
            
#         if "m" in devProDict[row['project']]:
#             devProDict['m'] = devProDict['m'] + 1
#         else:
#             devProDict['m'] = 0
#             devProDict['m'] = devProDict['m'] + 1
#     else:
#         if row['project'] not in devProDict: 
#             devProDict[row['project']]['s'] = 0
            
#         if "s" in devProDict[row['project']]:
#             devProDict['s'] = devProDict['s'] + 1
#         else:
#             devProDict['s'] = 0
#             devProDict['s'] = devProDict['s'] + 1
        
# devProList

