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