import re

def video_script_to_audio_text(script: str) -> str:
    """
    Converts a timestamped, markdown-formatted video script into clean audio narration text
    suitable for AWS Polly text-to-speech.
    
    Removes:
    - Timestamps and headers like **(0:00-0:15) [MAGNETIC HOOK]**
    - Bold markdown formatting
    - Visual cues like [VISUAL CUE: ...]
    - Any remaining square bracket content
    - Segment markers like **(Segment 1):**
    - Excessive whitespace and newlines
    
    Args:
        script (str): The original video script with timestamps and markdown
        
    Returns:
        str: Clean text suitable for audio narration
    """
    
    # Remove timestamps and headers like **(0:00-0:15) [MAGNETIC HOOK]**
    script = re.sub(r"\*\*\(\d+:\d+-\d+:\d+\)\s*\[[^\]]+\]\*\*", "", script)
    
    # Remove segment markers like **(Segment 1):** or **(Segment 2):**
    script = re.sub(r"\*\*\(Segment \d+\):\*\*", "", script)
    
    # Remove bold markdown formatting
    script = re.sub(r"\*\*(.*?)\*\*", r"\1", script)
    
    # Remove [VISUAL CUE: ...] and any other square bracket content
    script = re.sub(r"\[VISUAL CUE:.*?\]", "", script)
    script = re.sub(r"\[.*?\]", "", script)
    
    # Replace multiple newlines with single newline
    script = re.sub(r"\n{2,}", "\n", script.strip())
    
    # Normalize whitespace (multiple spaces to single space)
    script = re.sub(r"\s{2,}", " ", script)
    
    # Clean up any remaining leading/trailing whitespace on each line
    lines = [line.strip() for line in script.split('\n') if line.strip()]
    
    # Join lines with single space to create flowing text
    return " ".join(lines)

import re
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import timedelta

@dataclass
class ScriptElement:
    """Represents a visual, interactive, or structural element in the script"""
    element_type: str  # 'visual', 'interactive', 'structural', 'engagement'
    content: str
    timing: Optional[str] = None
    description: Optional[str] = None

@dataclass
class ScriptSegment:
    """Represents a complete segment of the video script"""
    title: str
    time_start: str
    time_end: str
    duration_seconds: float
    audio_script: str
    visual_elements: List[ScriptElement]
    interactive_elements: List[ScriptElement]
    engagement_elements: List[ScriptElement]
    structural_elements: List[ScriptElement]
    word_count: int
    estimated_tokens: int

class VideoScriptTokenizer:
    """Advanced tokenizer for educational video scripts with multi-modal element extraction"""
    
    def __init__(self):
        self.segment_patterns = {
            'magnetic_hook': r'\*\*(.*?)\[MAGNETIC HOOK\]\*\*(.*?)(?=\*\*.*?\[|$)',
            'context_foundation': r'\*\*(.*?)\[CONTEXT FOUNDATION\]\*\*(.*?)(?=\*\*.*?\[|$)',
            'core_knowledge_transfer': r'\*\*(.*?)\[CORE KNOWLEDGE TRANSFER\]\*\*(.*?)(?=\*\*.*?\[|$)',
            'practical_mastery': r'\*\*(.*?)\[PRACTICAL MASTERY\]\*\*(.*?)(?=\*\*.*?\[|$)',
            'critical_thinking_development': r'\*\*(.*?)\[CRITICAL THINKING DEVELOPMENT\]\*\*(.*?)(?=\*\*.*?\[|$)',
            'synthesis_transformation': r'\*\*(.*?)\[SYNTHESIS & TRANSFORMATION\]\*\*(.*?)(?=\*\*.*?\[|$)'
        }
        
        # Enhanced element patterns covering all prompt specifications
        self.element_patterns = {
            'visual': {
                'visual_cue': r'\[VISUAL CUE:\s*(.*?)\]',
                'visual_metaphor': r'\[VISUAL METAPHOR:\s*(.*?)\]',
                'visual_transition': r'\[VISUAL TRANSITION:\s*(.*?)\]',
                'color_coding': r'\[COLOR:\s*(.*?)\]',
                'gesture': r'\[GESTURE:\s*(.*?)\]',
                'body_language': r'\[BODY LANGUAGE:\s*(.*?)\]'
            },
            'interactive': {
                'pause_reflection': r'\[PAUSE FOR REFLECTION\]',
                'viewer_challenge': r'\[VIEWER CHALLENGE:\s*(.*?)\]',
                'poll_quiz': r'\[POLL/QUIZ:\s*(.*?)\]',
                'comment_prompt': r'\[COMMENT PROMPT:\s*(.*?)\]',
                'resource_link': r'\[RESOURCE LINK:\s*(.*?)\]'
            },
            'engagement': {
                'pattern_interrupt': r'\[PATTERN INTERRUPT:\s*(.*?)\]',
                'curiosity_gap': r'\[CURIOSITY GAP:\s*(.*?)\]',
                'knowledge_loop': r'\[KNOWLEDGE LOOP:\s*(.*?)\]',
                'yes_ladder': r'\[YES LADDER:\s*(.*?)\]',
                'emotional_anchor': r'\[EMOTIONAL ANCHOR:\s*(.*?)\]',
                'social_proof': r'\[SOCIAL PROOF:\s*(.*?)\]',
                'call_to_action': r'\[CALL TO ACTION:\s*(.*?)\]'
            },
            'structural': {
                'segment_marker': r'\*\*(Segment \d+.*?)\*\*',
                'learning_objective': r'\[LEARNING OBJECTIVE:\s*(.*?)\]',
                'transition_bridge': r'\[TRANSITION:\s*(.*?)\]',
                'confirmation_check': r'\[CHECK:\s*(.*?)\]',
                'key_takeaway': r'\[KEY TAKEAWAY:\s*(.*?)\]'
            }
        }
    
    def parse_time_range(self, time_str: str) -> tuple:
        """Parse time range from format like '(0:00-0:15)' or '(0:15-0:30)'"""
        time_match = re.search(r'\((\d+:\d+)-(\d+:\d+)\)', time_str)
        if time_match:
            start_time = time_match.group(1)
            end_time = time_match.group(2)
            
            # Convert to seconds for duration calculation
            start_seconds = self._time_to_seconds(start_time)
            end_seconds = self._time_to_seconds(end_time)
            duration = end_seconds - start_seconds
            
            return start_time, end_time, duration
        return None, None, 0
    
    def _time_to_seconds(self, time_str: str) -> float:
        """Convert time string 'M:SS' to seconds"""
        parts = time_str.split(':')
        return int(parts[0]) * 60 + int(parts[1])
    
    def extract_elements(self, text: str) -> Dict[str, List[ScriptElement]]:
        """Extract all visual, interactive, engagement, and structural elements"""
        elements = {
            'visual': [],
            'interactive': [],
            'engagement': [],
            'structural': []
        }
        
        for element_type, patterns in self.element_patterns.items():
            for pattern_name, pattern in patterns.items():
                matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
                for match in matches:
                    content = match if isinstance(match, str) else match[0] if match else ""
                    elements[element_type].append(
                        ScriptElement(
                            element_type=element_type,
                            content=content.strip(),
                            description=pattern_name
                        )
                    )
        
        return elements
    
    def clean_audio_script(self, text: str) -> str:
        """Remove all markup elements to get clean audio script"""
        # Remove time stamps
        text = re.sub(r'\*\*\(.*?\)\s*\[.*?\]\*\*', '', text)
        
        # Remove all element markers
        for element_type, patterns in self.element_patterns.items():
            for pattern in patterns.values():
                text = re.sub(pattern, '', text, flags=re.IGNORECASE | re.DOTALL)
        
        # Remove segment markers
        text = re.sub(r'\*\*(Segment \d+.*?)\*\*', '', text)
        
        # Clean up extra whitespace and newlines
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    
    def count_words_and_tokens(self, text: str) -> tuple:
        """Count words and estimate tokens"""
        words = len(text.split())
        # Estimate tokens (roughly 1.35 tokens per word for English)
        tokens = int(words * 1.35)
        return words, tokens
    
    def tokenize_script(self, script: str) -> Dict[str, ScriptSegment]:
        """
        Tokenize the complete video script into structured segments
        
        Returns:
            Dict mapping segment names to ScriptSegment objects
        """
        segments = {}
        
        for segment_name, pattern in self.segment_patterns.items():
            match = re.search(pattern, script, re.IGNORECASE | re.DOTALL)
            
            if match:
                time_portion = match.group(1)
                content_portion = match.group(2)
                
                # Parse timing
                start_time, end_time, duration = self.parse_time_range(time_portion)
                
                # Extract all elements
                elements = self.extract_elements(content_portion)
                
                # Clean audio script
                audio_script = self.clean_audio_script(content_portion)
                
                # Count words and tokens
                word_count, token_count = self.count_words_and_tokens(audio_script)
                
                # Create segment object
                segments[segment_name] = ScriptSegment(
                    title=segment_name.replace('_', ' ').title(),
                    time_start=start_time or "0:00",
                    time_end=end_time or "0:00",
                    duration_seconds=duration,
                    audio_script=audio_script,
                    visual_elements=elements['visual'],
                    interactive_elements=elements['interactive'],
                    engagement_elements=elements['engagement'],
                    structural_elements=elements['structural'],
                    word_count=word_count,
                    estimated_tokens=token_count
                )
        
        return segments
    
    def get_segment_summary(self, segments: Dict[str, ScriptSegment]) -> Dict[str, Any]:
        """Generate summary statistics for the tokenized script"""
        total_duration = sum(seg.duration_seconds for seg in segments.values())
        total_words = sum(seg.word_count for seg in segments.values())
        total_tokens = sum(seg.estimated_tokens for seg in segments.values())
        
        visual_count = sum(len(seg.visual_elements) for seg in segments.values())
        interactive_count = sum(len(seg.interactive_elements) for seg in segments.values())
        engagement_count = sum(len(seg.engagement_elements) for seg in segments.values())
        
        return {
            'total_duration_seconds': total_duration,
            'total_duration_formatted': f"{int(total_duration // 60)}:{int(total_duration % 60):02d}",
            'total_words': total_words,
            'total_tokens': total_tokens,
            'words_per_minute': (total_words / total_duration) * 60 if total_duration > 0 else 0,
            'segment_count': len(segments),
            'visual_elements_count': visual_count,
            'interactive_elements_count': interactive_count,
            'engagement_elements_count': engagement_count,
            'segments': list(segments.keys())
        }
    
    def export_for_manim(self, segments: Dict[str, ScriptSegment]) -> Dict[str, Any]:
        """Export tokenized script in format optimized for Manim animation"""
        manim_data = {
            'scenes': [],
            'global_settings': {
                'total_duration': sum(seg.duration_seconds for seg in segments.values()),
                'video_quality': 'high',
                'frame_rate': 60
            }
        }
        
        for segment_name, segment in segments.items():
            scene_data = {
                'scene_name': segment_name,
                'title': segment.title,
                'duration': segment.duration_seconds,
                'start_time': segment.time_start,
                'end_time': segment.time_end,
                'narration': {
                    'text': segment.audio_script,
                    'word_count': segment.word_count,
                    'estimated_duration': segment.duration_seconds
                },
                'visual_instructions': [
                    {
                        'type': elem.description,
                        'content': elem.content,
                        'timing': elem.timing
                    } for elem in segment.visual_elements
                ],
                'interactive_moments': [
                    {
                        'type': elem.description,
                        'content': elem.content,
                        'action': 'pause' if 'pause' in elem.description.lower() else 'highlight'
                    } for elem in segment.interactive_elements
                ],
                'engagement_triggers': [
                    {
                        'type': elem.description,
                        'content': elem.content
                    } for elem in segment.engagement_elements
                ]
            }
            
            manim_data['scenes'].append(scene_data)
        
        return manim_data
    
    
# Example usage function
def tokenize_video_script(script_text: str) -> Dict[str, ScriptSegment]:
    """
    Main function to tokenize a video script
    
    Args:
        script_text: Raw video script text
        
    Returns:
        Dictionary of tokenized segments
    """
    tokenizer = VideoScriptTokenizer()
    segments = tokenizer.tokenize_script(script_text)
    
    return segments

    
