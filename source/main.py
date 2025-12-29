from loader import load_facets

## importing the facets.csv file with the loader module
df = load_facets("data/Facets Assignment - Facets Assignment.csv")
print(df.head())
print("Rows:", len(df))

## importing the preprocessor module to preprocess the facets data
from preprocessor import preprocess_facets
cleaned_df = preprocess_facets(df)
# print(cleaned_df.head())
# print("Cleaned Rows:", len(cleaned_df))

## importing the facet engine module to create a facet engine object that can be used to any facet dynamically
from facet_engine import FacetEngine
engine = FacetEngine(cleaned_df)
# print("total facets:",len(engine.get_facets()))
# print("Categories:", len(engine.group_by_category()))


# Load Benchmark Conversations from JSON file
import json
import os
import pandas as pd

with open("data/benchmark_conversation.json", "r") as f:
    conversation_objects = json.load(f)

benchmark_conversations = [item["conversation"] for item in conversation_objects]
print(f"Loaded {len(benchmark_conversations)} benchmark conversations")


# Model + Scorer Setup
from model_loader import load_model 
from scorer import SCORER 
model,tokenizer = load_model()
scorer = SCORER(model,tokenizer,batch_size=3)

# sample = "User: You are absolutely useless and horrible. Assistant: I want to help you, but please speak respectfully."
# results = scorer.score(sample, engine.get_facets()['facet'][:10])
# for r in results:
#     print(r)


# now exporting the benmark results part
def export_results(conversations, facets, scorer, filename_prefix):

    checkpoint_file = "checkpoints/progress.json"
    all_rows = []
    start_idx = 0

    ## Resume support if crash happened earlier
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file, "r") as f:
            saved = json.load(f)
            all_rows = saved["rows"]
            start_idx = saved["next_index"]
        print(f"🔁 Resuming from conversation {start_idx + 1}")

    for i in range(start_idx, len(conversations)):
        convo = conversations[i]
        print(f"\n🧪 Processing conversation {i+1} / {len(conversations)}")

        results = scorer.score(convo, facets)
        print("➡️ Returned rows:", len(results))

        for r in results:
            r["conversation_id"] = i + 1
            r["conversation"] = convo
            all_rows.append(r)

        ## save checkpoint after every conversation
        with open(checkpoint_file, "w") as f:
            json.dump({
                "next_index": i + 1,
                "rows": all_rows
            }, f)

        print("💾 Checkpoint saved")

    print("\n🧮 All conversations processed. Writing final files...")

    df = pd.DataFrame(all_rows)
    df.to_csv(f"{filename_prefix}.csv", index=False)

    with open(f"{filename_prefix}.json", "w") as f:
        json.dump(all_rows, f, indent=2)

    print(f"\n✅ Saved: {filename_prefix}.csv and {filename_prefix}.json")

    ## cleanup checkpoint when finished
    os.remove(checkpoint_file)
    print("🧹 Checkpoint cleared")


# unit testing benchmark
# test = scorer.score(
#     benchmark_conversations[0],
#     engine.get_facets()["facet"][:20]
# )
# print("TEST RESULT:", len(test))


# Run Full Benchmark
export_results(
    benchmark_conversations,
    engine.get_facets()["facet"],
    scorer,
    "benchmark_results"
)
