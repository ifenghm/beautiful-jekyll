---
layout: post
title: Data Visualizations in the Wild
subtitle: 
---

## 1. Fun with Stacked Area Charts
I found many [stacked area charts](https://flowingdata.com/2021/06/08/seeing-how-much-we-ate-over-the-years/) about what kind of foods Americans have eaten over the years. I myself have been pescatarian for over 5 years, and tried, and horribly failed to be vegan, mostly because restaurants did not have good vegan or even vegetarian options. 

There are two charts in the article that show that if we grouped the dairy and fruit charts together, all american cheese would start below oranges in 1970, and rise to be below bananas as the second most consumed "fruit" in 2019. 
![Fruit Chart](https://flowingdata.com/wp-content/uploads/2021/06/fruits-fresh-1.png)
![Dairy Chart](https://flowingdata.com/wp-content/uploads/2021/06/dairy-eating-v2.png)

I thought it was really cool that the author was able to show popularity of foods moving to the top over time, as in, **using order as an important channel**, and I really wanted to be able to do this in Altair.
In the Altair gallery where they have a bunch of examples, I saw that there was a [streamgraph](https://altair-viz.github.io/gallery/streamgraph.html) example under the [area charts](https://altair-viz.github.io/gallery/index.html#area-charts) section. I think the only difference is that there's a `.stack('center')` method that makes the areas start stacking building out from the center, which is not what I want so I removed that from my chart.

I used vega's `us_employment` dataset to recreate a stacked chart because I knew what I needed was many categories plotted over time to get the same effect as the dietary charts. I already knew how to `melt()` this data into longform, so I did that, and then used `area` as a mark, and for channels: 
- time on the x-axis (classic)
- the `#` (in my case, employees) on the y-axis but also represented as order, which is neat! 
- color for the different categories (also classic)

```python
chart = alt.Chart(emp_lf).mark_area(stroke=None, interpolate="monotone", cursor="pointer").encode(
    x=alt.X("month:T"),
    y=alt.Y("employment:Q", title="employment (in 1000s)"),
    color="sector:N",
    order="sum(employment):Q", # the stacked areas move to the top!
    tooltip=["sector", "employment", "month:T"],
    # use the when method to change opacity when the selection is true
    opacity=alt.when(select).then(alt.value(1)).otherwise(alt.value(0.3)),
# need to use the add_params() method to add interactive components to chart
).add_params(select)
```

I also added some opacity because Altair can do interactive charts and it is pretty easy once I understood how to conditionally UI actions, e.g. `pointerover` is hover.

```python
select = alt.selection_point(on="pointerover")
```

This is the end result: 
<head>
  <!-- Import Vega & Vega-Lite (does not have to be from CDN) -->
  <script src="https://cdn.jsdelivr.net/npm/vega@5.31.0"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-lite@5.23.0"></script>
  <!-- Import vega-embed -->
  <script src="https://cdn.jsdelivr.net/npm/vega-embed@6.29.0"></script>
</head>

<div id="vis"></div>

<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/ifenghm/beautiful-jekyll/refs/heads/master/code/unit4/interactive_altair_us_employment.json";
  vegaEmbed('#vis', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

</script>


## 2. Packed Bubble Charts - Failure

For the next chart, the New York Times released a bunch of interactive charts with based on how the recent [ending of affirmative action](https://www.nytimes.com/interactive/2025/01/15/upshot/college-enrollment-race.html) has affected college enrollment. These bubble charts showing the change in color really cool because it is basically only a 1 way scatter plot, but the bubbles are packed tightly and created so they are not overlapping. 

![bubble college]({{ "/assets/img/unit4/bubblecollege.png" | absolute_url }})

It's really cool that this chart is able to graph not only 1) the change in enrollment of Black students (through both location and color), and the 2) size of the college through the size in each individual bubble, but also being able to make sure that the bubbles are not overlapping - I've always made charts that look like a mess because of all the overlaps. 

I Googled a couple things and I realized what I was looking for was a "Packed Bubble Chart" or a "Beeswarm plot." Altair's docs didn't have any example of this, but I had hope because [Vega](https://vega.github.io/vega/examples/beeswarm-plot/) had an example and I figured that I could load all vega charts into Altair since Altair is built on top of Vega. 

Unfortunately, I learned the hard way that not all Vega charts can be loaded into Altair (although the other way around IS true). When I tried to load the beeswarm json from vega using the `alt.Chart.from_json()` method, I got an error that said "ValidationError" on the json. There are no force transforms implemented in Altair yet, and so Altair can't parse this particular json. 

I did successfully implement a jitter plot which randomizes the x values of the colliding points a bit, but it doesn't spread the bubbles out wide enough.

```python
jittering = ""
with open("jittering.json") as f:
    jittering = f.read()

new_chart = alt.Chart.from_json(jittering).transform_calculate(jitter="random()")
new_chart.encoding.x = alt.Undefined  # remove x
new_chart.encoding.y = alt.Y("Miles_per_Gallon:Q")
new_chart.encoding.color = alt.Color(
    "Miles_per_Gallon:Q", scale=alt.Scale(scheme="redyellowgreen")
)
new_chart.encoding.xOffset = alt.XOffset("jitter:Q")  # random jitter
new_chart.encoding.tooltip = alt.Tooltip(["Name:N", "Miles_per_Gallon:Q"])
new_chart
```

![I tried...]({{ "/assets/img/unit4/attemptbubble.png" | absolute_url }})

So I ran into a big limitation of Altair, but that's alright (and maybe I'll learn more about vega proper if I have time)! I pivoted to implement a dropdown menu, which the New York Times also featured at the end of their article. I did run into an issue with a `MaxRows Error`, and learned that Altair can't process dataframes with more than 5000 rows. I had to filter out the data from the NYT articles (59 colleges reported to the federal government so the data is public domain and clean) to only include all freshman enrollment demographic data to 2015 and beyond.

The dropdown menu is a great way to filter out the data for people to do their own analysis. For example, we talk about average changes of the changes in Black/Hispanic enrollment in colleges, and it is subtle overall, but Johns Hopkins for example has a huge decrease in Black / Hispanic enrollment, and we should absolutely be looking into why that is.

```python
genre_dropdown = alt.binding_select(options=df["College"].unique(), name="College")
genre_select = alt.selection_point(
    fields=["College"], bind=genre_dropdown, value=df["College"].unique()[0]
)
alt.Chart(df).add_params(genre_select).transform_filter(genre_select).mark_line().encode(
    // channels ...
)

```

#### Select a College to see changes in racial enrollment over time

<div id="dropdown-vis"></div>

<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/ifenghm/beautiful-jekyll/refs/heads/master/code/unit4/line_education.json";
  vegaEmbed('#dropdown-vis', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
