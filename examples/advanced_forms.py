"""
Streamlit++ Sample Project - Advanced Forms

A comprehensive form application demonstrating advanced form components,
validation, multi-step wizards, and interactive user experiences.
"""

import streamlit as st
import streamlit_plus as stp
import pandas as pd
import numpy as np
from datetime import datetime, date
import re
import time

# Page configuration
st.set_page_config(
    page_title="Advanced Forms - Streamlit++",
    page_icon="📝",
    layout="wide"
)

# Custom theme with form-focused colors
theme = stp.custom_theme(colors={
    "primary": "#2563eb",
    "secondary": "#7c3aed",
    "success": "#059669",
    "danger": "#dc2626",
    "warning": "#d97706",
    "info": "#0891b2"
})
stp.set_theme(theme)

# Form validation utilities
class FormValidator:
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_phone(phone):
        pattern = r'^\+?1?[-.\s]?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})$'
        return re.match(pattern, phone) is not None

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        if not re.search(r'[A-Z]', password):
            return False, "Password must contain at least one uppercase letter"
        if not re.search(r'[a-z]', password):
            return False, "Password must contain at least one lowercase letter"
        if not re.search(r'\d', password):
            return False, "Password must contain at least one number"
        return True, "Password is strong"

    @staticmethod
    def validate_credit_card(card_number):
        # Luhn algorithm for credit card validation
        def luhn_checksum(card_num):
            def digits_of(n):
                return [int(d) for d in str(n)]
            digits = digits_of(card_num)
            odd_digits = digits[-1::-2]
            even_digits = digits[-2::-2]
            checksum = sum(odd_digits)
            for d in even_digits:
                checksum += sum(digits_of(d*2))
            return checksum % 10

        card_num = ''.join(filter(str.isdigit, card_number))
        return luhn_checksum(int(card_num)) == 0 and len(card_num) >= 13

# Multi-step form wizard
def registration_wizard():
    st.title("📝 User Registration Wizard")

    # Initialize session state for form steps
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 0

    steps = ["Personal Info", "Contact Details", "Account Setup", "Review & Submit"]

    # Progress indicator
    progress = (st.session_state.current_step + 1) / len(steps)
    st.progress(progress)
    st.markdown(f"**Step {st.session_state.current_step + 1} of {len(steps)}: {steps[st.session_state.current_step]}**")

    # Step navigation
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.session_state.current_step > 0:
            if st.button("⬅️ Previous", key="prev_step"):
                st.session_state.current_step -= 1
                st.rerun()

    with col3:
        if st.session_state.current_step < len(steps) - 1:
            if st.button("Next ➡️", key="next_step"):
                if validate_current_step():
                    st.session_state.current_step += 1
                    st.rerun()
        else:
            if st.button("🚀 Submit", key="submit_form", type="primary"):
                if validate_current_step():
                    submit_registration()
                    st.success("Registration completed successfully!")
                    time.sleep(2)
                    st.session_state.current_step = 0
                    st.rerun()

    # Form steps
    if st.session_state.current_step == 0:
        personal_info_step()
    elif st.session_state.current_step == 1:
        contact_details_step()
    elif st.session_state.current_step == 2:
        account_setup_step()
    elif st.session_state.current_step == 3:
        review_submit_step()

def personal_info_step():
    st.header("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        first_name = st.text_input("First Name *", key="first_name")
        last_name = st.text_input("Last Name *", key="last_name")
        date_of_birth = st.date_input(
            "Date of Birth *",
            min_value=date(1900, 1, 1),
            max_value=date.today(),
            key="dob"
        )

    with col2:
        gender = st.selectbox("Gender", ["Select...", "Male", "Female", "Non-binary", "Prefer not to say"], key="gender")
        nationality = st.selectbox("Nationality", ["Select..."] + ["United States", "Canada", "United Kingdom", "Australia", "Germany", "France", "Japan", "Other"], key="nationality")
        occupation = st.text_input("Occupation", key="occupation")

def contact_details_step():
    st.header("📞 Contact Details")

    col1, col2 = st.columns(2)

    with col1:
        email = st.text_input("Email Address *", key="email")
        phone = st.text_input("Phone Number *", placeholder="+1 (555) 123-4567", key="phone")
        address = st.text_area("Street Address *", key="address")

    with col2:
        city = st.text_input("City *", key="city")
        state = st.selectbox("State/Province", ["Select..."] + ["California", "New York", "Texas", "Florida", "Other"], key="state")
        zip_code = st.text_input("ZIP/Postal Code *", key="zip_code")
        country = st.selectbox("Country *", ["Select..."] + ["United States", "Canada", "United Kingdom", "Australia", "Other"], key="country")

def account_setup_step():
    st.header("🔐 Account Setup")

    col1, col2 = st.columns(2)

    with col1:
        username = st.text_input("Username *", key="username")
        password = st.text_input("Password *", type="password", key="password")
        confirm_password = st.text_input("Confirm Password *", type="password", key="confirm_password")

    with col2:
        security_question = st.selectbox(
            "Security Question *",
            ["Select...", "What was your first pet's name?", "What city were you born in?", "What was your first car?"],
            key="security_question"
        )
        security_answer = st.text_input("Security Answer *", key="security_answer")

        # Password strength indicator
        if password:
            is_valid, message = FormValidator.validate_password(password)
            if is_valid:
                stp.badge("Strong Password", "success")
            else:
                stp.badge(message, "warning")

def review_submit_step():
    st.header("✅ Review & Submit")

    # Display form data
    review_data = {
        "Personal Information": {
            "Name": f"{st.session_state.get('first_name', '')} {st.session_state.get('last_name', '')}",
            "Date of Birth": st.session_state.get('dob', ''),
            "Gender": st.session_state.get('gender', ''),
            "Nationality": st.session_state.get('nationality', ''),
            "Occupation": st.session_state.get('occupation', '')
        },
        "Contact Details": {
            "Email": st.session_state.get('email', ''),
            "Phone": st.session_state.get('phone', ''),
            "Address": st.session_state.get('address', ''),
            "City": st.session_state.get('city', ''),
            "State": st.session_state.get('state', ''),
            "ZIP Code": st.session_state.get('zip_code', ''),
            "Country": st.session_state.get('country', '')
        },
        "Account Setup": {
            "Username": st.session_state.get('username', ''),
            "Security Question": st.session_state.get('security_question', ''),
            "Password": "••••••••" if st.session_state.get('password') else ''
        }
    }

    for section, data in review_data.items():
        with st.expander(f"📋 {section}", expanded=True):
            for key, value in data.items():
                st.write(f"**{key}:** {value}")

    # Terms and conditions
    st.markdown("---")
    agree_terms = st.checkbox("I agree to the Terms and Conditions *", key="agree_terms")
    agree_privacy = st.checkbox("I agree to the Privacy Policy *", key="agree_privacy")
    subscribe_newsletter = st.checkbox("Subscribe to newsletter", key="subscribe_newsletter")

def validate_current_step():
    step = st.session_state.current_step

    if step == 0:  # Personal Info
        if not st.session_state.get('first_name', '').strip():
            st.error("First name is required")
            return False
        if not st.session_state.get('last_name', '').strip():
            st.error("Last name is required")
            return False
        if st.session_state.get('gender') == "Select...":
            st.error("Please select a gender")
            return False
        return True

    elif step == 1:  # Contact Details
        if not FormValidator.validate_email(st.session_state.get('email', '')):
            st.error("Please enter a valid email address")
            return False
        if not FormValidator.validate_phone(st.session_state.get('phone', '')):
            st.error("Please enter a valid phone number")
            return False
        if not st.session_state.get('address', '').strip():
            st.error("Address is required")
            return False
        if not st.session_state.get('city', '').strip():
            st.error("City is required")
            return False
        if st.session_state.get('country') == "Select...":
            st.error("Please select a country")
            return False
        return True

    elif step == 2:  # Account Setup
        if not st.session_state.get('username', '').strip():
            st.error("Username is required")
            return False
        if len(st.session_state.get('username', '')) < 3:
            st.error("Username must be at least 3 characters long")
            return False
        password = st.session_state.get('password', '')
        confirm_password = st.session_state.get('confirm_password', '')
        if not password:
            st.error("Password is required")
            return False
        is_valid, _ = FormValidator.validate_password(password)
        if not is_valid:
            st.error("Password does not meet requirements")
            return False
        if password != confirm_password:
            st.error("Passwords do not match")
            return False
        if st.session_state.get('security_question') == "Select...":
            st.error("Please select a security question")
            return False
        if not st.session_state.get('security_answer', '').strip():
            st.error("Security answer is required")
            return False
        return True

    elif step == 3:  # Review & Submit
        if not st.session_state.get('agree_terms'):
            st.error("You must agree to the Terms and Conditions")
            return False
        if not st.session_state.get('agree_privacy'):
            st.error("You must agree to the Privacy Policy")
            return False
        return True

    return True

def submit_registration():
    # Simulate form submission
    with st.spinner("Submitting registration..."):
        time.sleep(2)

    # Store registration data (in a real app, this would go to a database)
    registration_data = {
        "first_name": st.session_state.first_name,
        "last_name": st.session_state.last_name,
        "email": st.session_state.email,
        "username": st.session_state.username,
        "registration_date": datetime.now(),
        "status": "active"
    }

    # Clear form data
    for key in list(st.session_state.keys()):
        if key.startswith(('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'country', 'username', 'password', 'confirm_password', 'security_question', 'security_answer', 'gender', 'nationality', 'occupation', 'dob', 'agree_terms', 'agree_privacy', 'subscribe_newsletter')):
            del st.session_state[key]

# Advanced form components demo
def advanced_form_components():
    st.title("🎨 Advanced Form Components")

    st.markdown("Explore various advanced form components and their capabilities.")

    # Component tabs
    components = [
        {"label": "Input Controls", "icon": "📝", "content": input_controls_demo},
        {"label": "Selection Controls", "icon": "🎯", "content": selection_controls_demo},
        {"label": "Data Entry", "icon": "📊", "content": data_entry_demo},
        {"label": "Validation", "icon": "✅", "content": validation_demo}
    ]

    stp.tabs(components)

def input_controls_demo():
    st.header("Enhanced Input Controls")

    col1, col2 = st.columns(2)

    with col1:
        stp.card("Text Inputs", """
        Advanced text input with validation, formatting, and real-time feedback.
        """)

        # Enhanced text input with validation
        name = st.text_input("Full Name", placeholder="Enter your full name")
        if name and len(name.strip()) < 2:
            stp.badge("Name too short", "warning")

        # Email with validation
        email_input = st.text_input("Email", placeholder="your@email.com")
        if email_input and not FormValidator.validate_email(email_input):
            stp.badge("Invalid email format", "danger")

        # Password with strength indicator
        pwd = st.text_input("Password", type="password")
        if pwd:
            is_valid, message = FormValidator.validate_password(pwd)
            stp.badge(message, "success" if is_valid else "warning")

    with col2:
        stp.card("Numeric & Date Inputs", """
        Specialized inputs for numbers, dates, and formatted data entry.
        """)

        # Number input with range
        age = st.number_input("Age", min_value=0, max_value=120, value=25)

        # Currency input
        salary = st.number_input("Salary ($)", min_value=0, step=1000, format="%d")

        # Date range
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")

        if start_date and end_date and start_date > end_date:
            stp.badge("End date must be after start date", "danger")

def selection_controls_demo():
    st.header("Advanced Selection Controls")

    col1, col2 = st.columns(2)

    with col1:
        stp.card("Multi-Select & Tags", """
        Enhanced selection with search, tags, and custom styling.
        """)

        # Multi-select with search
        skills = st.multiselect(
            "Skills",
            ["Python", "JavaScript", "React", "SQL", "Machine Learning", "Data Analysis", "UI/UX Design"],
            default=["Python"]
        )

        # Tag input simulation
        tags = st.text_input("Tags (comma-separated)", placeholder="web, mobile, api")
        if tags:
            tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()]
            st.write("Tags:")
            for tag in tag_list:
                stp.badge(tag, "info")

    with col2:
        stp.card("Radio & Checkboxes", """
        Custom styled radio buttons and checkbox groups.
        """)

        # Radio buttons
        experience = st.radio(
            "Experience Level",
            ["Beginner", "Intermediate", "Advanced", "Expert"]
        )

        # Checkbox group
        interests = st.multiselect(
            "Interests",
            ["Technology", "Business", "Design", "Marketing", "Data Science", "AI/ML"]
        )

def data_entry_demo():
    st.header("Data Entry Components")

    col1, col2 = st.columns(2)

    with col1:
        stp.card("File Upload", """
        Advanced file upload with drag-and-drop, validation, and preview.
        """)

        uploaded_file = st.file_uploader("Upload a file", type=['csv', 'xlsx', 'json'])

        if uploaded_file is not None:
            stp.badge(f"File uploaded: {uploaded_file.name}", "success")

            # File preview
            if uploaded_file.type == "text/csv":
                df = pd.read_csv(uploaded_file)
                st.dataframe(df.head())

    with col2:
        stp.card("Rich Text Editor", """
        WYSIWYG editor for formatted text input.
        """)

        # Simulate rich text editor
        bio = st.text_area("Biography", height=150, placeholder="Tell us about yourself...")

        # Formatting options
        bold = st.checkbox("Bold")
        italic = st.checkbox("Italic")
        underline = st.checkbox("Underline")

        if bio:
            formatted_text = bio
            if bold:
                formatted_text = f"**{formatted_text}**"
            if italic:
                formatted_text = f"*{formatted_text}*"
            if underline:
                formatted_text = f"<u>{formatted_text}</u>"

            st.markdown(f"Preview: {formatted_text}", unsafe_allow_html=True)

def validation_demo():
    st.header("Form Validation & Feedback")

    stp.card("Real-time Validation", """
    Advanced validation with custom rules, error messages, and visual feedback.
    """)

    # Credit card validation
    card_number = st.text_input("Credit Card Number", placeholder="1234 5678 9012 3456")

    if card_number:
        # Remove spaces and validate
        clean_card = ''.join(filter(str.isdigit, card_number))
        if len(clean_card) >= 13:
            if FormValidator.validate_credit_card(card_number):
                stp.badge("Valid credit card number", "success")
            else:
                stp.badge("Invalid credit card number", "danger")
        else:
            stp.badge("Card number too short", "warning")

    # URL validation
    website = st.text_input("Website URL", placeholder="https://example.com")

    if website:
        if not website.startswith(('http://', 'https://')):
            stp.badge("URL must start with http:// or https://", "warning")
        else:
            stp.badge("Valid URL format", "success")

    # Custom validation rules
    st.subheader("Custom Validation Rules")

    value = st.number_input("Enter a number between 10 and 100", min_value=0, max_value=200)

    if value < 10:
        stp.badge("Value must be at least 10", "danger")
    elif value > 100:
        stp.badge("Value must be at most 100", "warning")
    else:
        stp.badge("Value is within acceptable range", "success")

# Survey form demo
def survey_form():
    st.title("📊 Interactive Survey")

    st.markdown("Complete this comprehensive survey to help us understand your preferences.")

    # Progress tracking
    total_questions = 5
    completed_questions = sum(1 for i in range(1, total_questions + 1)
                            if f'q{i}_answered' in st.session_state)

    progress = completed_questions / total_questions
    st.progress(progress)
    st.markdown(f"**Progress: {completed_questions}/{total_questions} questions completed**")

    # Survey questions
    questions = [
        {
            "id": 1,
            "question": "How satisfied are you with our service?",
            "type": "rating",
            "options": ["Very Dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very Satisfied"]
        },
        {
            "id": 2,
            "question": "Which features do you use most? (Select all that apply)",
            "type": "multiselect",
            "options": ["Data Visualization", "Form Builder", "Analytics", "Reporting", "API Integration", "Mobile App"]
        },
        {
            "id": 3,
            "question": "How likely are you to recommend us to a friend?",
            "type": "scale",
            "min": 1,
            "max": 10,
            "labels": ["Not at all likely", "Extremely likely"]
        },
        {
            "id": 4,
            "question": "What improvements would you suggest?",
            "type": "textarea",
            "placeholder": "Please share your thoughts..."
        },
        {
            "id": 5,
            "question": "Would you like to receive our newsletter?",
            "type": "radio",
            "options": ["Yes", "No", "Maybe later"]
        }
    ]

    for q in questions:
        with st.container():
            st.markdown(f"### Question {q['id']}: {q['question']}")

            if q['type'] == 'rating':
                response = st.radio(
                    f"q{q['id']}_response",
                    q['options'],
                    key=f"q{q['id']}",
                    horizontal=True
                )
            elif q['type'] == 'multiselect':
                response = st.multiselect(
                    f"q{q['id']}_response",
                    q['options'],
                    key=f"q{q['id']}"
                )
            elif q['type'] == 'scale':
                response = st.slider(
                    f"q{q['id']}_response",
                    q['min'], q['max'],
                    key=f"q{q['id']}"
                )
                st.markdown(f"<small>{q['labels'][0]} ← {response} → {q['labels'][1]}</small>",
                          unsafe_allow_html=True)
            elif q['type'] == 'textarea':
                response = st.text_area(
                    f"q{q['id']}_response",
                    placeholder=q.get('placeholder', ''),
                    key=f"q{q['id']}"
                )
            elif q['type'] == 'radio':
                response = st.radio(
                    f"q{q['id']}_response",
                    q['options'],
                    key=f"q{q['id']}"
                )

            # Mark as answered
            if response:
                st.session_state[f'q{q["id"]}_answered'] = True

            st.markdown("---")

    # Submit survey
    if completed_questions == total_questions:
        if st.button("🚀 Submit Survey", type="primary"):
            st.success("Thank you for completing the survey!")

            # Display results summary
            st.subheader("📈 Survey Summary")
            results = {}
            for q in questions:
                results[q['id']] = st.session_state.get(f"q{q['id']}", "Not answered")

            summary_df = pd.DataFrame({
                'Question': [q['question'] for q in questions],
                'Response': list(results.values())
            })
            st.dataframe(summary_df)

            # Clear survey data
            for key in list(st.session_state.keys()):
                if key.startswith('q') or key.endswith('_answered'):
                    del st.session_state[key]

# Main app
def main():
    # Navigation
    st.sidebar.title("📝 Advanced Forms Demo")

    pages = {
        "📋 Registration Wizard": "wizard",
        "🎨 Form Components": "components",
        "📊 Survey": "survey"
    }

    selected_page = st.sidebar.radio("Select Demo", options=list(pages.keys()))

    # Page routing
    if pages[selected_page] == "wizard":
        registration_wizard()
    elif pages[selected_page] == "components":
        advanced_form_components()
    elif pages[selected_page] == "survey":
        survey_form()

    # Footer
    st.markdown("---")
    st.markdown("*Built with Streamlit++ - Advanced Form Framework*")

if __name__ == "__main__":
    main()