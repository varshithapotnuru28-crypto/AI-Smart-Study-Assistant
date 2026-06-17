import streamlit as st
import os

from src.pdf_reader import extract_text
from src.notes_generator import generate_notes
from src.mcq_generator import generate_mcqs
from src.flashcard_generator import generate_flashcards
from src.interview_generator import generate_interview_questions
from src.study_plan_generator import generate_study_plan
from src.revision_generator import generate_revision_notes
from src.mindmap_generator import generate_mindmap

st.set_page_config(
    page_title="AI Smart Study Assistant",
    layout="wide"
)

st.title("📚 AI Smart Study Assistant")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)

    pdf_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    text = extract_text(pdf_path)

    st.success("✅ PDF Uploaded Successfully")

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "📝 Notes",
        "❓ MCQs",
        "📇 Flashcards",
        "💼 Interview",
        "📅 Study Plan",
        "📖 Revision",
        "🧠 Mind Map"
    ])

    # NOTES

    with tab1:

        if st.button("Generate Notes"):

            with st.spinner("Generating Notes..."):

                notes = generate_notes(text)

                st.markdown(notes)

    # MCQS

    with tab2:

        if st.button("Generate MCQs"):

            with st.spinner("Generating MCQs..."):

                mcqs = generate_mcqs(text)

                st.markdown(mcqs)

    # FLASHCARDS

    with tab3:

        if st.button("Generate Flashcards"):

            with st.spinner("Generating Flashcards..."):

                flashcards = generate_flashcards(text)

                st.markdown(flashcards)

    # INTERVIEW QUESTIONS

    with tab4:

        if st.button("Generate Interview Questions"):

            with st.spinner("Generating Interview Questions..."):

                interview = generate_interview_questions(text)

                st.markdown(interview)

    # STUDY PLAN

    with tab5:

        if st.button("Generate Study Plan"):

            with st.spinner("Generating Study Plan..."):

                study_plan = generate_study_plan(text)

                st.markdown(study_plan)

    # REVISION NOTES

    with tab6:

        if st.button("Generate Revision Notes"):

            with st.spinner("Generating Revision Notes..."):

                revision = generate_revision_notes(text)

                st.markdown(revision)

    # MIND MAP

    with tab7:

        if st.button("Generate Mind Map"):

            with st.spinner("Generating Mind Map..."):

                mindmap = generate_mindmap(text)

                st.markdown(mindmap)