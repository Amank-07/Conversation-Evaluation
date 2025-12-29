import json
from protocol import build_prompt


class SCORER:
    def __init__(self, model, tokenizer, batch_size=12):
        self.model = model
        self.tokenizer = tokenizer
        self.batch_size = batch_size

    def _query(self, prompt):
        messages = [
            {"role": "system", "content": "You are a strict JSON evaluation engine."},
            {"role": "user", "content": prompt}
        ]

        input_ids = self.tokenizer.apply_chat_template(
            messages,
            return_tensors="pt",
            add_generation_prompt=True
        ).to(self.model.device)

        attention_mask = (input_ids != self.tokenizer.pad_token_id).long()

        output_ids = self.model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_new_tokens=150,
            eos_token_id=self.tokenizer.eos_token_id,
            do_sample=False
        )

        decoded = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

        print("\n--- MODEL RESPONSE ---")
        print(decoded)
        print("---------------------\n")

        return decoded

    def score(self, conversation, facets):
        collected = []

        for i in range(0, len(facets), self.batch_size):
            batch = facets[i:i + self.batch_size]
            prompt = build_prompt(conversation, batch)

            raw = self._query(prompt)

            # 🧠 Extract ONLY the final JSON object
            left = raw.rfind('{"results"')
            right = raw.rfind('}') + 1

            if left == -1:
                print("⚠️ No JSON found")
                continue

            json_text = raw[left:right]

            try:
                payload = json.loads(json_text)
            except Exception as e:
                print("⚠️ JSON parse failed:", e)
                continue

            for row in payload.get("results", []):
                try:
                    score = int(row["score"])
                    confidence = float(row["confidence"])

                    # Enforce assignment constraint: Five ordered integers
                    score = max(1, min(5, score))

                    collected.append({
                        "facet": row["facet"],
                        "score": score,
                        "confidence": confidence
                    })
                except Exception as e:
                    print("⚠️ Skipping bad row:", row, "Error:", e)

        print(f"✅ Collected {len(collected)} scores")
        return collected
