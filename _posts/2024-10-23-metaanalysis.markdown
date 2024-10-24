---
layout: post
title: Sample Meta-Analysis
subtitle: The data is sparse out there!
thumbnail-img: /assets/img/housingthumb.png
cover-img: /assets/img/housingthumb.png
---

I wanted to learn about evictions in America, because I read Matthew Desmond's book *Evicted* and I wanted to see the data beyond the really moving stories. It was the very first ethnographic book that I read. I found Matthew Desmond's [Eviction Lab](https://evictionlab.org/) and I dug through all the [Google Scholar](https://scholar.google.com/scholar?cites=10745652819672726604&as_sdt=5,33&sciodt=0,33&hl=en) articles that cited the Eviction Lab's data to see what people were doing with it / how it was collected.

## Article 1 Confidential Data

This observational study, called [A comprehensive demographic profile of the US evicted population](https://www.pnas.org/doi/epub/10.1073/pnas.2305860120) explores the relationship between child ownership and eviction rates, as well as racial disparities in eviction threats.

The study's null hypotheses, were there are **no** correlations between race, sex, ethnicity, nativity (what country you are from), age, or any information that you fill out to the American Census Bureau, with how many evictions you've had. 

There are two salient "alternative" hypotheses the researchers found: One that there is a correlation between owning a child and being evicted. Additionally, they also identified stark racial disparities in eviction threats, with Black renters approximately three times more likely to face the threat of eviction compared to other racial groups.

### Do I Trust This Study?

I give them a score from 1-5 of trustworthiness for each section.
1. **Journal Reputation**: Published in PNAS, a highly respected scientific journal, and it's open access. **5**
2. **Institutional Affiliations**: Nick Graetz, the lead author, was a Postdoctoral researcher at Princeton University at the time of writing, now affiliated with the University of Minnesota. The others were from Princeton University (Matthew himself! And I read his 400 page book, I do feel like I know him.), Rutgers University-Newark, and the United States Census Bureau. In the **Author Contributions** section in <small style="color: red">itty bitty</small> text (see picture below), other contributors associated with the US Census Bureau "S.R.P. and D.H.S. oversaw project administration and administrative data linkage." **3**, see conflict of interest below...
     ![Information is presented smaller and smaller and smaller...](https://ifenghm.github.io/beautiful-jekyll/assets/img/articledataunavailability.png)*The more important information for meta-analysis is presented smaller and smaller!*

3. **Limitations**: The authors acknowledged potential limitations in their research, specifically noting "underreporting and incomplete eviction data" in their materials and methods section. **4**
4. **Conflict of Interest?**: The authors declared no competing interests, **but** in their acknowledgements, they said this, "Any opinions and conclusions expressed herein are those of the authors and do not represent the views of the US Census Bureau." It's interesting that they decided to say this; maybe it's some government thing. Is the US Census Bureau supposed to have "views"? Honestly, there's so much data here, I want my government to have some views about how to help their suffering citizens at large, like me, uwu... (jk I'm not at threat for eviction) **3**
5. **Funding**: In the Acknowledgements section, it says that "The Eviction Lab is supported by the JPB and Bill & Melinda Gates Foundations, the Chan Zuckerberg Initiative, the Eunice Kennedy Shriver National Institute of Child Health and Human Development of the NIH under Award No. P2CHD047879, and the National Institute of Nursing Research under R01NR020748."
I see how these nonprofits, like the Child Health one, could be argued as iffy... but honestly these are all nonprofits funded by people who should be giving their money away to research, so I'm all for it :) **4**


Overall trustworthiness score-wise, I'm pretty okay with this (**3.8 / 5**), but I am unhappy with the state of the data availability of this study... 

### Can I replicate this study?

No. Actually, they let on at the very end of the article that one half of the data is confidential. So even though the Eviction Lab has their data publically downloadable, the US Census Bureau data to do racial and parental demographics and to link the eviction data is confidential per person, which, I get it, but I'm really angry about this: 

>We are not able to make these data directly available. However, we can provide the code and researchers can follow the directions on how to write a proposal to gain access to the data via a Federal Statistical Research Data Center using the Standard Application Process. The code to conduct our analyses is available here: https://github.com/ngraetz/pnas_demographics_of_eviction.

When I go to the [github](https://github.com/ngraetz/pnas_demographics_of_eviction), there's literally nothing but a README. And they let this guy publish this? Sigh.

## Article 2: What's the price of data?

This is a study that somehow found a causal link between [eviction and poverty in American cities](https://academic.oup.com/qje/article/139/1/57/7276608). More specifically, the authors found an eviction order **increases** homelessness and hospital visits and reduces earnings, durable goods consumption, and access to credit in the first two years. I thought you can't prove causality without an experiment, and wouldn't a real-world experiment of evicting random people be umm... *unethical*? They mention a design **instrumental variables (IV)**, and I [wikipedia'd](https://en.wikipedia.org/wiki/Instrumental_variables_estimation) it "is used to estimate causal relationships when controlled experiments are not feasible or when a treatment is not successfully delivered to every unit in a randomized experiment." Oh okay, I'm going to stop there before I go to a rabbit hole, but I'm even more interested intrigued to see if I can what data the authors have collected and if I can trust them... 

### Do I Trust This Study?

1. **Journal Reputation**: Published in the Quarterly Journal of Economics, a highly respected scientific journal. **5**
2. **Institutional Affiliations**: The Authors are from Department of Economics in Notre Dame, Yale, UChicago. One of the writers now works at [Spotify](https://scholar.google.com/citations?user=IXsGHYQAAAAJ&hl=en&oi=ao) as a Data scientist after getting a PhD in public policy; what can I say, academia isn't glamorous. Also, it's interesting to see how long papers take to get published - there is a 2019 article talking about this research, and the research itself was published in 2023... **3**
3. **Limitations**: They did talk about IV design and how it could solve the problem of maybe an unobserved variable that could be underlying both eviction and poverty, and not anything the American Census Bureau could have collected. I also feel like this is kinda p-hacky, in that they create a "financial health index" but then they later say "access to credit in the first", which is so much more specific than "financial health", it feels like they are fishing for **something** to say.* **2**
4. **Conflict of Interest?**: The researchers didn't have an explicit section of this, but like the first paper, they used Census data and they also did the whole "Any opinions and conclusions expressed herein are those of the authors and do not represent the views of the US Census Bureau."  so I guess it's a legal formality to say this when you've gotten some extra help from the US Census Bureau. None of the authors seem to be directly working for the Bureau this time, but I think they needed to get approval for confidential information. **3.5**
5. **Funding**: In the Footnote section, the authors "gratefully acknowledge financial support from the NSF..., the Laura and John Arnold Foundation, the Spencer Foundation, the Kreisman Initiative on Housing Law and Policy, the Horowitz Foundation for Social Policy, the Becker Friedman Institute, and the Tobin Center for Economic Policy." **5** I haven't heard of ANY of these foundations, which actually makes me appreciate these foundations even more.

Trustability score: **3.7/5**, I kind of trust it, but I know nothing about IV design.

\* It does feel a bit "publish or perish"-y, although it includes around court sample includes around 414,000 eviction court orders for Cook County and 580,000 cases for New York conducted over 12 years (2004-2016). And they even say, relative to other studies, "we find more modest effects of eviction on employment and no effect on the poverty rate of neighborhoods to which evicted tenants move." So they are being honest about their non-groundbreaking results, which is nice. 

### Can I replicate this study?

... at a price. The [dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/Y9TZQI) is publically available on Harvard's servers, but oof! All of these files are .do files, which means they are Stata files, and I don't have Stata. And Stata is statistics for non-coders (I'm better than that). And it costs a lot of money, especially if I'm not part of a university. Even if I work for the government it's $900 / year?? For working on tooling that's provided by the government? I'm really confused. Oh well, I'll try one more...

![Stata costs](https://ifenghm.github.io/beautiful-jekyll/assets/img/stata.png)*Stata costs $160 / year if I'm in education, $90 if I'm a student, but this is all at the UNIVERSITY level.*

## Article 3: Finally, Data Access! But... 

Going back to google scholar, I found an older article of Matthew Desmond's that studied [Racial and Gender Disparities amongst evicted Americans](https://sociologicalscience.com/articles-v7-27-649/#tab-3). This observational study basically counted ratios across 4.1 million individuals in 39 states: how many x individuals who are male/female are evicted out of everyone in the county. The null hypothesis is that there is no difference between the ratio of evicted people and any other demographic variable.
The alternative hypothesis is that Black renters received a disproportionate share of eviction filings and experienced the highest rates of eviction filing and eviction judgment, and additionally, Black and Latinx **female** renters faced higher eviction rates than their male counterparts. 
Actually, [Article 1](#article-1-confidential-data) cited this study as being prone to errors as well as not being able to replicate the gender disparity results using the (hopefully, newer and improved). So let's dive into that...

### Do I Trust This Study?

1. **Journal Reputation**: Published in Sociological Science, I've never heard of this journal before, but I really liked their statement commitment to [reproducibility](https://sociologicalscience.com/reproducibility-policy/). Unfortunately, the policy only went into effect in 2023, and this is an older paper (published 2020, probably done in 2018), it doesn't have a reproducibility statement. But this paper in particular is awesome and makes all of its data AND code available! **5**

![reproducibility policy](https://ifenghm.github.io/beautiful-jekyll/assets/img/ReproducibilityPolicy.png)

2. **Institutional Affiliations**: The authors are from Rutgers and Princeton. But they all are part of the Eviction Lab. See conflicts of interest below. **4**
3. **Limitations**: Guessing gender and race from only names is really prone to error. The authors did mention this, but they said they used "geolocation" also. **2** I'm not sure if I like this.
4. **Conflict of Interest?**: It's interesting, this is a bit of a history lesson. I think the Eviction Lab was just getting started in 2018, when this data was being collected. They didn't mention that all three of the authors worked there, but it did list the funding below... **3.5** Maybe it's obvious, but I think it's important to mention that the Eviction Lab is a project of Princeton University, and it's not like they are a separate entity.
5. **Funding**: The Eviction Lab had roughly the same funding as in 2023, which means it is stable. Ones that no longer support: Ford Foundation and C3.ai Digital Transformation Institute. What does AI have to do with this? Maybe because of gender and race **imputation**? Not sure. **3**

Trustability score: **3.5/5**, 

### Can I replicate this study? 

Finally, yes I can! The data is publically available on the [Eviction Lab's website](www.evictionlab.org/demographics-of-eviction-data), and I can download it and see if I can replicate the results. The raw data is provided and all the scripts for gender / race imputation are listed. It actually *works* when I run the R script, even though I don't understand R too well. 

I needed an API key to get the Census data, and I went to the [census.gov](https://api.census.gov/data/key_signup.html) to get one. 
![Census API key]( https://ifenghm.github.io/beautiful-jekyll/assets/img/CensusAPIKeyRequest.png)

But when I click the Request a Key button, I got an error. 
![Census API key error](https://ifenghm.github.io/beautiful-jekyll/assets/img/CensusAPIKeyRequest.png)

Thankfully, the API key was left on the script. Here's a snippet (this is r code, which I don't know super well, but I know the arrows are left hand assignment, so acs and acs_hh are tables that are being saved).


```r
map_df(us_states, function(x) {
  get_acs(geography = "tract",
          variables = c(rhh.latin = "B25003I_003",
                        rhh.white = "B25003H_003",
                        rhh.black = "B25003B_003",
                        rhh.asian = "B25003D_003",
                        rhh.asian2 = "B25003E_003",
                        rhh.other = "B25003F_003",
                        rhh.other2 = "B25003G_003",
                        rhh.other3 = "B25003C_003"),
          year = 2016,
          state = x,
          key = "63153a9c483891cfc1fc7be953ff2c09982c9d1f")
}) -> acs

acs %>%
  group_by(GEOID, NAME) %>%
  mutate(race = case_when(str_detect(variable, "black") ~ "black",
                          str_detect(variable, "latin") ~ "hisp",
                          str_detect(variable, "white") ~ "white",
                          str_detect(variable, "asian") ~ "asian",
                          str_detect(variable, "other") ~ "other"
                          )) %>%
  group_by(GEOID, race) %>%
  summarize(estimate = sum(estimate),
            moe = sum_moes(moe)) %>%
  rename(GEOID.Tract = GEOID) %>%
  mutate(state = str_sub(GEOID.Tract, 1, 2),
         county = str_sub(GEOID.Tract, 3, 5),
         tract = str_sub(GEOID.Tract, 6, 11)) %>%
  select(GEOID.Tract, state:tract, race:moe) -> acs_hh


```

## Conclusion

It seems like **useful data** is kept confidential, and data that makes a lot of assumptions is what is available.