# Personal_Project

## FIFA Data Analysis 
**What kinds of Football players are needed for Manchester United**

#### Introduction 
Okay, my Football Knowledge is close to the ground. But, there are more and more new cases where the Football area performed well with Big Data. In 2016, there was a big change in the conservative Football world from one event. The introduction of VAR (Video reading system) was the one. After the introduction of VAR, 'miscarriage of justice' was reduced by 80%. With that opportunity, Big Data has been used in Football ever since 2016. There are THREE areas where Big Data is used in Football. First, Data and strategy analysis effect. Second, Injury prevention effect. Third, the effect of meeting Football fans ' needs through analyzing football matches. 

In this project, the first area of Big data used in Football, 'Data and Strategy analysis effect ', will be performed. The reason we want to analyze the data of Manchester United is that Manchester United outperformed in 2019/2020 Season. Ever since, Sir Alex Ferguson retired as manager of Manchester United in May 2013, Manchester United went down and ended the 2013/2014 season with a ranking that didn't match their reputation like a lie. There were several directors who were charged after the 2013/2014 season but Manchester United couldn't regain their status when directed by Alex Ferguson. As well, Manchester United went through several events. Ole Gunnar Solskjær who is used to be a player of Manchester United led by Alex Ferguson was hired as a new manager of Manchester United in 2020. As of March 2020, Ole Gunnar Solskjær succeeded in changing the atmosphere of Manchester United by signing contracts with only two players from the winter market of 2019/2020 season. 

Then who are the two players who changed the atmosphere of Manchester United successfully? What are the features of the two players? Was Manchester United a successful turnaround because of those two players? To investigate those listed questions, we will analyze Manchester United through 2018/2019 FIFA Data (from Kaggle) which is happened before Manchester United successfully turnaround the atmosphere. Then we will identify the type of international European football players needed for Manchester United and compare those players with the two players recruited by Ole Gunnar Solskjær from the winter market of 2019/2020.

The ranks of the Season club coefficients 2019/2020 can be found [here](https://www.uefa.com/memberassociations/uefarankings/club/seasons/)

Acording to [UEFA](https://www.uefa.com/memberassociations/uefarankings/club/about/), the coefficient can be read as follow: 
> The **club coefficients** are based on the results of clubs competing in the five previous seasons of the UEFA Champions League and UEFA Europa League. The rankings determine the seeding of each club in relevant UEFA competition draws.

> The **season club coefficients** are based on the results of clubs competing in the current UEFA Champions League and UEFA Europa League season. The rankings, combined with those of the previous four seasons, determine the seeding for each club in all UEFA competition draws.

> Coefficient calculation: **Clubs' coefficients** are determined EITHER the sum of all points won in the previous five years OR the association coefficient over the same period, WHICHEVER IS THE HIGHER (under a new system introduced for 2018/19 onwards).


##### < Description of the FIFA Data >

| Column Name|  Description |
|--------|-----------|
| ID | Identity Number |
| Name | Player's Name |
| Age | Player's Age |
| Overall | Player's current stats |
| Potential | Player's potential stats |
| Club | International Club(team) where player is in|
| Value | Player's Estimated Transfer Fee (EURO)|
| Wage | Player's Weakly Wage (EURO)|
| Preferred Foot | Player's Preffered Foot |
| Weak Foot | Player's Weak Foot |
| Skill Moves | Player's Skill Moves |
| Position | Player's Position |
| Jersey Number | Player's Jersey Number |
| Joined | Date Player joined the club(team) |
| Contract Valid Until | Player's contract Terms |
| Height | Player's Height (feet) |
| Weight | Player's Weight (Pound) |
| LS ~ RB | Player's stats by position |
| Crossing ~ GKReflexes | Player's detailed stats |
| Release Clause | Buyout Clause* |

*It is an amount stipulated in the player's contract that, if paid by another club, will automatically lead to the player being sold to that club.

#### Main Players 
The association football positions is  
* Goalkeeper
* Defender (Center-back, Sweeeper, Full-back, Wing-back)
* Midfielder (Center-midfiled, Defnesive midfield, Attacking midfield, Wide midfield)
* Forward (Center forward, Second striker, Winger) 

![Image of Soccer Position](https://images.saymedia-content.com/.image/c_limit%2Ccs_srgb%2Cq_auto:good%2Cw_432/MTc1NDU0MjY3MDg2NTQ2NTAw/positions-in-soccer-and-their-roles.webp)

--- 
In this project, we will select 
* GK:1 / CB:4 / MF:4 / ST: 2
* And the selection criteria of main players of two teams (MU and MC) is based on 'Overall' (Player's current stats)

**List of GK, CB, MF, ST**
There are 'GK', 'RCM', 'LCM', 'ST', 'RDM', 'LW', 'RW', 'CDM', 'CB', 'LCB',
       'RB', 'CM', 'RCB', 'RM', 'CAM', 'LB' positions in the data. 

* gk_list = 'GK'
* cb_list = 'CB', 'LCB', 'RCB', 'RB', 'LB'
* mf_list = 'RCM', 'LCM', 'CDM', 'CM', 'RM', 'CAM'
* st_list = 'ST', 'LW', 'RW'

---

This is Data Analysis Plan we established for this project. 

### 1. Analyze about players of Manchester United - What kind of players are in Manchester United
### 2. Compare players stat with Manchester City, the rival team of Manchester United
### 3. Choose(select) two insufficient positions
### 4. What kind of players Manchester United should recruit? Recruit two players from other teams with consideration of Manchester United's Finances, Feasiblity, and Recruitment policy



