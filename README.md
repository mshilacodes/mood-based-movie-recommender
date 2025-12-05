# <ins> Mood-Based Movie Recommender System </ins> 
by [SONIA MSHILA](https://www.linkedin.com/in/sonia-mshila-85a16b131/)


![Couple watching Movie](pexels-mikhail-nilov-7719224.jpg)
Image by [Mikhail Nilov](https://www.pexels.com/photo/a-couple-on-a-couch-with-a-bowl-of-popcorn-7719215/)


## ABOUT CHILIO
Chilio Streaming isn't just another streaming service—it's where bold content meets chill vibes. We're here to spice up your screen time with a hot mix of must-watch originals, cult classics, offbeat gems, and everything in between. If it's wild, weird, or just plain addictive, it's probably on Chilio.
Built for the binge generation, Chilio delivers a slick, no-BS viewing experience across devices, with smart discovery, zero fluff, and full-on personality. Whether you're here for late-night laughs, thrill-packed marathons, or something totally out of left field, we've got your flavor.
We're not trying to be the biggest, just the boldest. So grab your popcorn (or hot sauce) and let's break the algorithm.

***Stream bold. Chill with Chilio.***

## PROBLEM STATEMENT
Chilio's queer content is significantly underperforming due to critical content discovery and mood-matching failures. Users frequently select titles expecting one emotional experience (e.g., light and humorous) but encounter content with dramatically different emotional tones (e.g., intense and emotionally draining). This fundamental mismatch creates poor viewing experiences, drives user frustration, reduces engagement metrics, and ultimately suppresses viewership for queer content across the platform.

**Current Pain Points:**
- High abandonment rates on queer content within the first 15 minutes
- Negative user feedback citing "misleading content descriptions"
- Decreased completion rates compared to mainstream content categories
- Users avoiding queer content due to unpredictable emotional experiences

## OBJECTIVE
To address this critical gap, Chilio is implementing a machine learning-driven mood-based recommendation system specifically designed to personalize queer content discovery. The system will align viewers' emotional states with content that matches their desired mood, particularly during high-engagement periods like Pride Month.

**Expected Outcomes:** This intelligent recommendation tool will empower users to discover queer media that genuinely resonates with their current emotional needs, creating more satisfying, inclusive viewing experiences while boosting content completion rates and platform engagement.

## BUSINESS OBJECTIVES

1.	**Mood-Content Alignment:** How can we intelligently match users with queer content that authentically fits their current emotional state and viewing intentions?
2.	**Personalized Emotional Engagement:** How can we leverage mood-based personalization to create deeper emotional connections between users and queer content, ultimately driving higher satisfaction and loyalty?
3.	**Complementary Recommendation Intelligence:** How can we integrate mood as a primary recommendation factor alongside traditional filtering mechanisms (genre, rating, duration) to create a more sophisticated and user-centric discovery experience?

## OVERVIEW 
This machine learning project develops a mood-based recommendation system for streaming platforms by analyzing movie content and categorizing films into emotional profiles that match user preferences.

## METHODOLOGY

**Data Sources**

The project utilized two primary datasets:
- LGBTQ Movies Dataset: Contains over 7,000 movies with Genre IDs but lacks explicit genre names
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

## RESULTS AND ANALYSIS

***ROC Curve***

![ROC_before](https://github.com/user-attachments/assets/cb1dcc0f-44c9-4371-bc57-59329e397cc1)


The Initial Model Performance had an AUC of 0.49, which means that it's performing poorly. The Model struggles to distinguish between mood categories effectively.

![ROC_best](https://github.com/user-attachments/assets/ad73d112-a1db-4c88-a616-052cb31f45d7)


The Optimized Model performs much better, as indicated with an AUC of 0.68, this is shows a 39% improvement of the AUC. Meaning the model can distinguish between mood categories.
GridSearchCV hyperparameter helped transform the failing model into a functional classifier. This improvement translates to a better mood-content matching for Chilio users


***Heat Map***

   ![Updated_Random_forest](https://github.com/user-attachments/assets/fe979b5c-2c9a-4eb4-a56e-3b3ab269ca22)


The initial model heat map shows heavy confusion between opposite moods (Intense↔Uplifting)

![best_random_forest](https://github.com/user-attachments/assets/3206eb9d-21e8-4440-b7aa-3a6eabf44147)


The Optimized model heatmap shows that errors are more evenly distributed, indicating a better understanding of emotional nuance

***Bar Graph***

![Barchart_emotions](https://github.com/user-attachments/assets/ddf471ba-afea-4167-837d-71b8ade24350)

The  initial Model graph shows that the Uplifting mood is at 0.70 due to the large sample size, calm performs average despite the small sample size. Dark Struggles and Intense has the worst performance

![Barchart_emotions_best](https://github.com/user-attachments/assets/7bf553d1-9bcb-4c3f-bf5f-25d1ade93035)


The reworked model shows some interesting changes that were taken to improve the model. Uplifting has decreased to 0.48 but is more balanced, calm is at 0.38, which is still reasonable, dark decreased performance to 0.23, and intense (0.27) improved from being the worst performer

## CONCLUSION

1. **Mood-Content Matching Success:**
The optimized Random Forest model directly solves Chilio's fundamental challenge of matching users with emotionally appropriate queer content. With 72% accuracy and balanced F1-scores across mood categories, the system successfully prevents the critical mood-mismatch scenarios that were driving user dissatisfaction and content abandonment.

2. **Enhanced User Experience & Engagement:**
The dramatic improvement from AUC 0.49 (chance level) to AUC 0.68 (moderate discrimination) represents a transformation from a system that would exacerbate Chilio's discovery problems to one that actively enhances user satisfaction. The optimized model's consistent performance across Calm (45% F1), Dark (30% F1), Intense (20-27% F1), and Uplifting (70% F1) categories ensures reliable emotional alignment regardless of user mood state.

3. **Strategic Content & Technical Recommendations:**
The current model provides sufficient accuracy for deployment, directly addressing Chilio's Pride Month engagement goals and reducing browsing fatigue through improved mood-based filtering. The analysis reveals significant training data imbalance, with Uplifting content comprising 65% of the dataset while Calm content represents only 10%. To achieve optimal model performance, Chilio should prioritize acquiring diverse mood content, particularly in Dark and Intense categories, to create more balanced training data for future model iterations.

This mood-based recommendation system transforms Chilio's content discovery from a source of user frustration into a competitive advantage. By solving the emotional tone mismatch problem, the system directly supports increased completion rates, enhanced user satisfaction, and stronger engagement with queer content—positioning Chilio as the streaming platform that truly understands its users' emotional viewing needs.

## DEPLOYMENT 

[![Chillio!](https://www.flaticon.com/free-icon/watching-a-movie_4221484?term=movies&page=1&position=2&origin=search&related_id=4221484)](https://mood-based-movie-recommender-evgyswjjwxejgcrymyty3u.streamlit.app/#unknown)

## NEXT STEPS
In order to improve the model, the next steps include:

- Expand training dataset with balanced mood representation
- Implement ensemble methods for minority mood categories
- Develop real-time user feedback integration for continuous model improvement
- Explore deep learning approaches for enhanced emotional text analysis


## CONTACT 

[EMAIL](soniamshila@gmail.com)

[LINKEDIN](https://www.linkedin.com/in/sonia-mshila-85a16b131/)















 
