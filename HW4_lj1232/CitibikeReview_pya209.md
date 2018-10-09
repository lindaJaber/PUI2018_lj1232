# Citibike Review


## Question posed: Do people of different age groups use CitiBike the same?


## Analysis of Hypotheses: 

Linda has taken 2 age groups to compare, i.e. **Generation X** (born between 1965 and 1980), and **Millenials** (born between 1981 and 1996).

Her Null hypothesis states: 
>The proportion of Generation X using CitiBike is the same as that of Millenials in a given month.

Her Alternate hypothesis states:
>The proportion of Generation X using CitiBike is different from that of Millenials in a given month.

H0: G1/Gtotal = G2/Gtotal
H1: G1/Gtotal != G2total

The idea behind the hypotheses seem clear enough. However, only 2 age groups are chosen. I feel like more could have been included, to involve most of the population. 
Also, she has defined **Generation X** as people born between 1965-1980 and **Millenials** as people born between 1981-1996. These terms are fairly unofficial and they differ across various censuses/publications. However, it can be treated as an artibtrary value for this problem and since it is clearly defined, it should be alright.

## Analysis of Data:

Linda has taken CitiBike data for March 2018.

The first plot showing Distribution of the number of people that used Citibike in March 2018 by year of birth does a good job of visually showing the data. As Linda has mentioned, it is immediately evident the distribution skews towards later birth years, pointing out to the fact that younger peoples have higher counts as compared to older people.

I believe there is an error made ahead. Linda has mentioned initially G1 to be **Generation X** (born between 1965-1980) and G2 to be **Millenials** (born between 1981-1996). However the variables G1 and G2 created for plotting the data have used the years between 1928-1954 and 1946-1964.

## Test Suggested:

The data to be tested are two unpaired groups, i.e. the values in G1 do not relate to the values in G2. 
Since the values are counts, they are numerical data. Not being aware of whether the data follows the parameters of a Gaussian curve, and having not greater than 2 parameters, I suggest using the **Mann-Whitney U Test**.

