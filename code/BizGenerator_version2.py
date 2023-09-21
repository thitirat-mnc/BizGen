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
        Leverage the OpenAI API, along with the Langchain Python library, to generate a list of business names, 
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
            You are a business mentor. Given the context of business, your job is to help your mentee \
            generate a new business with a unique business name and a strong competitive advantage for that business. \
            For this business, the answer must be within 100 words. 
            Make sure that the answer is in the same language as the language of the context that the user type in.\

            
            context: {text}
            This is business idea {i + 1}:
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

        # Remove the "Generating ideas..." message once results are ready
        if generating_message:
            generating_message.empty()

        st.markdown("---")
        st.header("Business Ideas Generated")

        for i, business in enumerate(business_ideas):
            if i > 0:
                st.markdown("---")  # Add a separator between ideas
            st.subheader(f"🔗 Business {i + 1}")
            st.write(business)

            if st.button(f"Generate plan for Business {i + 1}"):
                # Define the prompt template for generating plan
                plan_template = f"""
                You are a talented business consultant. Your job is to write a implementation plan for business idea {i + 1}.
                For this business, the answer must be within 100 words. 
                Make sure that the answer is in the same language as the language of the Business Idea {i + 1}.

                Business Idea {i + 1}:
                {business}
                implementation plan from a business consultant:
                """

                plan_prompt_template = PromptTemplate(
                    input_variables=[],
                    template=plan_template,
                    output_variables=["plan"]
                )

                # Create the Langchain chain for generating plan
                consultant_chain = LLMChain(llm=llm, prompt=plan_prompt_template, output_key="plan")

                # This is the overall chain where we run business generation and plan generation in sequence
                overall_chain = SequentialChain(
                    chains=[business_chain, consultant_chain],
                    input_variables=[],
                    output_variables=[
                        "business_info",
                        "plan"
                    ],
                    verbose=True
                )

                # Generate plan using consultant_chain
                plan_output = overall_chain({})

                st.subheader(f"📃 Plan for Business {i + 1}")
                st.write(plan_output["plan"])
        st.markdown("---")
        st.markdown("Feel free to explore more business ideas and refine your concepts!")
        
