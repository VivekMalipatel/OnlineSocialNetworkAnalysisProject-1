CS 579: Online Social Network Analysis 
------------------------------------------------------------------------------------------------------------
Project I - Social Media Data Analysis 
------------------------------------------------------------------------------------------------------------
Group 45 
------------------------------------------------------------------------------------------------------------
Vivekanand Reddy Malipatel (A20524871) 
Mohammed Shoaib (A20512491)
------------------------------------------------------------------------------------------------------------
Steps to Run the program :

1. Run scrapper.py to fetch the data from Reddit and Store it to csv files.
2. Next, Run Visualise.py to generate the social network graph form the edges.csv.
3. Next, Run analyse.py to generate the network metrics.
------------------------------------------------------------------------------------------------------------
Libraries Required :

Pandas, Networkx, Praw, matplot.lib


# CS 579: Online Social Network Analysis

## Project I - Social Media Data Analysis

**Instructor:** Prof. Kai Shu  

### Overview
This project is a 2-member group assignment aimed at crawling social media data and performing an analysis on the collected data. The project is divided into three main steps: Data Collection, Data Visualization, and Network Measures Calculation.

### Project Objectives
- Crawl social media data.
- Process and analyze the extracted data.
- Report findings and methodology.

### Project Outline

1. **Data Collection:** Select a social media platform and crawl data to create a social network with 100-500 nodes.
2. **Data Visualization:** Use graph analysis software to visualize the network.
3. **Network Measures Calculation:** Calculate and plot various network measures.

### Guideline

#### Step 1: Data Crawling
Choose a social media platform and figure out how to crawl data from it. You may need API credentials for this purpose. Document your process in the report.

#### Step 2: Data Visualization
Visualize the fetched data as a graph using packages like NetworkX, SNAP, Gephi, NodeXL, or graph-tool. Include snapshots in your report.

#### Step 3: Network Measures
Calculate network measures like Degree Distribution, Clustering Coefficient, PageRank, Diameter, Closeness, and Betweenness. Choose appropriate measures to plot and analyze, and include these in your report.

### Submission Instructions

Submit the following in a `.zip` folder named `LASTNAME1_LASTNAME2_PJ1`:

- Data files
- Source code
- PDF report

Upload the `.zip` folder to Blackboard.

### Grading Rubric

| Points | Description                           |
|--------|---------------------------------------|
| 1      | Select platform in the first week     |
| 3      | Data Collection                       |
| 3      | Data Visualization                    |
| 3      | Network Measures Calculation          |
| **10** | **Total**                             |

### Academic Integrity

You must develop your own code for data scraping and cannot use public datasets. Referencing others' code is allowed but direct copying is not. Cite all used resources.

### Obtaining API Keys

#### Twitter:
Follow the instructions provided at https://developer.twitter.com to apply for a developer account and obtain your API keys.

#### Facebook:
Visit https://developers.facebook.com, set up a developer account, and obtain the necessary credentials to use the Facebook API.

### References

- NetworkX: [Link](#)
- SNAP: [Link](#)
- Gephi: [Link](#)
- NodeXL: [Link](#)
- Graph-tool: [Link](#)

> **Note:** Replace `[Link]` with actual URLs to the resources.

