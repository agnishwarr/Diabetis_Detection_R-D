from graphviz import Digraph

# Create a directed graph
flowchart = Digraph("Dataset Processing Pipeline", format="png")

# Nodes
flowchart.node("A", "PIMA Dataset")
flowchart.node("B", "FHGDD Dataset")
flowchart.node("C", "Merged Dataset (PIMA + FHGDD)")
flowchart.node("D", "SMOTE Data Augmentation")
flowchart.node("E", "Augmented Dataset")
flowchart.node("F", "Final Combined Dataset (Original + Augmented)")
flowchart.node("G", "Model Training & Evaluation")
flowchart.node("H", "Performance Metrics:\nAccuracy, F1, Recall, Precision")

# Edges
flowchart.edge("A", "C", label="Merge")
flowchart.edge("B", "C", label="Merge")
flowchart.edge("C", "D", label="Apply SMOTE")
flowchart.edge("D", "E", label="Generate Augmented Data")
flowchart.edge("C", "F", label="Combine")
flowchart.edge("E", "F", label="Combine")
flowchart.edge("F", "G", label="Train & Evaluate Model")
flowchart.edge("G", "H", label="Compute Metrics")

# Save and render
flowchart.render("dataset_pipeline", view=True)
