# library

import pandas as pd
import numpy as np

## visualization
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Data Collection
## a. Import Data

data = pd.read_csv("/Users/youheekil/Desktop/projects/FIFA/FIFA_data.csv")
data.head(10)

pd.set_option('display.max_columns', 80)
data.head()


## b. Check data and establish a data analysis plan

### 1. Analyze about players of Manchester United - What kind of players are in Manchester United
### 2. Compare players stat with Manchester City, the rival team of Manchester United
### 3. Choose(select) two insufficient positions
### 4. (Virtually) Recruit two players from other teams with consideration of Manchester United's Finances, Feasiblity, and Recruitment policy

# -------------------------------------------------------------------  #

# 2. Analysis of Manchester United

### 1. Analyze about players of Manchester United - What kind of players are in Manchester United

## a. EDA

mu = data[data['Club'] == 'Manchester United']
mc = data[data['Club'] == 'Manchester City']


mu['Club'].unique()
mc['Club'].unique()
data['Club'].unique()

print(f"Number of MU Players: {mu.shape[0]}\n")
print(f"MU players' positions: {mu['Position'].unique()}\n")
print(f"MU players' average overall Stats: {mu['Overall'].mean()} \n")
print(f"MU players' average potential Stats: {mu['Potential'].mean()}\n")


### sns.countplot(data) - it's a function that calculates the number of data and draws it as a graph
sns.countplot(mu['Age'])
sns.countplot(mu['Position'])
mu.tail()



sns.boxplot(data = mu, x = 'Position', y = 'Overall') # it's a box plox about current overall stats per position


# There are two outstanding outliers in variable 'CB' - maybe it looks like a outlier because the downward outlier one was affected by the upper outlier one.

### outliers

mu[mu['Overall']>140] #since the graph showed the outlier lies at overall over 140. Let's check which player has 'overall' over 140.

mu[mu['Position']=="CB"][['Name', 'Overall', 'CB']] # M.Rojo and P. Jones have same scores of CB position and same Overall, we can assume that if score of CB position, Overall score might be the same

mu['Overall'][11422] = 75 # make overall of the [11422] player to 75
sns.boxplot(data = mu, x = 'Position', y = 'Overall') # then the existed outliers are gone !

sns.boxplot(data =mu, x="Position", y='Potential')


### Missing Values
mu.info()

mu[mu.isnull()['LS']]['Position'] #LS~RS parts are missing for players whose positions are 'GK'

mu = mu.fillna(-1) # replace NaN to '-1' meaning we cannot measure NaN value in this case

mu.info() #voila ! there you go ! no missing values anymore




# -------------------------------------------------------------------  #

# 3. which position should Manchester United reinforece?

### 2. Compare players stat with Manchester City, the rival team of Manchester United

df = data[(data['Club'] == 'Manchester United')|(data['Club'] == 'Manchester City')]
df.head()


df['Club'].unique() #check if data contains only 'MU' and 'MC' for Club

## Select MU and MC players for comparison - (GK:1, CB:4, MF:4, ST:2)
### Selection Criteria of main player is based on 'Overall'

df['Position'].unique()

gk_list =['GK']
cb_list =['CB', 'LCB', 'RCB', 'RB', 'LB']
mf_list =['RCM', 'LCM', 'CDM', 'CM', 'RM', 'CAM']
st_list =['ST', 'LW', 'RW']

st_count = 2
mf_count = 4
cb_count = 4
gk_count = 1

mu_id=[]


for index in mu.index :
    if mu['Position'][index] in gk_list :
        if gk_count != 0 :
            mu_id.append(mu['ID'][index])
            gk_count -= 1
    elif mu['Position'][index] in cb_list :
        if cb_count != 0 :
            mu_id.append(mu['ID'][index])
            mu['Position'][index] = 'CB'
            cb_count -= 1
    elif mu['Position'][index] in mf_list :
        if mf_count != 0 :
            mu_id.append(mu['ID'][index])
            mu['Position'][index] = 'MF'
            mf_count -= 1
    else :
        if st_count != 0 :
            mu_id.append(mu['ID'][index])
            mu['Position'][index] = 'ST'
            st_count -= 1


##isin() function 리스트 안에 있는 선수만 MU선수로 남는다

mu = mu[mu['ID'].isin(mu_id)]
mu.shape[0]

### Do the same thing for MC

st_count = 2
mf_count = 4
cb_count = 4
gk_count = 1

mc_id = []

for index in mc.index :
    if mc['Position'][index] in gk_list :
        if gk_count != 0 :
            mc_id.append(mc['ID'][index])
            gk_count -= 1
    elif mc['Position'][index] in cb_list :
        if cb_count != 0 :
            mc_id.append(mc['ID'][index])
            mc['Position'][index] = 'CB'
            cb_count -= 1
    elif mc['Position'][index] in mf_list :
        if mf_count != 0 :
            mc_id.append(mc['ID'][index])
            mc['Position'][index] = 'MF'
            mf_count -= 1
    else :
        if st_count != 0 :
            mc_id.append(mc['ID'][index])
            mc['Position'][index] = 'ST'
            st_count -= 1

mc = mc[mc['ID'].isin(mc_id)]
mc.shape[0]


df = pd.concat([mu,mc]) # data for main players of mu and mc
df.shape[0]
df.head(10)


## b. EDA
### Main players comparison
sns.boxplot(data = df, x='Position', y='Overall', hue='Club')
df = pd.concat([mu,mc]) # data for main players of mu and mc

df['Value'] = df['Value'].str.slice(1, )


df['Value'] = df['Value'].str.replace('M', '00000') # replace M into 5digits zeros first, then we will do sth for decimal
df['Value'] = df['Value'].str.replace('K', '00')
df['Value'] = pd.to_numeric(df['Value'])
df['Value'] = df['Value'].str.replace('.', -1)


import warnings
warning.filterwarnings(action= 'ignore') # ignore warning
df['Value'] =
df['Value'] = df['Value'].str.replace('M', '000000') # replace M into 6digits zeros
df['Value'] = df['Value'].str.replace('K', '000')

df['Value'].head(30) # check how it worked, now we remove euro sign
df['Value'] = df['Value'].str.slice(1, )
df['Value'] = df['Value'].str.replace('.', -1)

df['Value'] = pd.to_numeric(df['Value'])
df['Value'] = df['Value'].astype(int) # transform to int type
sns.boxplot(data = df, x='Position', y='Value', hue='Club')


# 4. What kind of players Manchester United should recruit? Recruit two players from other teams with consideration of Manchester United's Finances, Feasiblity, and Recruitment policy

## a. EDA - determine which player who are in the required position can be replaced. Selection Criteria is based on 'Name','Overall','Potential','Age', 'Joined', 'Point'

# point = (Overall*2 + Potential) / Age
mu['Point'] = (mu['Overall']*2 + mu['Potential'])/ mu['Age']
mu[mu['Position']=='MF'][['Name', 'Overall', 'Potential', 'Age', 'Joined', 'Point']] # Juan Mata got lowest 'Point' among 'MF'

mu[mu['Position']=='CB'][['Name', 'Overall', 'Potential', 'Age', 'Joined', 'Point']] # C.smalling got lowest 'Point' among 'CB'


mu[mu['Position']=='ST'][['Name', 'Overall', 'Potential', 'Age', 'Joined', 'Point']] # two players got similar points (so we keep these two 'ST' main players)


## So, now we tried to kick out(?) those players who got lowest score on each field and recruit other players to each 'MF' and 'CB'

## visualization
### we only consider players who are positioning 'MF' & 'CB'.
market = data[(data['Position']=='MF')|(data['Position']=='CB')]

import matplotlib.pyplot as plt

f, ax = plt.subplots(2,4, figsize=(20,10))
vs_list = ['Age', 'Overall', 'Potential', 'Weak Foot']

for i in range(8) :

    if i < 4 :
        colors = ['firebrick' if x > market[market['Position']=='CB'][:13][vs_list[i]].mean() else 'gray' for x in market[market['Position']=='CB'][:13][vs_list[i]]]

        sns.barplot(x= vs_list[i], y = 'Name', data = market[market['Position']=='CB'][:13], palette = colors, ax = ax[i//4, i%4])

        ax[i//4, i%4].axvline(market[market['Position']=='CB'][:13][vs_list[i]].mean(), ls = '--')

    else :
        sns.barplot(x = vs_list[i%4], y = 'Name', data = market[market['Position']=='RM'][:13], ax = ax[i//4, i%4])

        ax[i//4, i%4].axvline(market[market['Position']=='RM'][:13][vs_list[i%4]].mean(), ls= '--')

market[market['Position']=='CB']
