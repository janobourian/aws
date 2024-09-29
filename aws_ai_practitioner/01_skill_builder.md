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

* Amazon SageMaker JumpStart
    * Pre-trained models
        * Foundation models
        * Computer vision
        * Natural Language Processing
    * Fine-tune with your data
    * Deploy using Sagemaker

* AWS Glue:
    * Cloud-optimized ETL service
    * Contains its own data catalog
    * Built-in transformations

* AWS Glue Data Catalog:
    * Custom classifiers
    * Built-in classifiers
    * Supported Data Sources
        * Amazon S3
        * Amazon Redshift
    * Put information in Tables (metadata) - Catalog

* AWS Glue DataBrew
    * Visualization and data preparation
        * Explorer and discover
        * Transformation steps saved as a recipe
        * Point-and-click data transformation
    * Data quality rules

* Cycle: Amazon Kinesis Data Streams -> AWS Glue ETL job -> CSV to Parquet -> Amazon S3 Data Lake

* Amazon SageMaker Ground Truth (Amazon SageMaker)
    * Raw data
    * Active learning model is trained from human labeled data
    * Training data the model understands is labeled automatically
    * Ambiguous data is sent to human for annotation

* Amazon SageMaker Canvas
    * Import, prepare, transform, visualize, and analyze
    * Transform 
        * Each adds a step to data flow
        * Built-in transform

* Amazon SageMaker training
    * Training jobs
        * Training data location
        * ML compute instances
        * Training image
        * Hyperparameters
        * S3 output bucket

* Amazon SageMaker experiments
    * Tracks inputs, parameter, configurations as separate runs
    * Compares runs against performance metrics
    * Visual interface

* Amazon SageMaker Automatic Model Tuning:
    * Automatically adjusts hyperparameters
    * Use specified objective metric
    * Tuning job:
        * Runs training jobs inside a loop
        * Satisfies completion criteria

* Amazon SageMaker Model Deployment
    * Choose a SageMaker inference option
        * Batch transfor
        * Asynchronous
        * Serverless
        * Real-time
    * Create an Amazon SageMaker Endpoint Configuration
    * Create an Amazon SageMaker Endpoint

* Amazon SageMaker Model Monitor
    * Data is automatically collecter from your endpoint
    * Define a monitoring schedules and detect changes in quality against a pre-defined baseline
    * Us built-in actions to detect data drift
    * See monitoring results
    * Automate corrective actions based on Amazon Cloudwatch alerts

* Amazon SageMaker Model Building Pipelines
    * Creating pipelines
    * Data Processing
    * Training jobs
    * Creating models
    * Registering models

* ML Pipeline
    * Identify Business Goal
        * Success criteria
        * Aligning stakeholders
    * Frame ML Problem
        * Defining the ML task: inputs, outputs, and metrics
        * Feasibility
        * Starting with simplest model options
        * Cost-benefit analysis
        * Model options
            * AI/ML hosted service
            * Pre-trained models
            * Fully custom model
    * Collect Data (Process Data)
        * Data sources
        * Data ingestion - ETL
        * Labels
    * Pre-process Data (Process Data, Prepare Data)
        * Exploratory data analysis
        * Clean
        * Split - train, validate test
    * Engineer Features (Process Data, Prepare Data)
        * Select features
        * 80 - 10 - 10
        * AWS SageMaker Canvas
    * Train, Tune model
        * Train
            * Iterative process
            * Tune parameters
        * Run experiments
            * Tune hyperparameters
                * Number of layers or neural networks
        * Model evaluation
            * Metrics targets
    * Deploy
        * Considerations
            * Batch inference
            * Real-time inference
            * Self-managed
                * AWS Batch, Amazon ECS, Amazon EKS, AWS Lambda, Amazon EC2
            * Hosted
                * SageMaker inference
    * Monitor
        * Continously monitor the quality of the ML model in real time
        * Identify the right time and frequency to retrain and update the model
        * Configure alerts to notify and initiate actions if any drift in model performance is observed

* ML Operations
    * Application of DevOps principles used in software development to machine learning
    * Infrastructure as code
    * Rapid experimentation
    * Version Control
    * Active performance monitoring
    * Automatic model retraining and validation when there are data and code changes
    * Benefits
        * Productivity
        * Repeatability
        * Reliabiliry
        * Auditability
        * Data and model quality

* Repository options
    * AWS CodeCommit
    * Amazon SageMaker Feature Store
    * Amazon SageMaker Model Registry

* Orchestation Options
    * Amazon SageMaker Pipelines
    * AWS Sterp Functions
    * Amazon Manged Workflows fro Apache Airflow

* Confusion matrix
    * Prediction vs Actual
    * Something like error type one or error type two
    * Accuracy = (True positive + True Negatives) / Total
    * Precision = True positives / (True positives + False positives)
    * Recall = True positives / (True positives + False Negatives), Sensitive
    * F1 = ((Precision * Recall)/( Precision + Recall)) ^2
    * False positive rate = False positives / (True negatives + false positives)
    * True negative rate = True negatives / (True negatives + False positives)
    * Area under the curve - Receiver operating characteristics (ROC)
    * Regression model errors
        * Mean squared error (MSE)
            * Average of the square of the errors
        * Root mean squared error (RMSE)
            * Square root of MSE
        * Mean absolute error (MAE)