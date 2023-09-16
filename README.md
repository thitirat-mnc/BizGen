# BizGenerator💰🏢  [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bizgen.streamlit.app/)
An application built with Streamlit to assist you in generating innovative business ideas. This tool combines the power of OpenAI's GPT-3.5 Turbo model with the Langchain Python library, offering a simple and intuitive way to spark your entrepreneurial creativity.

## 🔗 Table of Contents
- [Introduction](#introduction)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Explore the app](#explore-the-app)
- [Disclaimer](#disclaimer)

## Introduction 

Are you looking to kickstart your entrepreneurial journey or need some fresh business ideas? BizGenerator is here to assist you! It's a user-friendly web application that makes use of OpenAI's language model and the Langchain library to generate creative business ideas tailored to your specific context and preferences, as well as providing an implementation plan for each generated business by using Sequential chains.

## Key Features
Business Idea Generation: Users provide a business context, and the application generates creative business ideas, including names and competitive advantages.

Business Plan Generation: For each generated business idea, users can create an implementation plan, offering guidance on executing their concept effectively.

## Getting Started

### *Prerequisites*
You'll need an **OpenAI API Key** to use this application. <br>
If you don't have one, visit https://platform.openai.com/account/api-keys
1. Click `+ Create new secret key` button
2. Enter a name (optional)
3. Click `Create  secret key` button
### *Installation*

1. Clone the repository:
   ```shell
   git clone https://github.com/BizGenerator.git
   ```

2. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```

Certainly, let's provide a concise usage guide based on the code you provided:

## Usage

1. **OpenAI API Key**: Enter your OpenAI API key securely in the provided input field.

2. **Business Context**: Describe your business idea or context in detail within the text area. For example, you can input something like, "I want to start a sustainable clothing brand in Thailand."

3. **Number of Businesses to Generate**: Utilize the slider to select the number of business ideas you want to generate (ranging from 1 to 5).

4. **Generate Ideas**: Click the "Generate Ideas" button to start the idea generation process.

5. **View Generated Ideas**: Once the ideas are generated, the application will display a list of business ideas, including names and competitive advantages. Each idea is accompanied by a button labeled "Generate plan for Business [X]" to create an implementation plan for that specific idea.

6. **Generate Plans**: If you wish to create implementation plans for the generated ideas, click the corresponding button labeled "Generate plan for Business [X]". The application will provide you with detailed plans for executing each business concept.

7. **Explore and Refine**: Feel free to explore more business ideas and refine your concepts as needed. The application is designed to help you brainstorm and develop innovative business concepts.

## Explore the app
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bizgen.streamlit.app/)

## Disclaimer
Please note that BizGenerator is a tool designed to assist with brainstorming and idea generation. It does not guarantee the success or feasibility of the generated business ideas. It's essential to conduct thorough research and validation before pursuing any business concept.
