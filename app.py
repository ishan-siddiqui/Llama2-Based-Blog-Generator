import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers


## Function to get response from my llama-2 model
def getResponse(input_text,no_words,blog_style):

    ### LLama2 model
    llm=CTransformers(model='/path/to/your/model',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt Template
    template=f"""
        You are a subject matter expert in the field of {blog_style}. Write a blog for this job profile for a topic {input_text}
        within {no_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response


st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter a topic for the Blog")

## Creating 2 more columns for 2 more additional fields

col1,col2=st.columns([5,5])

## Col1 will be used to store number of words
with col1:
    no_words=st.text_input("No. of Words")

## Col2 will be used for whom I am creating this particular Blog in a dropdown box format
# We will be using this information to assign role to our llama-2 model while giving prompt
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','Common People'),index=0)
    
submit=st.button("Generate Blog")

## Final Response
if submit:
    st.write(getResponse(input_text,no_words,blog_style))