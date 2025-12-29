def build_prompt(conversation, facet_batch):
    facets = ", ".join(facet_batch)

    return f"""
Evaluate the conversation using the following facets:

{facets}

Conversation:
{conversation}

Return ONLY valid JSON in this exact schema:
{{"results":[{{"facet":string,"score":int(1-5),"confidence":float(0-1)}}]}}
"""
