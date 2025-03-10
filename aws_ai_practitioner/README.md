# AI Practitioner

## What is Artificial Intelligence? 

* Is the field of computer science dedicated to solving problmes that we commonly associate with human intelligence
* Examples:
    * Image creation
    * Image recognition
    * Speech-to-text
    * Learning
* How is it work?
    * Get training dataset
    * Data Scientist:
        * Design a Model
        * Train a Model
    * Classification Algorithm
    * User can get the information
* History of AI:
    * 1950 Alan Turing with the Turing Test
    * John McCarthy coins "Artificial Intelligence"
    * 1970 Expert Systems, AI Rule-based system to detect bacteria
    * 1990 Machine Learning and Data Mining
    * 1997 Deep Blue defeats Garry Kasparov
    * 2010 Deep Learning Revolution (Example 2016 - Alpha Go)
    * 2020 Virtual assistant
* AI Use Cases:
    * Transcribe and Translate Spoken Language
    * Playing humans in games
    * Driving cars, flying airplanes
    * Speech Recognition and generation
    * Suggesting code for developers
    * Medical Diagnosis
    * Automating Business Process
    * Fraud Detection
* AI techniques leveraged:
    * Computer Vision
    * Deep Learning
    * Natural Language Processing (NLP)
* Areas:
    * Artifical Intelligence
    * Machine Learning that uses Neural Networks
    * Deep Learning
    * Generative AI

## Introduction to AWS and Cloud Computing

* Components of cloud Computing:
    * CPU
    * Memory
    * Storage
    * Databases
    * Network

* Cloud Computing Deployment Models:
    * Private Cloud
    * Hybrid Cloud
    * Public Cloud
    * Multi-Cloud

* Six Advantages of Cloud Computing:
    * Change CAPEx for OPEx
    * Stop guessing capacity
    * Stop spending money mantaining servers
    * Go global in minutes
    * Velocity and Agility
    * Benefits for scale economies

* Types of Cloud Computing
    * IaaS: EC2
    * PaaS: Elastic Beanstalk
    * SaaS: Chime, Rekognition

* Pricing of the cloud:
    * Compute
    * Storage
    * Out data

* How to choose the correct Region:
    * Compliance
    * Latency
    * Services
    * Pricing

* Global services:
    * IAM
    * CloudFront
    * Route53
    * WAF

* AWS Acceptable Use Policy:
    * No ilegal, of Offensive use or Content
    * No security violations
    * No Netwrok abuse
    * No E-Mail or other message abuse

* Create a Budget:
    * To allow, in root session, to get access to Billing and Management service


## Amazon Bedrock and Generative AI

* What is Generative AI?
    * Is a subset of Deep Learning
    * Generate new data similar to the data it was trained
        * Text
        * Audio
        * Image
        * Code
        * Video
    * Unlabeled Data > Foundation Model > Broad range of general tasks
    * Foundation Model:
        * Are trained on wide variety of input data
        * GTP-4o, OpenAI, Meta, Amazon, Google, Anthropic
        * OpenSource: Meta, GoogleBERT
        * Commercial License: OpenAI, Anthropic
    * Large Language Models LLM:
        * Type of AI designed to generate coherent human-like text
        * Training
            * Books
            * Articles
            * Website
        * Tasks
            * Translation, Summarization
            * Question Answering
            * Content Creation
    * Generative Language Models:
        * Process:
            * Prompt
            * Model takes the information that it was trained
            * Answer
        * We usually interact with the LLM by giving a prompt
        * Non-deterministic: the generated text may be different for every user that uses the same prompt
        * Works word by word: After the rain, the streets were flooded
    * Generative AI for images
        * Generates the images based on prompts
        * Prompt -> images
        * Images -> images
        * Text -> images
    * Diffusion Models
        * Picture -> Training: Forward diffusion process -> Noise
        * Noise -> Generating: Reverse diffusion process -> Picture
    
* Amazon Bedrock Overview and Hands On:
    * Build Generative AI applications on AWS
    * Foundation Models:
        * AI21labs
        * Cohere
        * Stability.ai
        * Amazon
        * Anthropic
        * Meta
        * Mistral AI
    * None of your data is using to train the Foundation Models
    * Using Bedrock:
        * Select model
        * Insert the prompt
        * Knowledge Bases in RAG
            * More relevant and accurate responses
        * Fine-Tuning:
            * Update the model with your data
        * Output

* Amazon Bedrock Hands-on
    * Base Foundation Model
        * Model types
        * Performance requirements
        * Capabilities
        * Constraints
        * Compliance
        * Level of customization
        * Model Size
        * Inference options
        * Licesing agreements
        * Context window
        * Latency
        * Multimodal
    * Amazon Titan
        * High-performing Foundation Models from AWS
        * Image, text, multimodal model choices via a fully-managed APIs
        * Can be customized with your own data
        * Smaller models are more cost-effective
    * Options
        * Playground
            * Chat
            * Text
            * Images
        * Custom Models
            * Fine-tuning
        * Hyperparameters
            * Epochs
            * Batch Size
            * Learning rate
            * Learning rate warmup steps
    * Fine-Tuning a Model
        * Adapt a copy of a foundation model with your own data
        * Fine-tuning will change the weight of the base foundation model 
        * Training data must:
            * Adhere to a specific format
            * Be stored in Amazon S3
        * You must use "Provisiones Throughput" to use fine-tuned model
        * Instruction-based Fine Tuning
            * Improves the performance a pre-trained FM on domain-specific tasks
            * = further trained on a particular field or area of knowledge
            * Instruction-based fine-tuning uses labeled examples that are prompt-response pairs
        * Continued Pre-training
            * Provide unlabeled data to continue the training of an FM
            * Also called domain-adaptation fine-tuning, to make a model expert in a specific domain
            * For example: feeding the entire AWS documentation to a model to make it an expert on AWS
            * Good to feed industry-specific terminology into a model
            * Can continue to train the model as more data become available
        * Single-Turn Messaging
            * Part of instruction-based fine-tuning
            * system: context for the conversation
            * messages: an array of messages objects
                * role: either user or assistant
                * content: the text content of the message
        * Multi-Turn Messaging
            * To provide instruction-based fine tuning for a conversation
            * Chatbots = multi-turn environment
            * You must alternate between "user" and "assistant" roles
        * Transfer Learning:
            * the broader concept of reusing a pre-trained model to adapt it to a new related task
                * Widely used for image classification
                * And for NLP (models like BERT and GPT)
            * Can apper as a general ML concept
            * Fine-tuning is a specific kind of transfer learning

### Foundation Model - Evaluation

* Evaluate a model for quality control:
    * Built-in task types:
        * Text summarization
        * Question and answer
        * Text classification
        * Open-ended text generation
    * Bring you own prompt dataset or use built-in curated prompt datasets
    * Scores are calculated automatically
    * Benchmark Datasets
        * Curated collections of data designed specifically at evaluating the performance of lenguage models
    * Human evaluation
    * Automated Metrics to Evaluate an FM
        * ROUGE: Recall-Oriented Understudy for Gisting Evaluation
            * Evaluating automatic summarization and machine learning translation systems
            * ROUGE-N: Measure the number of matching n-grams between reference and generated text
            * ROUGE-L: longest common subsequence between reference and generated text
        * BLEU: Bilingual Evaluation Understudy
            * Evaluate the quality of generated text, especially for translations
            * Considers both precision and penalize too much brevity
            * Looks at a combination of n-grams
        * BERTScore
            * Semantic similarity between generated text
            * Uses pre-trained BERT models (Bidirectional Encoder Representations from Transformers)
        * Perplexity: How well the model predicts the next token
            * lower is better
        * User satisfaction
        * ARPU: Average Revenue per User
        * Cross-Domain Performance
        * Conversion Rate
        * Efficiency

### RAG and Knowledge Base

* RAG: Retrieval-Augmented Generation
    * Use the Foundation Model and real time information
    * Query + Retrieval text
    * Retrieval text
        * Using knowledge base + Amazon S3 + Vector Database
    * RAG Vector Database
        * Services
            * Open Search
            * Aurora
            * Mongo DB
            * Redis
            * Pinecone
        * Process:
            * Amazon S3 -> Document Chunks -> Embeddings Models -> Vector Database
            * Embeddings Models are the models used to create the Vector Database
        * Right Vector Databases:
            * Amazon OpenSearch Service
                * search and analytics database real time similarity queries
                * store millions of vector embeddings scalable index management
                * fast nearest-neighbor (kNN) search capability
            * Document DB
            * Amazon Aurora
            * Amazon RDS
            * Amazon Neptune
        * RAG Data Sources
            * Amazon S3
            * Confluence
            * SharePoint
            * Salesforce
            * Websites
        * Use Cases
            * Customer Service Chatbot
            * Legal Research and Analysis
            * Healthcare Question-Answering

* Lab: Builder tools > Knowledge Base

* GenAI Concept:
    * Tokenizations: 
        * Convert raw text into a sequence of tokens
    * Context window: 
        * The number of tokens an LLM can consider when generating text
        * First facto to look at when considering a model
    * Embeddings:
        * Create vectors out of text, images or audio
        * Dimentionality reduction of word embeddings to 2D
    * All together: 
        * Phrase
        * Tokenization
        * Have Token ID and Token
        * Embeddings models
        * Create Vectors
        * Vector Database
        * Nearest Neighbor capabilities

* Amazon Bedrock Guardrails:
    * Control the interaction between users and Foundation Models
    * Block topics
    * Reduce hallucinations
    * Remove Personal Identifiable Information (PII)

* Agents
    * Manage various multi-step tasks related to infrastructure, deployment and operational activities. 
    * Integration:
        * Tasks -> Bedrock Agent -> All information -> Bedrock Model -> Chain of Thought -> List of steps -> Actions (API call - results) -> Result -> Task + Result -> Model to summarize -> Final Response

* CloudWatch Integration
    * Model Invocation Logging
        * Bedrock:
            * CloudWatch Logs
            * Amazon S3
    * CloudWatch Metrics:
        * Bedrock:
            * Cloudwatch Metrics

* Labs -> You should configure it in settings

* Other features:
    * Bedrock Studio: 
        * give access to Amazon Bedrock to your team so they can easily create AI-powered applications
    * Watermark detection
        * check if an image was generated by Amazon Titan Generator

* Pricing:
    * On-Demand
    * Batch
        * Multiple predictions at a time (output is a single file in Amazon S3)
        * Provides up to 50% discounts
    * Provisioned Throughput
        * Mantain a base capacity
    * Temperature, Top K, Top P no impact on pricing

* Model improvement techniques cost order:
    * Prompt Engineering
    * Retrieval Augmented Generation
    * Instruction-based fine-tuning
    * Domain-adaptation fine-tuning

## Prompt Engineer

* Prompt:
    * little guidance and leaves a lot to the model's interpretation
    * Promt Engineering: developing, designing, and optimizing prompts to enhance the output of FM for your needs
    * Improved Prompting technique consists of:
        * Instructions 
        * Context
        * Input Data
        * Output Indicator
    * Negative Prompting:
        * Avoid Unwanted Content
        * Maintain Focus
        * Enhance Clarity

* Prompt performance Optimization
    * System prompts: how the model should behave and reply
    * Temperature (0 to 1): creativity of the model's output
    * Top P (0 to 1): most likely words when is closer to 0
    * Top K (0 to n): limits the number of probable words
    * Length: maximum lenght of the answer
    * Stop sequences: token that signal the model to stop generating output
    * Prompt latency: is how fast the model responds
        * The model size
        * The model type itself
        * The number of tokns in the input
        * The number of tokens in the output
        * Latency is not impacted by Top P, Top K and Temperature

* Prompt Engineering Techniques
    * Zero-shot prompting
        * without providing examples or explicit training for that specific task
    * Few-shot prompting
        * provide examples of a task to the model to guide its output
    * Chain of thought prompting:
        * Divide the task into a sequence of reasoning steps, leading to more structure and coherence
    * Retrieval-Augmented Generation (RAG)
        * Combine the model's capability with external data sources to generate a more informed and contextually rich response

* Prompt Templates:
    * Simplify and standardize the process of generating Prompts
    * Prompt Template Injections
        * Ignoring the prompt template

## Amazon Q

* Amazon Q Business
    * Fully managed Gen-AI assintant for your employees
    * based on your company's knowledge and data
    * Data Connectors -> Amazon Q Business -> Plugins
    * Users can be authenticated trough IAM Identity Center
    * Admin controls:
        * Admin controls == Guardrails
        * Respond only with internal information
        * Controls and customize responsers to your organizational needs

Labs: Hands On

* Amazon Q Apps
    * Part of Q Business
    * Create Gen AI-powered apps tirhout coding by using natural language

* Amazon Q Developer
    * Answer questions about the AWS documentation and AWS service selection
    * Answer questions about resources in your AWS account
    * Suggest CLI to run make changes to your account
    * AI code companion to help you code new applications

* Amazon Q for AWS Services
    * Amazon Quicksight
        * Amazon Q understands natural language that you use to ask questions about your data
    * Elastic Compute Cloud
        * Amazon Q provides guidance and suggestions for EC2 instance types that are best suited to your new workload
    * AWS Chatbot: is a way for you to deploy an AWS Chatbot in a Slack or Teams
        * Amazon Q can access directly in AWS Chatbot to accelerate understanfing of the AWS services, issues, and general support

* Party Rock
    * Playground to generate AI apps

# Artificial Intellignece and Machine Learning

* What is AI?
    * Performing tasks that tipically require human intelligence
* AI Components:
    * Data Layer
    * ML Framework and Algorithm Layer
    * Model Layer
    * Application Layer

* What is ML?
    * Make predictions based on data used to train model
    * Examples:
        * Regression
        * Classification

* AI is not ML

* What is Deep Learning?
    * Uses neurones and synapses to train a model
    * It uses nodes
    * Process more complex patterns in the data than traditional ML
    * Input Layer -> Hidden Layers -> Output Layer
    * Ex: 
        * Computer Vision
        * Natural Language Processing

* What is GenAI?
    * Multi-purpose foundation models backed by neural networks

* What is the Transformer Model?
    * Able to process a sentence as a whole instead of word by word
    * Ex: ChatGPT = Chat Generative Pretrained Transformer
    * Diffusion Models
    * Multi-modal Models: a lot of input types - a lot of output types

* ML terms in the exam:
    * GPT: Generative Pre-trained Transform
    * BERT: Bidirectional Encoder Representations from Transformers
        * It reads the text in two directions
    * RNN: Recurrent Neural Network
    * ResNet: Residual Network
    * SVM: Support Vector Machine
    * WaveNet
    * GAN: Generative Adversarial Network
    * XGBoost: Extreme Gradient Boosting

* Training Data
    * To train our model we must have good data
    * Data
        * Labeled Data
        * Unlabeled Data
    * Structure
        * Structured Data
        * Unstructured Data

* Supervised Learning
    * Learn a mapping function that can predict the output for new unseen input data
    * Classification Model
    * Models:
        * Regression
        * Classification
    * Training: 80%
    * Validation: 10%
    * Test: 10%
    * Feature Engineering
        * The process of using domain knowledge to select and transform raw data into meaningful features
        * Types
            * Creation
            * Selection
            * Transformation

* Unsupervised learning
    * Discover inherent patterns, structures or relationships within the input data

* Semi-supervised Learning
    * Use a small amount of labeled data and a large amount of unalbeled data to train system

* Reinforcement Learning (RL)
    * An agent learns to make decision by performing actions in an environment to maximize cumulative rewards
    * Key Concept:
        * Agent
        * Environment
        * Action
        * Reward
        * State
        * Policy
    * Applications
        * Games
        * Robotics
        * Finance
        * Healthcare
        * Autonomous vehicle

* Reinforcement Learning from Human Feedback
    * Human are the responsibles
    * How does it work?
        * Data Collection
        * Supervised fine-tuning of a language model
        * Build a separate reward model
        * Optimize the language model with the reward-based model
    * Process:
        * Step 1 Supervised Fine-Tuning
        * Step 2 Training a Reward Model
        * Step 3 Optimize Policy

* Model fit:
    * Overfitting: Very well on the training data but not on evaluation data
    * Underfitting: Model perform poorly on training data
    * Balanced: Neither overfitting or underfitting

* Bias
    * Difference or error between predicted and actual value

* Variance
    * How much the performance of a model changes if trained on a different dataset which has a similar distribution

* Model Evaluation
    * Binary Classification Example
        * Confusion Matrix
            * Precision = TP / (TP + FP), best when false positive are costly
            * Recall = TP / (TP + FN), Best when false negatives are costly
            * F1 
            * Accuracy
        * Area under the curve-receiver operato curve
            * Value from 0 to 1 (perfect model)
    * Regressions Metrics
        * Mean Absolute Error
        * Mean Absolute Percentage Error
        * Root Mean Square Error
        * R-square

* Machine Learning Inferencing
    * Inferencing is when a model is making prediction on new data
    * Real Time
        * Chatbots
    * Batch
        * Large amount of data to analyze at once
    * At the Edge
        * Edge devices like your phone

* Phases of Machine Learning Project
    * Business Problem
    * Frame ML Problem
    * Collect Data
    * Prepared Data
    * Feature Engine
    * Train and fine tuning
    * Model Evaluation
    * Data Augmentation or Feature Augmentation
    * Model Testing
    * Model Deployment
    * Monitoring

* Hyperparameters
    * Settings that define the model structure and learning algorithm and process
    * Importante
        * Learning rate
        * Batch size (number of training examples)
        * Number of Epochs (number of iterations)

* When is not machine learning a good option?
    * Deterministic problems

# AWS Managed AI Services

* Amazon Comprehend:
    * Natural Language Processing
    * Document classification based on rules
    * Sentimental interaction
    * Named Entity Recognition (NER)
* Amazon Transalte:
    * Natural and accurate language translation
* Amazon Transcribe:
    * Speech to text
    * Improving Accuracy
        * Custom Vocabularies; for words
        * Custom Language Models: for context
* Amazon Polly
    * Text to speech
    * Lexicons: How to read certain specific pieces of text
    * SSML: Markup for your text to indicate how to pronounce it
    * Voice engine: generative, long-form, neural, standard
    * Speech mark: Encode where a sentece/word starts or ends in the audio
* Amazon Rekognition
    * Find objects, people, text, scenes in images and videos using ML
    * Process:
        * Labeled Images -> Amazon S3 -> Training -> Amazon Rekognition -> Custom classification
    * Content Moderation
* Amazon Forecast
    * Fully Managed service that uses ML to deliver highly accurate forecast
* Amazon Lex
    * Build chatbots quickly for your applications using voice and text
* Amazon Personalize
    * Fully managed ML-service to build apps with real-time personalized recommendations
    * Recipies
        * Algorithms that are prepared for specific use cases
* Amazon Textract
    * Automatically extracts text, handwriting, and data from any scanned documents using AI and ML
* Amazon Kendra:
    * Fully managed document search service powered by Machine Learning
    * You can fine-tune search results
* Amazon Mechanical Turk
    * Crowdsourcing to perform simple human tasks
* Amazon Augmented AI (A21)
    * Separate High-confidence predictions and Low-confidence predictions
    * low-confidence predictions are reviewed for people
* AWS DeepRacer
    * Reinforcement Learning
* Amazon Transcribe Medical
    * Automatically convert medical-related speech to text
    * Amazon Comprehend Medical
* Hardware for AI
    * Amazon EC2
        * GPU-based EC2 Instances
        * AWS Trainium
        * AWS Inferentia

# Amazon SageMaker - Deep Dive

* Amazon SageMaker
    * Fully managed service for developers / data scientists to build ML models
    * Built-in Algorithms
        * Supervised ALgorithms
        * Unsupervised Algorithms
        * Textual Algorithms
        * Image Processing
    * Automatic Model Tuning (AMT)
    * Model Deployment and Inference
        * Real-time
        * Serverless
        * Asynchronous
        * Batch
    * SageMaker Studio
        * End-to-end ML development from a unified interface

* SageMaker Data Tools
    * Data Wrangler
        * Prepare tabular and image data for machine learning
        * Data preparation, transformation and feature engineering
        * SQL support
        * Data Quality tool
        * Export Data Flow
    * ML Features
        * Features are inputs to ML models used during training and used for inference
        * SageMaker - Feature Store
            * Ingests features from a variety of sources

* SageMaker Clarify
    * Evaluate Foundations Models
    * Evaluating human-factors such as friendliness or humor
    * Model Explainability
    * Detect Bias (human)

* SageMaker Ground Truth
    * Reinforcement Learning from Human Feedback
    * Amazon Mechanical Turk

* SageMaker ML Governance
    * SageMaker Model Cards
    * SageMaker Model Dashboard
    * SageMaker Role Manager
    * SageMaker Model Monitor
    * SageMaker Model Registry
    * SageMaker Pipelines
        * Processing
        * Training
        * Tuning
        * AutoML
        * Model
        * ClarifyCheck
        * QualityCheck

* SageMaker JumpStart
    * ML Hub to find pre-trained Foundation Model

* SageMaker Canvas
    * Build ML models using a visual interface
    * It has Ready-to-use models

* MLFlow on Amazon SageMaker
    * An open-source tool which helps ML teams manage the entire ML lifecycle

# AI Challenges and Responsibilities

* Responsible AI and Security
    * Responsible AI
        * Fairness
        * Explainability
        * Privacy and security
        * Transparency
        * veracity and robustness
        * Governance
        * Safety
        * Controllability
        * Interpretability
    * Security
        * Threat Detection
        * Vulnerability Management
        * Infrastructure Protection
        * Prompt injection
        * Data Encryption
        * Monitoring AI systems
            * Performance Metrics
                * Model Accuracy
                * Precision
                * Recall
                * F1-score
                * Latency
            * Infrastructure monitoring
            * Bias and fairness
    * Governance
        * Managing, optimizing, and scaling the organizational AI initiative
        * AWS Tool:
            * AWS Config
            * Amazon Inspector
            * AWS Audit Manager
            * AWS Artifact
            * AWS CloudTrail
            * AWS Trusted Advisor
        * Governance Strategies
            * Policies
            * Review Cadence
            * Review Strategies
            * Transparency Standards
            * Team Training Requirements
        * Data Governance Strategies
            * Responsible AI
            * Governance Structure and Roles
            * Data Sharing and Collaboration
            * Data Lifecycles
            * Data Logging
            * Data Residency
            * Data Monitoring
            * Data Analysis
            * Data Retention
    * Compliance
        * Reporting regularly to federal agencies
        * Regulated workload
        * Complexity and opacity
        * Dynamism and Adaptability
        * Emergent Capabilities
        * Unique Risks
        * Algorithm accountability

* Secure Data Engineering
    * Assesing data quality
        * Completeness
        * Accuracy
        * Timeliness
        * Consistency
    * Privacy-enhance technologies
    * Data Access Control
    * Data Integrity

* GenAI
    * Challenges
        * Regulatory violations
        * Social risks
        * Toxicity
        * Hallucinations
        * Plagiarism and Cheating
        * Nondeterminism
    * Security Scoping Matrix (Framework)
        * Consumer App
        * Enterprise App
        * Pre-trained Models
        * Fine-tuned Models
        * Self-trained Models
    * MLops
        * Data Pipeline
            * Data preparation
            * Model Build
            * Model Evaluation
            * Model Selection
            * Deployment
            * Monitoring

# AWS Security Services

* IAM
* EC2
* AWS Lambda
* AWS MAcie: machine learning and pattern matching to discover and protect your sensitive data in AWS
* AWS Config auditing and recording compliance of our AWS resources
    * record configurations and changes over time
* Amazon Inspector: Automated Security Assesments only for EC2, Containers and Lambdas
* Amazon CloudTrail
* AWS Artifact
* AWS Audit Manager: Assess risk and compliance of your AWS workloads
* Trusted Advisor: Analyze your AWS accounts and provides recommendation on six categories
* Amazon VPC