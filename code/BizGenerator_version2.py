import streamlit as st
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

# Create a Streamlit page config
st.set_page_config(
    page_title="BizGenerator",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded")


# Sidebar decoration
with st.sidebar:
    st.markdown("# Sparks New Business Ideas👩‍💼📈")
    st.markdown("""
        Leverage the OpenAI API, along with the Langchain Python library, to generate a list of business names, visions, missions, 
        competitive advantages and specific implementation plan
        based on the context given.
        """)
    st.markdown("---")
    "[Get Your OpenAI API Key](https://platform.openai.com/account/api-keys)"
    "[📁 View Source Code](https://github.com/thitirat-mnc/BizGenerator)"

# Define the Langchain model
llm_model = "gpt-3.5-turbo"

# Title decoration
st.title("BizGenerator💰🏢")
openai_api_key = st.text_input("OpenAI API Key", type="password")
os.environ['OPENAI_API_KEY'] = openai_api_key

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

def callback():
    st.session_state.button_clicked = True


# Check if the OpenAI API key is provided
if not openai_api_key:
    st.info("Please add your [OpenAI API key](https://platform.openai.com/account/api-keys) to continue.")
else:
    # Get user input for business context with instructions
    text = st.text_area(
        "Type your business context here. \t e.g., I want to start a sustainable clothing brand in Thailand.",
        help="Provide a description of your business idea or context",
        key="business_context"
    )

    num_ideas = st.slider("Number of Businesses to Generate", 1, 5, 5)

    # "Generate Ideas" button
    if (st.button("Generate Ideas", on_click=callback) or st.session_state.button_clicked) and text:
        # Display "Generating ideas..." message
        generating_message = st.info("Generating ideas...")

        llm = OpenAI(temperature=1)

        business_ideas = []

        for i in range(num_ideas):
            # Define the prompt template for generating business ideas
            business_template = f"""
                Imagine you are a business mentor. Your mission is to guide your mentee in crafting a well-rounded business concept \
                that encompasses a distinctive business name, a clear vision, a compelling mission statement, and a strong competitive advantage. \
                Encourage them to think outside the box and let their creativity flow freely. \
                Your response should be structured under the following topics, each not exceeding 100 words, \
                and should be in the same language as the context provided:

                Context: {text}
                
                **Business Name:**
                
                **Vision:**
                
                **Mission:**
                
                **Competitive Advantage:**
                """

            business_prompt_template = PromptTemplate(
                input_variables=[],
                template=business_template,
                output_variables=[
                    "business_info"
                ]
            )

            # Create the Langchain chain for generating business ideas
            business_chain = LLMChain(llm=llm, prompt=business_prompt_template, output_key="business_info")

            # Generate business idea
            business_output = business_chain({})
            business_ideas.append(business_output["business_info"])
        
        for i, business in enumerate(business_ideas):
            if i > 0:
                st.markdown("---")  # Add a separator between ideas
            st.subheader(f"🔗 Business {i + 1}")
            st.write(business)

            STP_template = f"""
                As an experienced business consultant, your task is to create a concise STP (Segmentation, Targeting, Positioning) analysis for Business Idea {i + 1}. \
                Your response, limited to 100 words, should be in the same language as the context.

                Business Idea {i + 1}:
                {business}

                
                Please structure your response as follows:

                **Segmentation Strategy:**

                **Targeting Strategy:**

                **Positioning Strategy:**

                Imagine you are guiding the business with a clear, actionable strategy as a business consultant:

                """
            
            STP_prompt_template = PromptTemplate(
                input_variables=[],
                template=STP_template,
                output_variables=["STP"]
            )
            
            # Create the Langchain chain for STP
            STP_chain = LLMChain(llm=llm, prompt=STP_prompt_template, output_key="STP")

            second_chain = SequentialChain(
                chains=[business_chain, STP_chain],
                input_variables=[],
                output_variables=[
                    "business_info",
                    "STP"
                ],
                verbose=True
            )
            
            STP_output = second_chain({})
            with st.expander(f"📮 STP "):    
                st.write(STP_output["STP"])
            

            plan_template = f"""
                As an experienced business consultant, your task is to create a concise implementation plan for Business Idea {i + 1}. \
                Your response, limited to 100 words, should be in the same language as the context.

                Business Idea {i + 1}:
                {business}

                Present your response in a numbered list format, delineating each step of the implementation plan. \
                Imagine you are providing a clear, actionable strategy as a business consultant:

                """

            plan_prompt_template = PromptTemplate(
                input_variables=[],
                template=plan_template,
                output_variables=["plan"]
            )

            # Create the Langchain chain for generating plan
            plan_chain = LLMChain(llm=llm, prompt=plan_prompt_template, output_key="plan")

            # This is the second chain where we run business generation and plan generation in sequence
            third_chain = SequentialChain(
                chains=[business_chain, plan_chain],
                input_variables=[],
                output_variables=[
                    "business_info",
                    "plan"
                ],
                verbose=True
            )

            # Generate plan
            plan_output = third_chain({})
            with st.expander(f"📓 Plan for Business {i + 1}"):    
                st.write(plan_output["plan"])

            criticism_template = f"""
            Imagine you are a business critic tasked with evaluating Business Idea {i + 1}, its STP Analysis, and its Implementation Plan. 
            Your response, limited to 100 words, should be in the same language as the context.

            Business Idea {i + 1}:
            {business}

            STP Analysis:
            {STP_output["STP"]}

            Implementation Plan:
            {plan_output["plan"]}
            
            Provide the answer in the following structure:

            **Business Idea Feedback:**
            1. *Strengths:* [Highlight the strengths of the business idea.]
            2. *Suggestions for Improvement:* [Offer constructive suggestions for enhancing the business idea.]

            **STP Analysis Feedback:**
            1. *Strengths:* [Identify the strengths of the STP analysis.]
            2. *Suggestions for Improvement:* [Propose improvements to the STP analysis.]

            **Implementation Plan Feedback:**
            1. *Strengths:* [Point out the strengths of the implementation plan.]
            2. *Suggestions for Improvement:* [Provide recommendations for improving the implementation plan.]

            Your input, structured in numbered lists, will contribute to the refinement and enhancement of these critical components of the business proposal.
            """


            criticism_prompt_template = PromptTemplate(
                input_variables=[],
                template=criticism_template,
                output_variables=["criticism"]
            )

            # Create the Langchain chain for generating criticism
            criticism_chain = LLMChain(llm=llm, prompt=criticism_prompt_template, output_key="criticism")
            
            fourth_chain = SequentialChain(
                chains=[business_chain, STP_chain, plan_chain, criticism_chain],
                input_variables=[],
                output_variables=[
                    "business_info",
                    "criticism"
                ],
                verbose=True
            )

            # Generate plan
            criticism_output = fourth_chain({})
            with st.expander(f"🔖 Criticism for Business {i + 1}"):    
                st.write(criticism_output["criticism"])


        # Remove the "Generating ideas..." message once results are ready
        if generating_message:
            generating_message.empty()

        st.markdown("---")
        st.markdown("Feel free to explore more business ideas and refine your concepts!")


    
