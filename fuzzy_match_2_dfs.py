import pandas as pd
from fuzzywuzzy import process, fuzz

testdata1 = {'Animal':['Cat','Dog','Bunny','Squirrel','Hamster'],'ID':['A1','B2','C3','D4','E5']}
testdata1_df = pd.DataFrame.from_dict(testdata1)

testdata2 = {'Animal':['Doggie','Bunny Rabbit','Cats','Squirrel','Hammie'],'ID':['G1','H2','I3','J4','K5']}
testdata2_df = pd.DataFrame.from_dict(testdata2)

testdata2_df['matches'] = testdata2_df['Animal'].apply(lambda x: process.extractOne(x, testdata1_df['Animal'], scorer=fuzz.partial_ratio, score_cutoff=88))
testdata2_df[['Match','Score','Data1Index']] = pd.DataFrame(testdata2_df['matches'].tolist(), index=testdata2_df.index)
combo = testdata2_df.merge(testdata1_df, left_on='Match', right_on='Animal')
