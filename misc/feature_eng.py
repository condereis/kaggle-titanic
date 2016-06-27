

# Creating an empty dataframe for new features.
new_features = pd.DataFrame()
split_df = full_data['Name'].str.split(', ',expand=True,n=1)
new_features['Title'] = split_df[1].str.split('. ',expand=True,n=1)[0]
new_features.loc[new_features.Title == 'Mme', 'Title'] = 'Mr'
new_features.loc[new_features.Title == 'Ms', 'Title'] = 'Miss'
new_features.loc[new_features.Title == 'Mlle', 'Title'] = 'Miss'
new_features.loc[new_features.Title == 'Mme', 'Title'] = 'Mr'
new_features.loc[new_features.Title.isin(['Rev', 'Dr', 'Col', 'Major', 'Lady', 'Don', 'Capt', 'Sir', 'Dona', 
                                        'Jonkheer','th']), 'Title'] = 'Rare'

surname_df = pd.DataFrame()
surname_df.loc[:,'Surname'] = split_df[0]
surname_df.loc[:,'Survived'] = pd.concat([train_data.Survived, test_data.Sex.replace(['male','female'],[0,1])], axis=0).reset_index(drop=True)
surname_df.loc[:,'SurvivingRelatives'] = 0
for i, row in surname_df.iterrows():
    if any((surname_df.drop(i).Surname==row.Surname) & (surname_df.drop(i).Survived==1)):
        surname_df.SurvivingRelatives.iloc[i]=1
new_features.loc[:,'SurvivingRelatives'] = surname_df.SurvivingRelatives
