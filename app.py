import os

import joblib
import pandas as pd
import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    model_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "churn_model.pkl"
    )

    if not os.path.exists(model_path):
        st.error(
            f"❌ Model file not found.\n\n"
            f"Expected location:\n{model_path}"
        )
        st.stop()

    try:
        return joblib.load(model_path)

    except Exception as e:
        st.error("❌ Could not load the model.")
        st.exception(e)
        st.stop()


model = load_model()


# ============================================================
# HEADER
# ============================================================

st.title("📊 Customer Churn Prediction")

st.markdown(
    """
    Predict whether a telecom customer is likely to **churn**
    based on their demographic, service, contract, and billing information.
    """
)

st.divider()


# ============================================================
# CUSTOMER INFORMATION
# ============================================================

st.subheader("👤 Customer Information")

col1, col2, col3 = st.columns(3)


with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=40,
        step=1
    )

    married = st.selectbox(
        "Married",
        ["Yes", "No"]
    )


with col2:

    dependents = st.number_input(
        "Number of Dependents",
        min_value=0,
        max_value=10,
        value=0,
        step=1
    )

    referrals = st.number_input(
        "Number of Referrals",
        min_value=0,
        max_value=20,
        value=0,
        step=1
    )

    tenure = st.number_input(
        "Tenure in Months",
        min_value=0,
        max_value=100,
        value=12,
        step=1
    )


with col3:

    city = st.text_input(
        "City",
        value="Los Angeles"
    )

    zip_code = st.number_input(
        "Zip Code",
        min_value=0,
        max_value=99999,
        value=90001,
        step=1
    )


# ============================================================
# LOCATION
# ============================================================

st.subheader("📍 Location")

col1, col2 = st.columns(2)


with col1:

    latitude = st.number_input(
        "Latitude",
        value=34.05,
        format="%.6f"
    )


with col2:

    longitude = st.number_input(
        "Longitude",
        value=-118.24,
        format="%.6f"
    )


# ============================================================
# TELECOM SERVICES
# ============================================================

st.subheader("📱 Telecom Services")

col1, col2, col3 = st.columns(3)


with col1:

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["Yes", "No"]
    )


with col2:

    if internet_service == "Yes":

        internet_type = st.selectbox(
            "Internet Type",
            [
                "DSL",
                "Fiber Optic",
                "Cable"
            ]
        )

    else:

        internet_type = "None"

        st.selectbox(
            "Internet Type",
            ["None"],
            disabled=True
        )

    online_security = st.selectbox(
        "Online Security",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    online_backup = st.selectbox(
        "Online Backup",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )


with col3:

    device_protection = st.selectbox(
        "Device Protection Plan",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    tech_support = st.selectbox(
        "Premium Tech Support",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    unlimited_data = st.selectbox(
        "Unlimited Data",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )


# ============================================================
# ENTERTAINMENT SERVICES
# ============================================================

st.subheader("🎬 Entertainment Services")

col1, col2, col3 = st.columns(3)


with col1:

    streaming_tv = st.selectbox(
        "Streaming TV",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )


with col2:

    streaming_movies = st.selectbox(
        "Streaming Movies",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )


with col3:

    streaming_music = st.selectbox(
        "Streaming Music",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )


# ============================================================
# BILLING & CONTRACT
# ============================================================

st.subheader("💳 Billing & Contract")

col1, col2, col3 = st.columns(3)


with col1:

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-Month",
            "One Year",
            "Two Year"
        ]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        [
            "Yes",
            "No"
        ]
    )


with col2:

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Bank Withdrawal",
            "Credit Card",
            "Mailed Check"
        ]
    )

    monthly_charge = st.number_input(
        "Monthly Charge",
        min_value=0.0,
        max_value=500.0,
        value=70.0,
        step=1.0
    )


with col3:

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=10000.0,
        value=1000.0,
        step=10.0
    )

    total_refunds = st.number_input(
        "Total Refunds",
        min_value=0.0,
        max_value=1000.0,
        value=0.0,
        step=10.0
    )


# ============================================================
# ADDITIONAL CHARGES
# ============================================================

st.subheader("💰 Additional Charges")

col1, col2, col3 = st.columns(3)


with col1:

    avg_long_distance = st.number_input(
        "Avg Monthly Long Distance Charges",
        min_value=0.0,
        value=25.0,
        step=1.0
    )


with col2:

    avg_gb_download = st.number_input(
        "Avg Monthly GB Download",
        min_value=0.0,
        value=20.0,
        step=1.0
    )


with col3:

    extra_data_charges = st.number_input(
        "Total Extra Data Charges",
        min_value=0.0,
        value=0.0,
        step=10.0
    )


col1, col2 = st.columns(2)


with col1:

    total_long_distance = st.number_input(
        "Total Long Distance Charges",
        min_value=0.0,
        value=100.0,
        step=10.0
    )


with col2:

    total_revenue = st.number_input(
        "Total Revenue",
        min_value=0.0,
        value=1000.0,
        step=10.0
    )


# ============================================================
# OFFER
# ============================================================

st.subheader("🎁 Offer")

offer = st.selectbox(
    "Current Offer",
    [
        "None",
        "Offer A",
        "Offer B",
        "Offer C",
        "Offer D",
        "Offer E"
    ]
)


# ============================================================
# PREDICTION
# ============================================================

st.divider()

predict_button = st.button(
    "🔍 Predict Customer Churn",
    use_container_width=True,
    type="primary"
)


if predict_button:

    # ========================================================
    # CREATE INPUT DATAFRAME
    # ========================================================

    input_data = pd.DataFrame({

        "Gender": [gender],

        "Age": [age],

        "Married": [married],

        "Number of Dependents": [dependents],

        "City": [city],

        "Zip Code": [zip_code],

        "Latitude": [latitude],

        "Longitude": [longitude],

        "Number of Referrals": [referrals],

        "Tenure in Months": [tenure],

        "Offer": [offer],

        "Phone Service": [phone_service],

        "Avg Monthly Long Distance Charges": [
            avg_long_distance
        ],

        "Multiple Lines": [multiple_lines],

        "Internet Service": [internet_service],

        "Internet Type": [internet_type],

        "Avg Monthly GB Download": [
            avg_gb_download
        ],

        "Online Security": [online_security],

        "Online Backup": [online_backup],

        "Device Protection Plan": [
            device_protection
        ],

        "Premium Tech Support": [
            tech_support
        ],

        "Streaming TV": [streaming_tv],

        "Streaming Movies": [streaming_movies],

        "Streaming Music": [streaming_music],

        "Unlimited Data": [unlimited_data],

        "Contract": [contract],

        "Paperless Billing": [
            paperless_billing
        ],

        "Payment Method": [
            payment_method
        ],

        "Monthly Charge": [
            monthly_charge
        ],

        "Total Charges": [
            total_charges
        ],

        "Total Refunds": [
            total_refunds
        ],

        "Total Extra Data Charges": [
            extra_data_charges
        ],

        "Total Long Distance Charges": [
            total_long_distance
        ],

        "Total Revenue": [
            total_revenue
        ]
    })


    # ========================================================
    # VALIDATE INPUT COLUMNS
    # ========================================================

    expected_columns = [
        "Gender",
        "Age",
        "Married",
        "Number of Dependents",
        "City",
        "Zip Code",
        "Latitude",
        "Longitude",
        "Number of Referrals",
        "Tenure in Months",
        "Offer",
        "Phone Service",
        "Avg Monthly Long Distance Charges",
        "Multiple Lines",
        "Internet Service",
        "Internet Type",
        "Avg Monthly GB Download",
        "Online Security",
        "Online Backup",
        "Device Protection Plan",
        "Premium Tech Support",
        "Streaming TV",
        "Streaming Movies",
        "Streaming Music",
        "Unlimited Data",
        "Contract",
        "Paperless Billing",
        "Payment Method",
        "Monthly Charge",
        "Total Charges",
        "Total Refunds",
        "Total Extra Data Charges",
        "Total Long Distance Charges",
        "Total Revenue"
    ]


    if list(input_data.columns) != expected_columns:

        st.error(
            "❌ Input columns do not match the trained model."
        )

        st.write(
            "Expected columns:",
            expected_columns
        )

        st.write(
            "Received columns:",
            input_data.columns.tolist()
        )

        st.stop()


    # ========================================================
    # MAKE PREDICTION
    # ========================================================

    try:

        prediction = model.predict(input_data)[0]

        probabilities = model.predict_proba(input_data)[0]

        churn_probability = probabilities[1]

        churn_percentage = churn_probability * 100


        # ====================================================
        # RESULT
        # ====================================================

        st.subheader("📈 Prediction Result")


        result_col1, result_col2 = st.columns(2)


        with result_col1:

            if prediction == 1:

                st.error(
                    "🔴 HIGH RISK — Customer Likely to Churn"
                )

            else:

                st.success(
                    "🟢 LOW RISK — Customer Likely to Stay"
                )


        with result_col2:

            st.metric(
                "Churn Probability",
                f"{churn_percentage:.2f}%"
            )


        # ====================================================
        # PROBABILITY BAR
        # ====================================================

        st.write("### Churn Risk Level")

        st.progress(
            int(
                max(
                    0,
                    min(
                        100,
                        round(churn_percentage)
                    )
                )
            )
        )


        # ====================================================
        # RISK INTERPRETATION
        # ====================================================

        if churn_percentage >= 70:

            st.error(
                "⚠️ Very High Churn Risk"
            )

            risk_message = (
                "This customer has a very high predicted "
                "probability of churn. Immediate retention "
                "action is recommended."
            )

            recommendation = (
                "Consider a personalized retention offer, "
                "discount, contract upgrade, dedicated "
                "customer support, or loyalty incentive."
            )


        elif churn_percentage >= 40:

            st.warning(
                "⚠️ Moderate Churn Risk"
            )

            risk_message = (
                "This customer has a moderate predicted "
                "probability of churn. Proactive engagement "
                "may help retain the customer."
            )

            recommendation = (
                "Consider targeted engagement, loyalty "
                "offers, service improvements, or a "
                "personalized communication."
            )


        else:

            st.success(
                "✅ Low Churn Risk"
            )

            risk_message = (
                "This customer has a relatively low "
                "predicted probability of churn."
            )

            recommendation = (
                "Continue regular engagement and maintain "
                "the current customer experience."
            )


        st.write(risk_message)


        # ====================================================
        # BUSINESS RECOMMENDATION
        # ====================================================

        st.subheader("💡 Business Recommendation")

        st.info(recommendation)


        # ====================================================
        # CUSTOMER INPUT SUMMARY
        # ====================================================

        st.subheader("👤 Customer Information Summary")

        with st.expander(
            "View submitted customer information"
        ):

            display_data = input_data.T.rename(
                columns={0: "Value"}
            )

            st.dataframe(
                display_data,
                use_container_width=True
            )


        # ====================================================
        # TECHNICAL DETAILS
        # ====================================================

        with st.expander(
            "🔧 View prediction details"
        ):

            st.write(
                f"**Prediction:** "
                f"{'Churn' if prediction == 1 else 'Not Churned'}"
            )

            st.write(
                f"**Churn probability:** "
                f"{churn_percentage:.2f}%"
            )

            st.write(
                f"**Stay probability:** "
                f"{probabilities[0] * 100:.2f}%"
            )


    except Exception as e:

        st.error(
            "❌ An error occurred while making the prediction."
        )

        st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Customer Churn Prediction | "
    "Machine Learning Project | "
    "Built with Python, Scikit-learn & Streamlit"
)