# What is Machine Learning?

Machine Learning (ML) is a core component of Artificial Intelligence (AI) that enables computers to learn from data and make intelligent decisions without being explicitly programmed for every task.

It combines concepts from several disciplines, including:

- Probability Theory
- Statistics
- Approximation Theory
- Convex Analysis
- Algorithm Complexity Theory

## Machine Learning Process

![Machine Learning Overview](images/ml-overview.png)

Machine learning works by using data to train computational models. These trained models can then:

- Recognize patterns
- Solve problems
- Predict future outcomes

For example, a machine learning system trained on thousands of images of cats and dogs can eventually learn to distinguish between the two automatically.

---

## AlphaGo: A Real-World Example

AlphaGo is a groundbreaking AI system developed by Google DeepMind to play the board game Go.

It became the first AI system to defeat professional human Go players and world champions.

Through **deep learning**, AlphaGo:

- Studied enormous amounts of game data
- Discovered hidden strategies and patterns
- Continuously improved through experience

Instead of memorizing moves, AlphaGo learned the underlying principles of the game and made intelligent decisions in complex situations.

### AlphaGo Match

![AlphaGo Match](images/alphago-match.png)

**Video:**

https://www.youtube.com/watch?v=SUbqykXVx0A&t=38s

---

# Types of Machine Learning

Machine learning can generally be divided into two major categories:

1. Supervised Learning
2. Unsupervised Learning

The key difference is whether the training data includes known answers (labels).

---

# 1. Supervised Learning

Supervised learning trains a model using **labeled data**.

Each training example contains:

- Input data
- Correct output (label)

The algorithm learns the relationship between inputs and outputs so it can make predictions on new data.

---

## Learning with a Teacher

Supervised learning is similar to learning with a teacher.

The model is shown examples along with correct answers and gradually learns how to produce correct outputs on its own.

---

## How Supervised Learning Works

1. Provide labeled training data.
2. Learn patterns and relationships.
3. Compare predictions with actual answers.
4. Correct errors.
5. Improve accuracy over time.

### Visualization

```text
Training Data (Input + Correct Answer)
                ↓
   Machine Learning Algorithm
                ↓
          Learns Patterns
                ↓
      Predicts New Results
```

---

## Example: Image Recognition

Suppose we provide thousands of dog images:

```text
Image 1 → Dog
Image 2 → Dog
Image 3 → Dog
```

The model learns features such as:

- Shape
- Ears
- Fur patterns
- Facial structure

After sufficient training, it can classify completely new images correctly.

### Example Images

![Dog Classification Example](images/dogs-example.png)

---

# Model Selection in Supervised Learning

Model selection is the process of choosing the most suitable machine learning model for a given problem.

A model is the mathematical or computational method used to identify patterns in data.

Different datasets require different models because every problem has unique characteristics.

Choosing the correct model improves:

- Accuracy
- Efficiency
- Performance

---

## Why Model Selection Matters

The selected model determines:

- How learning occurs
- Prediction accuracy
- Performance on unseen data

Poor model selection can result in:

- Inaccurate predictions
- Slow performance
- Failure to capture important patterns

### Visualization

```text
Training Data
      ↓
Choose Suitable Model
      ↓
Train Model
      ↓
Prediction / Decision
```

---

# Common Supervised Learning Models

## 1. Linear Regression

![Linear Regression](images/linear-regression.png)

Linear Regression predicts continuous numerical values by fitting a straight-line relationship between variables.

### Applications

- House price prediction
- Temperature forecasting
- Sales forecasting

### Key Idea

As one variable changes, another changes proportionally.

---

## 2. Logistic Regression

Logistic Regression is primarily used for classification problems.

### Example Outputs

- Yes / No
- True / False
- Spam / Not Spam

### Applications

- Email spam detection
- Disease prediction
- Student pass/fail prediction

---

## 3. Decision Trees

Decision Trees work like flowcharts and make decisions step by step.

### Visualization

```text
       Is Age > 18?
          /     \
       Yes       No
        |         |
    Approved   Rejected
```

### Applications

- Loan approval systems
- Customer classification
- Medical diagnosis

### Advantages

- Easy to understand
- Easy to visualize

---

## 4. Support Vector Machine (SVM)

Support Vector Machines separate different classes by finding the optimal decision boundary.

### Applications

- Face recognition
- Text classification
- Image classification

### Key Idea

Find the boundary that best separates categories.

---

## 5. Deep Neural Networks

![Deep Neural Network](images/deep-neural-network.png)

Deep Neural Networks use multiple layers of artificial neurons inspired by the human brain.

### Applications

- Self-driving cars
- Speech recognition
- Chatbots
- Image recognition
- AI assistants

### Visualization

```text
Input Layer
     ↓
Hidden Layers
     ↓
Output Layer
```

Deep Neural Networks are particularly powerful for large-scale AI applications.

---

# Choosing the Right Model

The best model depends on several factors:

| Factor | Description |
|----------|-------------|
| Type of Data | Numerical, Text, Images, Audio |
| Problem Type | Classification or Prediction |
| Dataset Size | Small or Large |
| Complexity | Simple or Complex Patterns |
| Accuracy Requirements | Basic or High Performance |

---

## Key Concepts

- There is no single best model for every problem.
- Different problems require different models.
- Machine learning engineers choose the model that best fits the data and task.

---

# Feature Engineering

Feature engineering prepares raw data for machine learning models.

Typical tasks include:

- Data cleaning
- Handling missing values
- Normalization
- Standardization
- Feature selection
- Feature creation

Good feature engineering can significantly improve model performance.

---

# Training and Optimization

Training teaches the model how to make predictions using labeled data.

The process involves:

1. Defining a loss function
2. Measuring prediction errors
3. Reducing errors through optimization

Common optimization techniques include:

- Gradient Descent
- Stochastic Gradient Descent (SGD)

---

# Model Evaluation

After training, models are tested using unseen data.

Common evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC Curve

These metrics help determine whether the model performs reliably in real-world scenarios.

---

# Supervised Learning Summary

The supervised learning workflow consists of:

1. Model Selection
2. Feature Engineering
3. Training and Optimization
4. Evaluation

Together, these steps form the foundation of supervised machine learning.

---

# 2. Unsupervised Learning

Unsupervised learning uses data that has no labels or predefined answers.

The algorithm must discover:

- Patterns
- Relationships
- Similarities

without human guidance.

---

## Example: Grouping Cats and Dogs

Suppose a dataset contains cat and dog images but no labels.

The algorithm can analyze visual similarities and automatically group them into clusters.

This allows the system to discover hidden structures within data.

### Visualization

![Unsupervised Learning](images/unsupervised-learning.png)

---

# Summary

Machine Learning enables computers to learn from data and make intelligent decisions.

The two primary categories are:

| Learning Type | Uses Labels? | Goal |
|---------------|--------------|------|
| Supervised Learning | Yes | Predict outcomes |
| Unsupervised Learning | No | Discover hidden patterns |

Machine learning powers modern technologies such as:

- Recommendation systems
- Chatbots
- Self-driving cars
- Image recognition
- Medical diagnosis
- AI assistants
