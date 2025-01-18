import streamlit as st
import llama_integration
import database

def display_menu():
    st.set_page_config(page_title="AI-Powered Personal Assistant", layout="wide")
    st.title("✨ AI-Powered Personal Assistant ✨")
    st.markdown("---")

    # Sidebar Navigation
    st.sidebar.title("🌟 Navigation Menu")
    action = st.sidebar.radio(
        "What would you like to do?",
        ["Ask a Question", "View Tasks", "Add a Task", "Delete a Task", "View Notes", "Add a Note", "Delete a Note"],
    )

    # Main Content Area
    with st.container():
        st.markdown(f"### 🚀 Selected Option: **{action}**")
        st.markdown("---")
        if action == "Ask a Question":
            ask_question_ui()
        elif action == "View Tasks":
            view_tasks_ui()
        elif action == "Add a Task":
            add_task_ui()
        elif action == "Delete a Task":
            delete_task_ui()
        elif action == "View Notes":
            view_notes_ui()
        elif action == "Add a Note":
            add_note_ui()
        elif action == "Delete a Note":
            delete_note_ui()

def ask_question_ui():
    """
    Interactive chat interface with live streaming responses from the assistant.
    """
    st.markdown("### 💬 Chat with Your Assistant")
    prompt = st.text_input("🔍 Type your question or command here:")

    if st.button("💡 Submit"):
        try:
            # Handle commands for task/note management
            if prompt.lower().startswith("add task:"):
                task = prompt[9:].strip()
                database.add_task(task)
                st.success(f"✅ Task added: {task}")
            elif prompt.lower().startswith("delete task:"):
                task = prompt[12:].strip()
                database.delete_task(task)
                st.success(f"✅ Task deleted: {task}")
            elif prompt.lower().startswith("add note:"):
                note = prompt[9:].strip()
                database.add_note(note)
                st.success(f"✅ Note added: {note}")
            elif prompt.lower().startswith("delete note:"):
                note = prompt[12:].strip()
                database.delete_note(note)
                st.success(f"✅ Note deleted: {note}")
            else:
                # Stream LLM response
                st.markdown("🤖 **AI Response:**")
                response_placeholder = st.empty()
                response_text = ""

                # Call the LLM with streaming
                for chunk in llama_integration.query_llama_with_context_stream(prompt):
                    response_text += chunk["message"]["content"]
                    response_placeholder.markdown(f"```{response_text}```")

        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")

def view_tasks_ui():
    st.markdown("### 📝 Your Tasks")
    try:
        tasks = database.get_tasks()
        if tasks:
            for task in tasks:
                st.markdown(f"- {task}")
        else:
            st.info("No tasks found.")
    except Exception as e:
        st.error(f"Error: {str(e)}")

def add_task_ui():
    st.markdown("### ➕ Add a Task")
    with st.form("add_task_form"):
        task = st.text_input("Enter the new task:")
        submitted = st.form_submit_button("✅ Add Task")
        if submitted:
            try:
                database.add_task(task)
                st.success("Task added successfully.")
            except Exception as e:
                st.error(f"Error: {str(e)}")

def delete_task_ui():
    st.markdown("### ❌ Delete a Task")
    try:
        tasks = database.get_tasks()
        if tasks:
            task_to_delete = st.selectbox("Select a task to delete:", tasks)
            if st.button("🗑️ Delete Task"):
                database.delete_task(task_to_delete)
                st.success("Task deleted successfully.")
        else:
            st.info("No tasks to delete.")
    except Exception as e:
        st.error(f"Error: {str(e)}")

def view_notes_ui():
    st.markdown("### 🗒️ Your Notes")
    try:
        notes = database.get_notes()
        if notes:
            for note in notes:
                st.markdown(f"- {note}")
        else:
            st.info("No notes found.")
    except Exception as e:
        st.error(f"Error: {str(e)}")

def add_note_ui():
    st.markdown("### ➕ Add a Note")
    with st.form("add_note_form"):
        note = st.text_input("Enter the new note:")
        submitted = st.form_submit_button("✅ Add Note")
        if submitted:
            try:
                database.add_note(note)
                st.success("Note added successfully.")
            except Exception as e:
                st.error(f"Error: {str(e)}")

def delete_note_ui():
    st.markdown("### ❌ Delete a Note")
    try:
        notes = database.get_notes()
        if notes:
            note_to_delete = st.selectbox("Select a note to delete:", notes)
            if st.button("🗑️ Delete Note"):
                database.delete_note(note_to_delete)
                st.success("Note deleted successfully.")
        else:
            st.info("No notes to delete.")
    except Exception as e:
        st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    display_menu()
