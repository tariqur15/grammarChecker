from language_tool_python import LanguageTool

class SpellCheckerModule:
    def __init__(self, language='en-US'):
        self.language_tool = LanguageTool(language)

    def correct_grammar(self, text):
        matches = self.language_tool.check(text)

        # Apply suggestions to the text
        corrected_text = self.language_tool.correct(text)

        return corrected_text, matches

# Example usage:
#if __name__ == "__main__":
    # Initialize GrammarCorrector
    #grammar_corrector = SpellCheckerModule()

    # Example text
    #input_text = "i gose home."

    # Correct the grammar
    #corrected_text, mistakes = grammar_corrector.correct_grammar(input_text)

    # Display corrected text and mistakes found
    #print("Original Text:", input_text)
    #print("Corrected Text:", corrected_text)
    #print("Mistakes Found:", len(mistakes))
    #for mistake in mistakes:
        #print("Mistake:", mistake)