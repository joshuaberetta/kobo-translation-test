"""
Quiz translator for Thinkific courses.

Handles translation of quiz questions while preserving:
- Question structure and logic
- Correct answer mappings
- Answer order
- Question difficulty
- Technical accuracy

Critical: Never change which answer is correct!
"""

from typing import Dict, List, Optional
import json


class QuizTranslator:
    """
    Translate quiz content while maintaining correctness.
    
    Integrates with existing translation agent to use Claude
    with special prompts for quiz translation.
    """
    
    QUESTION_TYPES = [
        'multiple_choice',
        'true_false',
        'fill_in_blank',
        'essay',
        'matching',
        'ordering'
    ]
    
    def __init__(self, translation_agent=None):
        """
        Initialize quiz translator.
        
        Args:
            translation_agent: Instance of SRTTranslationAgent for Claude API
        """
        self.translation_agent = translation_agent
    
    # ========================================================================
    # Quiz Translation
    # ========================================================================
    
    def translate_quiz(self, quiz_data: Dict, target_language: str) -> Dict:
        """
        Translate entire quiz while preserving structure.
        
        Args:
            quiz_data: Quiz dictionary with title, questions, etc.
            target_language: Target language code (es, fr, ar)
            
        Returns:
            Translated quiz dictionary
        """
        print(f"\n📝 Translating quiz: {quiz_data.get('title', 'Untitled')}...")
        
        translated_quiz = {
            'id': quiz_data.get('id'),
            'title': self._translate_text(
                quiz_data.get('title', ''), 
                target_language,
                context='quiz_title'
            ),
            'description': self._translate_text(
                quiz_data.get('description', ''),
                target_language,
                context='quiz_description'
            ),
            'questions': []
        }
        
        # Translate each question
        for idx, question in enumerate(quiz_data.get('questions', []), 1):
            print(f"  Translating question {idx}/{len(quiz_data.get('questions', []))}...")
            translated_q = self.translate_question(question, target_language)
            translated_quiz['questions'].append(translated_q)
        
        print(f"  ✅ Quiz translation complete!\n")
        
        return translated_quiz
    
    def translate_question(self, question: Dict, target_language: str) -> Dict:
        """
        Translate a single question with all its components.
        
        Args:
            question: Question dictionary
            target_language: Target language code
            
        Returns:
            Translated question dictionary
        """
        question_type = question.get('question_type', 'multiple_choice')
        
        # Route to appropriate handler
        handlers = {
            'multiple_choice': self._translate_multiple_choice,
            'true_false': self._translate_true_false,
            'fill_in_blank': self._translate_fill_in_blank,
            'essay': self._translate_essay,
            'matching': self._translate_matching,
            'ordering': self._translate_ordering
        }
        
        handler = handlers.get(question_type, self._translate_generic)
        return handler(question, target_language)
    
    # ========================================================================
    # Question Type Handlers
    # ========================================================================
    
    def _translate_multiple_choice(
        self, 
        question: Dict, 
        target_language: str
    ) -> Dict:
        """
        Translate multiple choice question.
        
        CRITICAL: Preserve which answer is correct by maintaining IDs.
        """
        # Build special prompt for quiz translation
        answers_text = "\n".join([
            f"  {i+1}. {answer.get('text', '')}" 
            for i, answer in enumerate(question.get('answers', []))
        ])
        
        correct_indices = [
            i+1 for i, ans in enumerate(question.get('answers', [])) 
            if ans.get('is_correct', False)
        ]
        
        prompt = f"""Translate this quiz question to {target_language}.

CRITICAL REQUIREMENTS:
- Maintain technical accuracy
- Do NOT change which answer is correct
- Preserve question difficulty level
- Keep answer order the same
- Use terminology from KoboToolbox UI translations

Question: {question.get('text', '')}

Answers:
{answers_text}

Correct answer(s): #{correct_indices}

IMPORTANT: Translate the text but keep the same answer as correct!
"""
        
        # Translate question text
        translated_text = self._translate_with_prompt(prompt, target_language)
        
        # Parse response and build translated question
        # For now, translate each component separately for clarity
        translated_question = {
            'id': question.get('id'),
            'question_type': 'multiple_choice',
            'text': self._translate_text(
                question.get('text', ''),
                target_language,
                context='quiz_question'
            ),
            'answers': []
        }
        
        # Translate each answer while preserving correctness
        for answer in question.get('answers', []):
            translated_answer = {
                'id': answer.get('id'),  # PRESERVE ID
                'text': self._translate_text(
                    answer.get('text', ''),
                    target_language,
                    context='quiz_answer'
                ),
                'is_correct': answer.get('is_correct', False),  # PRESERVE CORRECTNESS
                'position': answer.get('position')
            }
            translated_question['answers'].append(translated_answer)
        
        # Translate explanation/feedback if present
        if question.get('explanation'):
            translated_question['explanation'] = self._translate_text(
                question['explanation'],
                target_language,
                context='quiz_explanation'
            )
        
        return translated_question
    
    def _translate_true_false(self, question: Dict, target_language: str) -> Dict:
        """Translate True/False question."""
        return {
            'id': question.get('id'),
            'question_type': 'true_false',
            'text': self._translate_text(
                question.get('text', ''),
                target_language,
                context='quiz_question'
            ),
            'correct_answer': question.get('correct_answer'),  # Keep as True/False
            'explanation': self._translate_text(
                question.get('explanation', ''),
                target_language,
                context='quiz_explanation'
            ) if question.get('explanation') else None
        }
    
    def _translate_fill_in_blank(self, question: Dict, target_language: str) -> Dict:
        """
        Translate fill-in-the-blank question.
        
        Note: Blank position may need adjustment based on language grammar.
        """
        return {
            'id': question.get('id'),
            'question_type': 'fill_in_blank',
            'text': self._translate_text(
                question.get('text', ''),
                target_language,
                context='quiz_question'
            ),
            'acceptable_answers': [
                self._translate_text(ans, target_language, context='quiz_answer')
                for ans in question.get('acceptable_answers', [])
            ],
            'explanation': self._translate_text(
                question.get('explanation', ''),
                target_language,
                context='quiz_explanation'
            ) if question.get('explanation') else None
        }
    
    def _translate_essay(self, question: Dict, target_language: str) -> Dict:
        """Translate essay question (just the prompt)."""
        return {
            'id': question.get('id'),
            'question_type': 'essay',
            'text': self._translate_text(
                question.get('text', ''),
                target_language,
                context='quiz_question'
            ),
            'guidelines': self._translate_text(
                question.get('guidelines', ''),
                target_language,
                context='quiz_guidelines'
            ) if question.get('guidelines') else None
        }
    
    def _translate_matching(self, question: Dict, target_language: str) -> Dict:
        """Translate matching question."""
        return {
            'id': question.get('id'),
            'question_type': 'matching',
            'text': self._translate_text(
                question.get('text', ''),
                target_language,
                context='quiz_question'
            ),
            'pairs': [
                {
                    'left': self._translate_text(
                        pair.get('left', ''),
                        target_language,
                        context='quiz_answer'
                    ),
                    'right': self._translate_text(
                        pair.get('right', ''),
                        target_language,
                        context='quiz_answer'
                    ),
                    'id': pair.get('id')  # Preserve pairing
                }
                for pair in question.get('pairs', [])
            ]
        }
    
    def _translate_ordering(self, question: Dict, target_language: str) -> Dict:
        """Translate ordering/sequencing question."""
        return {
            'id': question.get('id'),
            'question_type': 'ordering',
            'text': self._translate_text(
                question.get('text', ''),
                target_language,
                context='quiz_question'
            ),
            'items': [
                {
                    'text': self._translate_text(
                        item.get('text', ''),
                        target_language,
                        context='quiz_answer'
                    ),
                    'correct_position': item.get('correct_position'),  # PRESERVE
                    'id': item.get('id')
                }
                for item in question.get('items', [])
            ]
        }
    
    def _translate_generic(self, question: Dict, target_language: str) -> Dict:
        """Fallback for unknown question types."""
        print(f"  ⚠️  Unknown question type: {question.get('question_type')}")
        return {
            **question,
            'text': self._translate_text(
                question.get('text', ''),
                target_language,
                context='quiz_question'
            ),
            '_warning': 'Translated generically - review recommended'
        }
    
    # ========================================================================
    # Translation Helpers
    # ========================================================================
    
    def _translate_text(
        self, 
        text: str, 
        target_language: str,
        context: str = 'general'
    ) -> str:
        """
        Translate text using the translation agent.
        
        Args:
            text: Text to translate
            target_language: Target language code
            context: Context hint (quiz_question, quiz_answer, etc.)
            
        Returns:
            Translated text
        """
        if not text or not text.strip():
            return text
        
        if self.translation_agent:
            # Use the existing translation agent with special quiz context
            # This would integrate with your SRTTranslationAgent
            # For POC, return a placeholder
            return f"[{target_language.upper()}] {text}"
        else:
            # Placeholder for when no agent provided
            return f"[{target_language.upper()}] {text}"
    
    def _translate_with_prompt(self, prompt: str, target_language: str) -> str:
        """
        Translate using a custom prompt.
        
        For complex questions that need special handling.
        """
        if self.translation_agent:
            # This would call Claude with the custom prompt
            # Integration point for your existing system
            pass
        
        return ""
    
    # ========================================================================
    # Validation
    # ========================================================================
    
    def validate_quiz_translation(
        self, 
        original: Dict, 
        translated: Dict
    ) -> Dict:
        """
        Validate that translation preserved quiz integrity.
        
        Checks:
        - Same number of questions
        - Same number of answers per question
        - Correct answers unchanged
        - IDs preserved
        
        Args:
            original: Original quiz data
            translated: Translated quiz data
            
        Returns:
            Validation result dictionary
        """
        issues = []
        
        # Check question count
        orig_q_count = len(original.get('questions', []))
        trans_q_count = len(translated.get('questions', []))
        
        if orig_q_count != trans_q_count:
            issues.append(f"Question count mismatch: {orig_q_count} vs {trans_q_count}")
        
        # Check each question
        for idx, (orig_q, trans_q) in enumerate(
            zip(original.get('questions', []), translated.get('questions', []))
        ):
            # Check IDs preserved
            if orig_q.get('id') != trans_q.get('id'):
                issues.append(f"Question {idx+1}: ID mismatch")
            
            # Check answer count for multiple choice
            if orig_q.get('question_type') == 'multiple_choice':
                orig_ans_count = len(orig_q.get('answers', []))
                trans_ans_count = len(trans_q.get('answers', []))
                
                if orig_ans_count != trans_ans_count:
                    issues.append(
                        f"Question {idx+1}: Answer count mismatch "
                        f"({orig_ans_count} vs {trans_ans_count})"
                    )
                
                # Check correct answer preserved
                for orig_ans, trans_ans in zip(
                    orig_q.get('answers', []),
                    trans_q.get('answers', [])
                ):
                    if orig_ans.get('is_correct') != trans_ans.get('is_correct'):
                        issues.append(
                            f"Question {idx+1}: Correct answer changed! "
                            f"This is a CRITICAL error."
                        )
        
        return {
            'valid': len(issues) == 0,
            'issues': issues,
            'total_questions': orig_q_count,
            'checked': min(orig_q_count, trans_q_count)
        }


if __name__ == "__main__":
    """Test quiz translator with sample data."""
    
    print("🧪 Testing Quiz Translator...\n")
    
    translator = QuizTranslator()
    
    # Sample quiz data
    sample_quiz = {
        'id': 123,
        'title': 'KoboToolbox Basics Quiz',
        'description': 'Test your knowledge of KoboToolbox fundamentals',
        'questions': [
            {
                'id': 1,
                'question_type': 'multiple_choice',
                'text': 'What is KoboToolbox primarily used for?',
                'answers': [
                    {'id': 'a', 'text': 'Data collection', 'is_correct': True},
                    {'id': 'b', 'text': 'Video editing', 'is_correct': False},
                    {'id': 'c', 'text': 'Photo storage', 'is_correct': False}
                ],
                'explanation': 'KoboToolbox is a data collection and management platform.'
            },
            {
                'id': 2,
                'question_type': 'true_false',
                'text': 'KoboToolbox can be used offline.',
                'correct_answer': True,
                'explanation': 'Yes, KoboCollect works offline and syncs when online.'
            }
        ]
    }
    
    # Translate quiz
    translated = translator.translate_quiz(sample_quiz, 'es')
    
    print("Original quiz:")
    print(f"  Title: {sample_quiz['title']}")
    print(f"  Questions: {len(sample_quiz['questions'])}")
    
    print("\nTranslated quiz:")
    print(f"  Title: {translated['title']}")
    print(f"  Questions: {len(translated['questions'])}")
    
    # Validate translation
    validation = translator.validate_quiz_translation(sample_quiz, translated)
    
    print(f"\nValidation:")
    print(f"  Valid: {validation['valid']}")
    print(f"  Checked: {validation['checked']} questions")
    if validation['issues']:
        print(f"  Issues found:")
        for issue in validation['issues']:
            print(f"    - {issue}")
    else:
        print(f"  ✅ No issues found!")
