# Computational Narratives
Imagine a story that unfolds not just through words, but through a seamless blend of text, data, and even code. 
That's the essence of computational narratives, a captivating way to communicate complex ideas using the power of data and computation.
Computational narratives combine text, data, and code to tell interactive stories about various topics. 
These narratives often allow readers to engage with the material in a dynamic way, exploring data and running code to better understand the subject matter.

Some consider computational narratives to be the "papers of the future," as they offer a more interactive and engaging approach to presenting research and information. 
They improve transparency and reproducibility by design, which is particularly important in the context of Open Science, 
where making research methods and results accessible and verifiable is crucial.

Jupyter Notebooks are perhaps the most popular format for creating computational narratives. 
They provide an ideal platform for integrating code, data analysis, and explanatory text, 
making them a go-to choice for researchers and data scientists aiming to share their work in an interactive, transparent, and reproducible way.

## Best Practices
As with many complex things, developing compelling computational narratives takes time and practice. 
Some general rules of thumb are summarized in the following do's and dont's:

Do:

- Tell a story for an audience
- Document the process, not just the results
- Craft a compelling narrative
- Use visualizations effectively
- Keep it simple and focused

Don't:

- Present code without context
- Delay documentation
- Overcomplicate visualizations
- Assume (too much) audience knowledge

## Building a Computational Narrative: The AQI Example

The best way to understand what makes a good computational narrative is to build one.
In this section we walk through the AQI project notebook
(`notebooks/computational_narrative.ipynb`) step by step,
connecting each decision to the best practices listed above.
The notebook analyses hourly air quality measurements from the
[German Federal Environment Agency (UBA)](https://www.umweltbundesamt.de/en)
and computes the official German Air Quality Index (Luftqualitätsindex, LQI)
for a Berlin monitoring station.

### Separating Logic from Narrative

A common mistake in computational narratives is to put all code — including complex,
reusable logic — directly in the notebook.
This makes the notebook hard to test and hard to read.

In the AQI project, the classification thresholds and the maximum-operator rule
are implemented in `src/aqi_calculator.py`, which has its own unit tests
(see Chapter [Testing](https://se-up.github.io/RSE-UP/chapters/testing_programs.html)).
The notebook simply imports that module:

```python
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from src.aqi_calculator import compute_row_aqi, AQI_LEVELS, AQI_SCORE
```

The sys.path adjustment tells Python where to find src/ relative to the
notebooks/ directory.
After this single import, the notebook never implements classification logic itself,
it only calls compute_row_aqi and uses the results.
This keeps the notebook focused on the narrative ("what does the data show?")
rather than on algorithmic details ("how is the index computed?").

### Loading the Data
The UBA exports data as CSV files with two non-standard properties:
a semicolon (;) delimiter instead of a comma, and datetime strings wrapped in
single quotes (e.g. '2025-08-01 01:00').
A brief markdown cell before the loading code tells the reader what to expect:


```python
file_path = '../data/raw/Grunewald_august.csv'
df_raw = pd.read_csv(file_path, sep=';')
print("Raw Data Shape:", df_raw.shape)
df_raw.head()
```

Calling df_raw.head() as the last expression in the cell lets Jupyter render
the first five rows as a formatted table without any extra print statements.
Showing the raw data immediately after loading is an example of
"Document the process, not just the results":
the reader can see exactly what arrived from the data portal before any
transformations are applied.

### Preprocessing the Data
Raw data from external sources rarely arrives in a form that is immediately useful.
The preprocessing section renames the verbose UBA column headers to short,
code-friendly names, parses the quoted datetime strings, converts pollutant
columns to numeric values, and drops rows that are missing both a station code
and a timestamp:


```python
df = df_raw.rename(columns={
    "Particulate matter (PM₁₀) One hour average in µg/m³": "pm10",
    "Ozone (O₃) One hour average in µg/m³":                "o3",
    "Nitrogen dioxide (NO₂) One hour average in µg/m³":    "no2",
    "Particulate matter (PM₂,₅) One hour average in µg/m³":"pm25",
    "Sulphur dioxide (SO₂) One hour average in µg/m³":     "so2",
})

df["datetime"] = (
    df["datetime_raw"]
    .str.strip("'\"")
    .pipe(pd.to_datetime, format="%Y-%m-%d %H:%M", errors="coerce")
)
```
Each step is preceded by a short markdown cell explaining *why* that step is
necessary, not just what it does.
For example, the cell before the timestamp parsing explains that the UBA portal
wraps datetime strings in single quotes, which prevents pandas from parsing them
directly as datetimes.
This kind of explanation is exactly what separates a computational narrative from
a script: a reader who has never seen UBA data before can follow the reasoning
without needing to inspect the raw file themselves.

The preprocessing section also handles missing pollutant values.
According to the UBA methodology, the index can be calculated as long as at
least one of the five pollutants is available.
Rather than dropping rows with any missing value, the notebook adds a helper column:

```python
pollutant_cols = ["pm10", "pm25", "o3", "no2", "so2"]
df["num_pollutants_available"] = df[pollutant_cols].notna().sum(axis=1)
df["has_any_pollutant"] = df["num_pollutants_available"] >= 1
```

Documenting this decision makes the notebook self-contained: a reader does not
need to look up the UBA methodology to understand why rows with partial data are kept.

### Applying the Calculation

With clean data available, calling the AQI module is a single line:

```python
df["aqi_computed"] = df.apply(compute_row_aqi, axis=1)
```

Before running the calculation on the full dataset, the notebook first demonstrates
it on a single row:

```python
example_row = df.iloc[0]
print(example_row[["pm10", "pm25", "o3", "no2", "so2"]])
print("Computed AQI:", compute_row_aqi(example_row))
print("Official AQI:", example_row["aqi_official"])
```

This single-row example cell serves two purposes.
First, it shows the reader concretely what input and output look like for one
measurement, making the subsequent bulk computation easier to trust.
Second, it provides an immediate sanity check: if the computed value for this
one row matches the official value, the import and the function call are working
correctly.
The full validation across all rows follows naturally from this single-row check.

### Visualizing the Results

The notebook uses three complementary visualizations, each answering a different
question about the data.

**Hourly time series** — one subplot per pollutant, sharing a time axis.
This answers "how did individual pollutant concentrations change over the month?"
and makes it easy to spot peaks and co-occurring pollution events.

**Bar chart of AQI category frequencies** — counts of how many hours fell into
each category (very good, good, moderate, poor, very poor).
This answers "what was the overall air quality picture for August?"
and illustrates the effect of the maximum-operator rule: even if most pollutants
are in the "very good" range, a single elevated reading pushes the overall
category higher.

**Heatmap of AQI score by hour-of-day and date** — a grid where colour encodes
the AQI score (1 = very good, 5 = very poor).
This answers "are there systematic time-of-day patterns?"
Rush-hour NO₂ peaks, for example, would show up as darker rows at 07:00–09:00
and 17:00–19:00 on weekdays.

Each visualization is introduced by a markdown cell that explains what the reader
should look for, not just how the plot was made.
Following the "Use visualizations effectively" guideline means choosing plot types
that match the question, and explaining the connection between the visual and
the conclusion in the surrounding text.

### What Makes This a Good Computational Narrative

Looking back at the best practices listed earlier, the AQI notebook follows them
in concrete ways:

- **Tell a story for an audience** — the notebook is addressed to a reader who
  understands air quality monitoring but may not know the UBA methodology.
  It explains each concept (the maximum-operator rule, the five pollutant categories)
  before using it in code.
- **Document the process, not just the results** — every data quirk (semicolon
  delimiter, quoted timestamps, missing SO₂ at some stations) is explained in
  the markdown cells where it is first encountered.
- **Keep it simple and focused** — complex logic lives in `src/aqi_calculator.py`.
  The notebook itself never implements a classification threshold.
- **Use visualizations effectively** — three different chart types answer three
  different questions; each is preceded by a cell explaining what to look for.
- **Don't present code without context** — every code cell is preceded or followed
  by a markdown cell that explains the purpose of that step.







## Further Examples
Here are some links to quite nice examples available at [nbviewer.org](https://nbviewer.org/):

- [An exploratory statistical analysis of the 2014 World Cup Final](https://nbviewer.org/github/rjtavares/football-crunching/blob/master/notebooks/an%20exploratory%20data%20analysis%20of%20the%20world%20cup%20final.ipynb)
- [An open RNA-Seq data analysis pipeline tutorial with an example of reprocessing data from a recent Zika virus study](https://nbviewer.org/github/maayanlab/Zika-RNAseq-Pipeline/blob/master/Zika.ipynb)
- [An open science approach to a recent false-positive between solar activity and the Indian monsoon](https://nbviewer.org/github/benlaken/Comment_BadruddinAslam2014/blob/master/Monsoon_analysis.ipynb)
- [Analysis and visualization of a public OKCupid profile dataset using python and pandas](https://nbviewer.org/github/lalelale/profiles_analysis/blob/master/profiles.ipynb)
- [Particle-In-Cell Plasma Sim](https://nbviewer.org/github/numerical-mooc/assignment-bank/blob/master/Lessons.and.Assignments/Particle.In.Cell.Simulations/PIC_Bonus_Notebook.ipynb)
- [Visualization: Mapping Global Earthquake Activity](https://nbviewer.org/github/ehmatthes/intro_programming/blob/master/notebooks/visualization_earthquakes.ipynb)



For a deeper dive into computational narratives and storytelling with data, there is specific literature available, 
for example [H. Eckert's book "Storytelling with Data"](https://link.springer.com/book/10.1007/978-3-658-38555-2).

### Summary:
This chapter walks through the AQI computational narrative notebook step by step. It covers five topics: separating reusable logic into src/aqi_calculator.py, loading UBA CSV data with its non-standard format, preprocessing and handling missing pollutant values, applying the calculation with a single-row sanity check before the full run, and choosing three visualizations that each answer a different question. Each step is shown with a code snippet and connected back to the Best Practices listed earlier in the chapter. 