import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize the GPT-2 model and tokenizer
def load_model():
    model_name = "gpt2"  # You can try "gpt2-medium", "gpt2-large", or "gpt2-xl" for better quality
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    return model, tokenizer

# Function to generate a story
def generate_story(prompt, model, tokenizer, max_length=200):
    # Encode the prompt text and generate a sequence of tokens
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.92, top_k=50)
    # Decode the generated tokens into a string
    story = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return story

# Streamlit user interface
def main():
    st.title("AI Story Generator")
    st.markdown("Generate short stories from a prompt using GPT-2!")
    
    # Get user input for the story prompt
    prompt = st.text_area("Enter a prompt for the story:", "Once upon a time,")
    
    if st.button("Generate Story"):
        if prompt:
            # Load the model and tokenizer
            model, tokenizer = load_model()
            
            # Generate the story
            with st.spinner("Generating story..."):
                story = generate_story(prompt, model, tokenizer)
                
            st.write(story)
        else:
            st.warning("Please enter a prompt to generate a story!")

if __name__ == "__main__":
    main()
