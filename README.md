# <ins> Mood-Based Movie Recommender System </ins>



## ABOUT CHILIO
Chilio Streaming isn't just another streaming service—it's where bold content meets chill vibes. We're here to spice up your screen time with a hot mix of must-watch originals, cult classics, offbeat gems, and everything in between. If it's wild, weird, or just plain addictive, it's probably on Chilio.
Built for the binge generation, Chilio delivers a slick, no-BS viewing experience across devices, with smart discovery, zero fluff, and full-on personality. Whether you're here for late-night laughs, thrill-packed marathons, or something totally out of left field, we've got your flavor.
We're not trying to be the biggest. Just the boldest. So grab your popcorn (or hot sauce) and let's break the algorithm.

***Stream bold. Chill with Chilio.***

## PROBLEM STATEMENT
Chilio's queer content is significantly underperforming due to critical content discovery and mood-matching failures. Users frequently select titles expecting one emotional experience (e.g., light and humorous) but encounter content with dramatically different emotional tones (e.g., intense and emotionally draining). This fundamental mismatch creates poor viewing experiences, drives user frustration, reduces engagement metrics, and ultimately suppresses viewership for queer content across the platform.

**Current Pain Points:**
- High abandonment rates on queer content within first 15 minutes
- Negative user feedback citing "misleading content descriptions"
- Decreased completion rates compared to mainstream content categories
- Users avoiding queer content due to unpredictable emotional experiences

## OBJECTIVE
To address this critical gap, Chilio is implementing a machine learning-driven mood-based recommendation system specifically designed to personalize queer content discovery. The system will align viewer emotional states with content that matches their desired mood, particularly during high-engagement periods like Pride Month.

**Expected Outcomes:** This intelligent recommendation tool will empower users to discover queer media that genuinely resonates with their current emotional needs, creating more satisfying, inclusive viewing experiences while boosting content completion rates and platform engagement.

## BUSINESS OBJECTIVES

1.	**Mood-Content Alignment:** How can we intelligently match users with queer content that authentically fits their current emotional state and viewing intentions?
2.	**Personalized Emotional Engagement:** How can we leverage mood-based personalization to create deeper emotional connections between users and queer content, ultimately driving higher satisfaction and loyalty?
3.	**Complementary Recommendation Intelligence:** How can we integrate mood as a primary recommendation factor alongside traditional filtering mechanisms (genre, rating, duration) to create a more sophisticated and user-centric discovery experience?

## Overview 
This machine learning project develops a mood-based recommendation system for streaming platforms by analyzing movie content and categorizing films into emotional profiles that match user preferences.

## Methodolgy

**Data Sources**

The project utilized two primary datasets:
- LGBTQ Movies Dataset: Contains over 7,000 movies with Genre IDs but lacking explicit genre names
- Movie Genres Dataset: Provides the mapping between Genre IDs and descriptive genre names

**Data Preprocessing** 

The datasets were merged using Genre IDs to enrich the LGBTQ movies with clear genre classifications. During data exploration, null values were identified and handled appropriately, with irrelevant columns removed to streamline the dataset. Genre IDs were parsed and separated to ensure accurate movie-genre matching, then consolidated to eliminate duplicates.

**Feature Engineering & Selection:** 
A key innovation was developing a mood classification system from movie overviews. The text data was processed to extract emotion-relevant keywords using a custom lexicon approach. These emotions were consolidated into four primary mood categories:

- **Calm:** Peaceful, relaxing content
- **Dark:** Serious, somber themes
- **Intense:** High-energy, dramatic content
- **Uplifting:** Positive, inspiring material

Both categorical and numerical features underwent appropriate preprocessing; categorical variables were one-hot encoded while numerical features were normalized. To address potential class imbalance across mood categories, SelectKBest feature selection was implemented to identify the most informative features for classification.

**Model Development**

The dataset was split into training and testing sets for model validation. Initially, a Decision Tree classifier was implemented, but due to the complex relationships between features and target mood categories, the model was upgraded to Random Forest. This ensemble method was selected because it combines multiple decision trees to produce more accurate and stable predictions while reducing overfitting.

**Model Optimization** 
GridSearchCV was employed for systematic hyperparameter tuning, focusing on three key Random Forest parameters:
- **max_depth:** Controls tree complexity to prevent overfitting
- **min_samples_split:** Minimum samples required to split internal nodes
- **min_samples_leaf:** Minimum samples required at leaf nodes

**Model Performance & Evaluation** 
The model was evaluated using multiple metrics to provide a comprehensive performance assessment:
- **Accuracy:** Overall correct predictions
- **Precision:** Proportion of correctly predicted positive cases
- **Recall:** Proportion of actual positive cases correctly identified
- **F1-Score:** Harmonic mean of precision and recall

The initial Random Forest model achieved 55% accuracy across all metrics. Through GridSearchCV optimization of the hyperparameters, the model's performance improved significantly to 72% accuracy, with corresponding improvements in precision, recall, and F1-scores, representing a substantial 16 percentage point increase.













 
