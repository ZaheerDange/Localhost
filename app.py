import os
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_code(filename):
    file_path = os.path.join(BASE_DIR, "modules", filename)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return f"# Error: {filename} not found."


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Student Data Mining System",
    page_icon="🎓",
    layout="wide"
)


# =========================================================
# PROJECT TITLE
# =========================================================

st.title("🎓 Student Intelligence and Learning Analytics System")

st.write(
    """
    This project demonstrates different Data Mining techniques
    using student academic, learning, feedback, web, multimedia
    and spatial data.
    """
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📊 Data Mining Techniques")

technique = st.sidebar.selectbox(
    "Select Technique",
    [
        "Home",
        "ID3",
        "J48",
        "Naive Bayes",
        "Decision Tree",
        "K-NN",
        "K-Means",
        "Apriori",
        "Text Mining",
        "Web Mining",
        "Multimedia Mining",
        "Spatial Mining"
    ]
)


# =========================================================
# HOME
# =========================================================

if technique == "Home":

    st.header("🏠 Project Dashboard")

    st.write(
        """
        The system applies different Data Mining techniques
        to solve different types of problems in education.
        """
    )

    st.subheader("📚 Techniques Covered")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            """
            🌳 **ID3**

            Classification

            Main Concept:
            Information Gain
            """
        )

        st.info(
            """
            🌳 **J48**

            Classification

            Main Concept:
            C4.5 Decision Tree
            """
        )

        st.info(
            """
            🎲 **Naive Bayes**

            Classification

            Main Concept:
            Probability
            """
        )

        st.info(
            """
            🌳 **Decision Tree**

            Classification

            Main Concept:
            Gini / Decision Rules
            """
        )

    with col2:

        st.info(
            """
            👥 **K-NN**

            Classification

            Main Concept:
            Distance / Neighbours
            """
        )

        st.info(
            """
            🔵 **K-Means**

            Clustering

            Main Concept:
            Clusters / Centroids
            """
        )

        st.info(
            """
            🛒 **Apriori**

            Association Mining

            Main Concept:
            Support / Confidence / Lift
            """
        )

        st.info(
            """
            📝 **Text Mining**

            Text Analysis

            Main Concept:
            Frequency / TF-IDF
            """
        )

    with col3:

        st.info(
            """
            🌐 **Web Mining**

            Web Analysis

            Main Concept:
            Web Behaviour
            """
        )

        st.info(
            """
            🎥 **Multimedia Mining**

            Multimedia Analysis

            Main Concept:
            Feature Groups
            """
        )

        st.info(
            """
            📍 **Spatial Mining**

            Spatial Analysis

            Main Concept:
            Location / Area Patterns
            """
        )

    st.subheader("🎯 Project Objectives")

    st.write(
        """
        • Predict whether a student is likely to Pass or Fail.

        • Classify students using different classification algorithms.

        • Find groups of similar students.

        • Discover relationships between learning activities.

        • Analyze student feedback.

        • Analyze student behaviour on an online learning portal.

        • Group educational multimedia resources.

        • Identify patterns in different geographical areas.
        """
    )

    st.subheader("🔄 Common Data Mining Flow")

    st.code(
        """
Load Data
    ↓
Select Features
    ↓
Create Model
    ↓
Apply Algorithm
    ↓
Generate Result
    ↓
Interpret Result
        """,
        language="text"
    )


# =========================================================
# ID3
# =========================================================

elif technique == "ID3":

    st.header("🌳 ID3 Classification")

    st.write(
        """
        ID3 is a decision tree classification algorithm.
        It uses Entropy and Information Gain to select
        the best attribute for splitting the data.
        """
    )

    st.subheader("💻 Python Source Code (`modules/id3.py`)")
    st.code(load_code("id3.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        **ID3 follows these basic steps:**

        1. Calculate Entropy
        2. Calculate Information Gain
        3. Select the best attribute
        4. Create the Decision Tree
        5. Predict Pass / Fail

        The attribute with the best split becomes an
        important decision point in the tree.
        """
    )


# =========================================================
# J48
# =========================================================

elif technique == "J48":

    st.header("🌳 J48 Classification")

    st.write(
        """
        J48 is Weka's implementation of the C4.5 decision tree.
        In this Python project, an entropy-based decision tree
        is used as a C4.5-style implementation.
        """
    )

    st.subheader("💻 Python Source Code (`modules/j48.py`)")
    st.code(load_code("j48.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        J48 is based on the C4.5 decision tree approach.

        Tree Depth tells us how deep the tree is.

        Number of Leaves tells us how many final decision
        nodes are present.
        """
    )


# =========================================================
# NAIVE BAYES
# =========================================================

elif technique == "Naive Bayes":

    st.header("🎲 Naive Bayes Classification")

    st.write(
        """
        Naive Bayes uses probability to predict
        the class of a student.
        """
    )

    st.subheader("💻 Python Source Code (`modules/naive_bayes.py`)")
    st.code(load_code("naive_bayes.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        Naive Bayes calculates the probability of each class.

        The class having the highest probability
        is selected as the prediction.
        """
    )


# =========================================================
# DECISION TREE
# =========================================================

elif technique == "Decision Tree":

    st.header("🌳 Decision Tree Classification")

    st.write(
        """
        Decision Tree creates decision rules and uses
        them to classify students.
        """
    )

    st.subheader("💻 Python Source Code (`modules/decision_tree.py`)")
    st.code(load_code("decision_tree.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        Decision Tree divides data using decision rules.

        In this practical, Gini is used as the splitting criterion.
        """
    )


# =========================================================
# K-NN
# =========================================================

elif technique == "K-NN":

    st.header("👥 K-Nearest Neighbours")

    st.write(
        """
        K-NN classifies a student by looking at
        nearby training observations.
        """
    )

    st.subheader("💻 Python Source Code (`modules/knn.py`)")
    st.code(load_code("knn.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        K-NN predicts a student's class by looking
        at the nearest K observations.

        Key idea:
        Distance → Neighbours → Classification
        """
    )


# =========================================================
# K-MEANS
# =========================================================

elif technique == "K-Means":

    st.header("🔵 K-Means Clustering")

    st.write(
        """
        K-Means groups students having similar academic characteristics.
        """
    )

    st.subheader("💻 Python Source Code (`modules/kmeans.py`)")
    st.code(load_code("kmeans.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        K-Means is a clustering algorithm.

        It does not predict Pass or Fail.

        It groups similar students into clusters.

        Cluster numbers such as 0, 1 and 2 are labels only.
        Their meaning should be understood from the
        Cluster Summary.
        """
    )


# =========================================================
# APRIORI
# =========================================================

elif technique == "Apriori":

    st.header("🛒 Apriori Association Rule Mining")

    st.write(
        """
        Apriori discovers relationships between
        frequently occurring learning activities.
        """
    )

    st.subheader("💻 Python Source Code (`modules/apriori.py`)")
    st.code(load_code("apriori.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        Apriori finds relationships between items.

        Support     → How frequently items occur together.

        Confidence  → How often the rule is correct.

        Lift        → Strength of the relationship.
        """
    )


# =========================================================
# TEXT MINING
# =========================================================

elif technique == "Text Mining":

    st.header("📝 Text Mining")

    st.write(
        """
        Text Mining analyzes student feedback
        and identifies important words.
        """
    )

    st.subheader("💻 Python Source Code (`modules/text_mining.py`)")
    st.code(load_code("text_mining.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        Text Mining converts text into useful information.

        Word Frequency → Shows commonly used words.

        TF-IDF → Identifies words that are important
        within the documents.
        """
    )


# =========================================================
# WEB MINING
# =========================================================

elif technique == "Web Mining":

    st.header("🌐 Web Mining")

    st.write(
        """
        Web Mining analyzes how students use
        an online learning portal.
        """
    )

    st.subheader("💻 Python Source Code (`modules/web_mining.py`)")
    st.code(load_code("web_mining.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        Web Mining analyzes student interaction
        with an online learning system.

        Important variables include:

        • Login Count
        • Pages Visited
        • Video Watching Time
        • Quiz Attempts
        • Assignment Downloads
        """
    )


# =========================================================
# MULTIMEDIA MINING
# =========================================================

elif technique == "Multimedia Mining":

    st.header("🎥 Multimedia Mining")

    st.write(
        """
        Multimedia Mining analyzes educational
        image and video resources.
        """
    )

    st.subheader("💻 Python Source Code (`modules/multimedia_mining.py`)")
    st.code(load_code("multimedia_mining.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        Multimedia Mining represents multimedia
        using measurable features.

        Example:

        Brightness
        Size
        Duration

        Similar resources can then be grouped together.
        """
    )


# =========================================================
# SPATIAL MINING
# =========================================================

elif technique == "Spatial Mining":

    st.header("📍 Spatial Mining")

    st.write(
        """
        Spatial Mining identifies patterns in
        area-level student data.
        """
    )

    st.subheader("💻 Python Source Code (`modules/spatial_mining.py`)")
    st.code(load_code("spatial_mining.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        Spatial Mining studies patterns related to location.

        In this project we analyze:

        • Area
        • Latitude
        • Longitude
        • Number of Students
        • Attendance
        • Average Marks
        """
    )


# =========================================================
# FOOTER
# =========================================================

st.sidebar.markdown("---")

st.sidebar.write(
    "🎓 Student Data Mining Project"
)

st.sidebar.write(
    "Python + Pandas + Scikit-learn + Streamlit"
)