import streamlit as st
import assistant_view

def main():
    # Configure Streamlit page
    st.set_page_config(
        page_title="AI-Powered Personal Assistant",
        page_icon="✨",
        layout="wide",
    )
    
    # header
    st.title("✨ Welcome to Your AI-Powered Personal Assistant! ✨")
    st.markdown("Your one-stop solution to manage tasks, notes, and get AI-driven responses.")
    st.markdown("---")
    
    assistant_view.display_menu()

if __name__ == "__main__":
    main()
