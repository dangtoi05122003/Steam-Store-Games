# Steam-Store-Games

>*As a gamer and data enthusiast, I have always been fascinated by how the Steam marketplace evolves. This curiosity inspired me to explore the data behind the platform and gain deeper insights into market trends, player preferences.*

## Overview

This project is designed to collect, store, process, and visualize data from the Steam Store for game market analysis. The goal is to derive meaningful insights into market trends and game performance.

## Architecture

![Architecture](images/Architecture.png)

## Data Visualization

### 1. Market Overview

This dashboard provides a high-level summary of the Steam marketplace by monitoring three core metrics: Total Games, Average Price, and Positive Rating Ratio. It visualizes the Age Requirement Distribution of the catalog alongside the volume of Games Released by Year, allowing users to immediately understand the market's composition and release trends.

![Architecture](images/Market_Overview.png)

### 2. Product Performance

This dashboard breaks down game performance across categories and platforms. It features a treemap showcasing Genre Market Share and a pie chart analyzing Operating System Support. Additionally, a stacked bar chart compares Positive vs Negative Ratings by Genre, making it easy to contrast user sentiment against specific game types.

![Architecture](images/Product_Performance.png)

### 3. Commercial Insights

This dashboard examines the intersection of pricing strategy, player engagement, and market value. It uses a scatter plot to analyze the Price vs Rating Tipping Point, mapping out how price levels correlate with positive user feedback. Additionally, two horizontal bar charts rank the market's outliers by displaying the Average Playtime by Game alongside the Most Expensive Games, offering a clear view of commercial factors on Steam.

![Architecture](images/Commercial_Insights.png)

## Data Source

The dataset used in this project is publicly available on Kaggle under the title [Steam Store Games](https://www.kaggle.com/datasets/nikdavis/steam-store-games). It contains information on over 27,000 Steam games from 1997 to 2019, including metadata, pricing, genres, system requirements, ratings, and playtime statistics.

## Project Structure

```
steam-store-games/
├── analytics_core/
│   ├── dbt_project.yml
│   └── models/
├── config/
├── data/
├── dags/
│   ├── configs/
│   └── root/
├── plugins/
│   ├── generators/
│   └── models/
└── src/
    ├── catalog/
    ├── config/
    ├── ingestion/
    ├── transform/
    └── utils/
```