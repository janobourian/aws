# Domain 1: Fundamentals of AI and ML (Standard AIF)

## Explain basic AI concepts and terminologies

* What is AI?
    * Human-like intelligence
        * Conversations
        * Creation of content
        * Solutions to complex problems
        * Increased business efficiency
        * Smarter decisions
    * Self-learning systems

* What is ML?
    * Use data and algorithm to imitate how humans learn
    * Identify patterns and make predictions
    * Prediction are named inference

* What is Deep Learning?
    * Using layers or neural networks to process information

* Benefits:
    * Health:
        * Diagnosing illness
        * Predict outbreaks
    * Quality:
        * Finding product defects
        * Predective maintenance
    * Customer experience
        * Self-help
        * Recommendations
    * Decision making
        * Forecasting demand
        * Preventing fraud
    * Productivity
        * Hiring
        * Targeted marketing

* What can AI do?
    * Make predictions
    * Detect anomalies
    * Detect defects by using computer vision
    * Translation
    * Natural Language Processing (NLP): Understand and interprete the human language
    * Create content

* Machine Learning:
    * Identify patterns
    * Find correlation
    * Generate or predict
    * Without explicit instructions
    * Process:
        * Known Data
        * Features
        * Mathematical Algorithm (Train)
        * Output
    * Train: Known data
    * Inference: unknown data

* Type of data:
    * Structured: Tables like RDS, Amazon Redshift, Amazon S3
    * Semi-structured: JSON, XML or something in Amazon DynamoDB, Amazon DocumentDB, Amazon S3
    * Unstructured: It does not have a specific format, images, text files or social media post. Store in Amazon S3
    * Time-series: Labeled records with timestamps

* Model Training:
    * Algorithm
    * Training
    * Infering
        * Model
            * Inference code
                * Software that implements the model by reading the artifacts
            * Model artifacts
        * Types:
            * real-time
            * batch transform
    * Parameters

* Supervised learning:
    * Use pre-labeled data
    * For this task:
        * Amazon SageMaker Ground Truth
        * Amazon Mechanical Turk

* Unlabeled data:
    * Cluster the data
    * Pattern recognition
    * It can detect anomalies

* Reinforcement learning:
    * It has a goal
    * Trial and error
    * Maximize rewards
    * Process
        * Agent -> Action -> Environment -> Reward
    * AWS DeepRacer

* Troubleshooting model performance:
    * Overfitting
    * Underfitting
    * Bias and fairness
        * Diversity of training data
        * Feature importance
        * Fairness constraints

* Deep learning:
    * Neural networks
    * layers:
        * Input layers
        * Hidden layers
        * Output layers
    * Tasks:
        * Image classification
        * Natural Language Processing

* Generative AI:
    * Large Language Models
        * Deep learning foundation models
        * Transformers
        * Hundreds of billions of features
        * Flexible use cases:
            * Text clasification
            * Text generation 
            * Translation 
            * Code generation

## Idenitify practical use cases for AI

* Consider AI/ML for:
    * Increasing business efficiency
    * Solving complex problems
    * Making better decisions

* Consider AI/ML alternatives when:
    * Costs outweigh the benefits
    * Models cannot meet the interpretability requirements
    * System must be deterministic rather than probabilistic

* Practical use cases
    * Contains target values?
        * Yes: Supervised learning
            * Categorical: Classification (Binary or multiclass)
            * Continuous: Regression (Linear, multiple or logistic)
        * Not: Unsupervised learning
            * Discrete groups: Clustering
            * Outliers: Anomaly Detection

* Amazon Rekognition: Computer vision
    * Images, videos and streaming
    * Facial comparison and analysis
    * Object detection and labeling
    * Text detection
    * Content moderation

* Amazon Textract
    * Extract text, handwrite, layout elements, and data from scanned documents
* Amazon Comprehend
    * Extract key phrases, entinties, and sentiment
    * For PII

* Language AI
    * Amazon Lex
        * Conversational voice and text
    * Amazon Transcribe
        * Converts speech to text
    * Amazon Polly
        * Converts text to speech

* Customer experience
    * Amazon Kendra
        * Intelligent document search
    * Amazon Personalize
        * Personalized product recommendations
    * Amazon Translate
        * Translates between 75 language

* Business metrics
    * Amazon Forecast
        * Predicts future points in time-series data
    * Amazon Fraud Detector
        * Detects fraud and fraudulent activities
        * Checks online transactions, product reviews, checkout and payments, new accounts, and account takeover

* Generative AI
    * Amazon Bedrock
        * Foundation models
        * Can customize with training data or Retrieval Augmented Generation (RAG)

* Model development
    * Amazon Sagemaker
        * Fully managed ML service
        * Data preparation and labeling
        * Model training and evaluation
        * Model deployment and monitoring
        * Pre-trained models

* Mastercard: Fraud detection and prevention
* DoorDash: Conversational AI for self service
    * Natural language processing: Amazon Lex
    * Full automation of eight services
* Laredo Petroleum: Preventive maintenance
* Booking.com: Product recommendations
* Pinterest: Computer vision
* AffordableTours.com: Amazon Forecast

## Describe the ML development life cycle