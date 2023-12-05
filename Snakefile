rule prepare:
    output: "data/wine.data"
    script: "scripts/prepare_data.py"

rule profile:
    input: "data/wine.data"
    output: "profiling/report.html"
    script: "scripts/profile.py"

rule analyze:
    input: "data/wine.data"
    output: 
        "results/alcohol_distribution.png",
        "results/classification_accuracy.txt",
        "results/summary_statistics.csv"
    script: "scripts/analyze.py"

