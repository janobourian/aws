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

# AWS Managed AI Services

# Amazon SageMaker - Deep Dive

# AI Challenges and Responsibilities

# AWS Security Services