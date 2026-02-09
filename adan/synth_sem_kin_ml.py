import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from semantic_resolver import SemanticResolver
from kinematic_linguistics import get_kinematic_analyzer

# Synthesize semantic and kinematic analysis, then run ML clustering
from sklearn.cluster import KMeans
import numpy as np

queries = [
    "What city does France govern from?",
    "Where does Japan rule from?",
    "Who started Microsoft?",
    "Who created Google?",
    "What is the capital of Germany?",
    "atomic structure of carbon",
    "How many people live in China?",
    "What language do they speak in Brazil?",
    "The quick brown fox jumps over the lazy dog.",
    "Colorless green ideas sleep furiously.",
    "Hello world",
    "1 + 1 = 2",
    "f(x) = x² + 2x + 1",
    "(unclosed parenthesis",
]

resolver = SemanticResolver()
analyzer = get_kinematic_analyzer()

features = []
for q in queries:
    shape = resolver.detect_shape(q) or "None"
    entity = resolver.extract_entity(q) or "None"
    kin = analyzer.analyze_sentence(q)["kinematic_summary"]
    # Feature vector: [avg_weight, avg_curvature, commitment_profile (numeric), shape (one-hot)]
    commit_map = {"strong": 2, "moderate": 1, "weak": 0}
    shape_map = {s: i for i, s in enumerate(["CAPITAL_OF", "FOUNDER_OF", "ELEMENT_INFO", "POPULATION_OF", "LANGUAGE_OF", "None"])}
    vec = [
        kin["average_weight"],
        kin["average_curvature"],
        commit_map.get(kin["commitment_profile"], 0),
        shape_map.get(shape, 5)
    ]
    features.append(vec)

X = np.array(features)

# Run KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42)
labels = kmeans.fit_predict(X)

for i, q in enumerate(queries):
    print(f"[{labels[i]}] {q}")
    print(f"   Features: {features[i]}")

print("\nCluster centers:")
print(kmeans.cluster_centers_)
