Dynamic Customer-Centric Recommendation Engine

Project Description
This project moves beyond traditional Market Basket Analysis by developing an advanced recommendation system using the Instacart dataset. It leverages unsupervised machine learning (K-Means) to first segment customers into distinct personas based on their purchasing behavior. Subsequently, it generates highly relevant, personalized product recommendations for each specific segment using the FP-Growth algorithm. The entire system is deployed as an interactive web dashboard built with Streamlit, translating complex data patterns into actionable business insights.
Key Features
Customer Segmentation: Identifies distinct customer personas (e.g., "Core Organic Buyers," "Sparkling Water Enthusiasts") using K-Means clustering on engineered features like order frequency, basket size, and department affinity.

Personalized Recommendations: Generates unique association rules tailored to each persona's specific buying habits, revealing insights invisible in a general analysis.

Performance Optimization: Implemented memory-safe data processing techniques, including aggressive product filtering and order sampling, to handle a large dataset (>3 million orders) on a standard local machine.

Interactive Dashboard: A user-friendly web application built with Streamlit to visualize and explore the unique recommendations for each customer persona.

🛠️ Tech Stack
Language: Python

Libraries: Pandas, Scikit-learn, MLXtend, Streamlit, Plotly

Tools: Jupyter Notebook, Git, GitHub

💾 Data Source
The dataset used for this project is the "Instacart Market Basket Analysis" dataset from Kaggle. Due to its large size, it is not included in this repository. You can download it from the official Kaggle competition page:

Download the data here

🚀 How to Run This Project
Clone the repository to your local machine:

git clone [https://github.com/Rajat573/market-basket-recommendation-engine.git](https://github.com/Rajat573/market-basket-recommendation-engine.git)

Navigate to the project directory:

cd market-basket-recommendation-engine

Create a Python virtual environment and activate it.

Install the required dependencies from the requirements.txt file:

pip install -r requirements.txt

Place the downloaded Instacart CSV files into a data/ subfolder.

Run the Jupyter Notebook (Untitled.ipynb) to perform the analysis and generate the cluster_rules.pkl file.

Launch the Streamlit app:

streamlit run app.py

💡 Key Findings
The analysis successfully identified several customer personas with vastly different purchasing patterns. The most notable finding was the "Sparkling Water Enthusiasts" persona (Cluster 3), which showed extremely high confidence and lift (>15x) for rules involving different flavors of sparkling water. This powerful, specific insight proves the value of a segmented approach for creating effective, targeted marketing strategies that would be impossible with a generic model.
