import pandas as pd

def preprocess_facets(df):
    rows = df['Facets'].dropna().astype(str)

    structured = []
    current_category = "General"

    for text in rows:
        text = text.strip()

        if text.endswith(':'):
            current_category = text.replace(':','').strip()
        else:
            structured.append({
                'category': current_category,
                'facet': text
            })

    clean_df = pd.DataFrame(structured)
    return clean_df
