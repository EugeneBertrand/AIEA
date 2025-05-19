# inference_engine.py

from pyswip import Prolog

class InferenceEngine:
    def __init__(self, kb_file):
        self.prolog = Prolog()
        self.prolog.consult(kb_file)

    def query(self, goal):
        try:
            results = list(self.prolog.query(goal))
            return results if results else None
        except Exception as e:
            print(f"Error processing query: {e}")
            return None

if __name__ == "__main__":
    engine = InferenceEngine("knowledge_base.pl")

    # Example: Is John an ancestor of Tom?
    query_str = "ancestor(john, tom)"
    result = engine.query(query_str)

    if result:
        print(f"✅ Success: {query_str} is true")
    else:
        print(f"❌ Failure: {query_str} is false")
