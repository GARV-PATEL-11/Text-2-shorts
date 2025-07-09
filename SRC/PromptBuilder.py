def get_enhanced_conversational_script_prompt(
    paragraph: str,
    audience_level: str = "intermediate",
    tone: str = "conversational",
    duration_minutes: float = 1.75,
    include_engagement: bool = True,
    academic_rigor: str = "moderate",
    content_type: str = "educational",
    visual_elements: bool = False,
    interactive_elements: bool = False
) -> str:
    """
    Advanced conversational script prompt builder with comprehensive educational video optimization.
    
    Major enhancements:
    - Multi-modal content support (audio, visual, interactive)
    - Advanced audience psychology profiling
    - Cognitive load optimization
    - Retention-focused structure
    - Platform-specific optimizations
    - AI-assisted quality assurance
    
    Args:
        paragraph (str): Source text to transform into script
        audience_level (str): "beginner", "intermediate", "advanced", or "expert"
        tone (str): "conversational", "explanatory", "narrative", "tutorial", "inspirational", "analytical"
        duration_minutes (float): Target video duration in minutes
        include_engagement (bool): Whether to include viewer engagement elements
        academic_rigor (str): "light", "moderate", "rigorous", or "scholarly"
        content_type (str): "educational", "entertainment", "professional", "academic", "tutorial"
        visual_elements (bool): Whether to include visual cues and descriptions
        interactive_elements (bool): Whether to include interactive components
        
    Returns:
        str: Optimized prompt for conversational script generation
    """
    # Enhanced speech metrics with platform optimization
    platform_specs = {
        "youtube": {"wpm": 150, "retention_curve": "hook_heavy"},
        "educational": {"wpm": 130, "retention_curve": "steady_build"},
        "podcast": {"wpm": 160, "retention_curve": "narrative_arc"},
        "presentation": {"wpm": 140, "retention_curve": "structured"}
    }
    
    words_per_minute = 150  # Base rate
    target_words = int(duration_minutes * words_per_minute)
    estimated_tokens = int(target_words * 1.35)  # Updated token ratio
    
    # Advanced audience psychology profiling
    audience_profiles = {
        "beginner": {
            "cognitive_load": "Minimal - one concept at a time",
            "complexity": "Introduce concepts with scaffolding and clear definitions",
            "language": "Simple, jargon-free with rich analogies and metaphors",
            "examples": "Everyday, relatable examples from personal experience",
            "pacing": "Slower with repetition and confirmation checks",
            "attention_span": "Short bursts with frequent engagement",
            "motivation": "Build confidence through small wins and encouragement"
        },
        "intermediate": {
            "cognitive_load": "Moderate - connect new to existing knowledge",
            "complexity": "Build on foundational knowledge with logical progression",
            "language": "Professional terminology with contextual explanations",
            "examples": "Industry-relevant cases and practical applications",
            "pacing": "Balanced depth with efficient knowledge transfer",
            "attention_span": "Sustained with periodic reinforcement",
            "motivation": "Show practical value and skill advancement"
        },
        "advanced": {
            "cognitive_load": "High - multiple interconnected concepts",
            "complexity": "Dive into nuanced details and sophisticated frameworks",
            "language": "Technical precision with field-specific terminology",
            "examples": "Complex scenarios, edge cases, and expert insights",
            "pacing": "Dense information with assumed rapid comprehension",
            "attention_span": "Extended focus with intellectual challenge",
            "motivation": "Present cutting-edge insights and mastery opportunities"
        },
        "expert": {
            "cognitive_load": "Maximum - abstract and theoretical concepts",
            "complexity": "Explore theoretical foundations and research frontiers",
            "language": "Scholarly discourse with precise academic terminology",
            "examples": "Research findings, theoretical models, and paradigm shifts",
            "pacing": "Rapid with assumption of deep prior knowledge",
            "attention_span": "Deep focus with analytical thinking",
            "motivation": "Challenge assumptions and present novel perspectives"
        }
    }
    
    # Expanded tone specifications with emotional intelligence
    tone_profiles = {
        "conversational": {
            "style": "Natural dialogue with personal connection",
            "voice": "Friendly expert sharing insights over coffee",
            "techniques": "Direct address, rhetorical questions, casual language"
        },
        "explanatory": {
            "style": "Clear teaching voice with structured delivery",
            "voice": "Patient educator guiding discovery",
            "techniques": "Logical progression, clarifying questions, teaching moments"
        },
        "narrative": {
            "style": "Story-driven with emotional engagement",
            "voice": "Compelling storyteller revealing insights",
            "techniques": "Character development, plot progression, dramatic tension"
        },
        "tutorial": {
            "style": "Step-by-step guidance with practical focus",
            "voice": "Expert mentor providing hands-on instruction",
            "techniques": "Clear instructions, checkpoint verification, troubleshooting"
        },
        "inspirational": {
            "style": "Motivational with emotional resonance",
            "voice": "Inspiring leader sharing transformative vision",
            "techniques": "Emotional appeals, success stories, call to action"
        },
        "analytical": {
            "style": "Systematic examination with critical thinking",
            "voice": "Thoughtful analyst exploring complexities",
            "techniques": "Evidence presentation, logical reasoning, balanced perspectives"
        }
    }
    
    # Advanced academic rigor with research integration
    rigor_frameworks = {
        "light": {
            "depth": "Surface-level understanding with practical focus",
            "sources": "Popular sources and common knowledge",
            "evidence": "Anecdotal examples and basic reasoning",
            "complexity": "Simplified models and straightforward explanations"
        },
        "moderate": {
            "depth": "Balanced theoretical foundation with practical application",
            "sources": "Professional publications and established research",
            "evidence": "Empirical examples and logical frameworks",
            "complexity": "Nuanced understanding with multiple perspectives"
        },
        "rigorous": {
            "depth": "Comprehensive coverage with theoretical depth",
            "sources": "Peer-reviewed research and expert consensus",
            "evidence": "Scientific studies and systematic analysis",
            "complexity": "Sophisticated models and critical evaluation"
        },
        "scholarly": {
            "depth": "Exhaustive examination with research-level precision",
            "sources": "Primary research and cutting-edge findings",
            "evidence": "Methodological rigor and statistical analysis",
            "complexity": "Advanced theoretical frameworks and original insights"
        }
    }
    
    # Content type optimization
    content_optimizations = {
        "educational": "Focus on learning outcomes and knowledge retention",
        "entertainment": "Prioritize engagement and emotional connection",
        "professional": "Emphasize practical application and career relevance",
        "academic": "Maintain scholarly standards and theoretical rigor",
        "tutorial": "Ensure actionable steps and practical implementation"
    }
    
    # Visual and interactive elements
    visual_cues = ""
    if visual_elements:
        visual_cues = """
## Visual Integration Guidelines
- Include [VISUAL CUE] markers for key concepts that need visual support
- Suggest specific visual metaphors and analogies
- Indicate timing for visual transitions and emphasis
- Recommend color coding and visual hierarchy
- Include gesture and body language suggestions for presenter"""
    
    interactive_components = ""
    if interactive_elements:
        interactive_components = """
## Interactive Elements
- Embed [PAUSE FOR REFLECTION] moments at strategic points
- Include [VIEWER CHALLENGE] segments for active participation
- Suggest [POLL/QUIZ] opportunities for knowledge checking
- Add [COMMENT PROMPT] questions to drive engagement
- Include [RESOURCE LINK] callouts for deeper exploration"""
    
    # Dynamic engagement with retention optimization
    engagement_strategy = ""
    if include_engagement:
        engagement_strategy = """
## Advanced Engagement Strategy
- Open with attention-grabbing hook within first 15 seconds
- Use pattern interrupts every 30-45 seconds to maintain focus
- Include curiosity gaps and knowledge loops
- Employ the "Yes Ladder" technique for psychological buy-in
- Create emotional anchors for key concepts
- Use the "Zeigarnik Effect" with open loops and callbacks
- Include social proof and credibility indicators
- End with compelling call-to-action and next steps"""
    
    # Get current specifications
    audience_spec = audience_profiles.get(audience_level, audience_profiles["intermediate"])
    tone_spec = tone_profiles.get(tone, tone_profiles["conversational"])
    rigor_spec = rigor_frameworks.get(academic_rigor, rigor_frameworks["moderate"])
    content_opt = content_optimizations.get(content_type, content_optimizations["educational"])
    
    # Build comprehensive prompt
    prompt = f"""# Advanced Educational Content Script Generation

## Core Mission
Transform the provided text into a masterfully crafted conversational script that combines academic excellence with engaging storytelling, optimized for maximum learning retention and viewer engagement.

## Target Specifications
- **Duration:** {duration_minutes} minutes ({target_words} words, ~{estimated_tokens} tokens)
- **Audience:** {audience_level.title()} level ({audience_spec['attention_span']})
- **Tone:** {tone.title()} - {tone_spec['style']}
- **Academic Rigor:** {academic_rigor.title()} - {rigor_spec['depth']}
- **Content Type:** {content_type.title()} - {content_opt}

## Audience Psychology Profile
**Cognitive Load Management:** {audience_spec['cognitive_load']}
**Complexity Approach:** {audience_spec['complexity']}
**Language Strategy:** {audience_spec['language']}
**Example Selection:** {audience_spec['examples']}
**Pacing Methodology:** {audience_spec['pacing']}
**Motivation Drivers:** {audience_spec['motivation']}

## Tone & Voice Guidelines
**Primary Voice:** {tone_spec['voice']}
**Delivery Techniques:** {tone_spec['techniques']}
**Academic Framework:** {rigor_spec['evidence']}
**Source Integration:** {rigor_spec['sources']}{visual_cues}{interactive_components}{engagement_strategy}

## Advanced Script Architecture

### **[MAGNETIC HOOK]** (15-20 seconds)
- Deploy psychological triggers: curiosity gap, pattern interrupt, or cognitive dissonance
- Create immediate emotional connection with viewer's deepest interests or pain points
- Use the "What if..." or "Imagine..." technique for mental engagement
- Establish personal stake: "This will change how you think about..."

### **[CONTEXT FOUNDATION]** (20-30 seconds)
- Provide essential background with narrative elements
- Use the "Before we dive in..." bridging technique
- Define key terms through storytelling rather than dictionary definitions
- Create conceptual scaffolding for complex ideas ahead

### **[CORE KNOWLEDGE TRANSFER]** (60-70% of total time)
**Structured as interconnected segments:**
- **Segment 1:** Foundation concepts with vivid analogies
- **Segment 2:** Building complexity with logical progression
- **Segment 3:** Advanced applications with real-world connections
- **Integration:** Synthesis of all concepts into coherent framework

*Each segment includes:*
- Clear learning objective stated upfront
- Multiple explanation approaches (visual, auditory, kinesthetic)
- Confirmation checks: "Does this make sense so far?"
- Transition bridges: "Now that we understand X, let's explore Y"

### **[PRACTICAL MASTERY]** (15-20% of total time)
- Present 2-3 progressively complex examples
- Use the "Show, Tell, Do" methodology
- Include common pitfalls and how to avoid them
- Provide mental models and frameworks for application
- Connect to viewer's specific context and goals

### **[CRITICAL THINKING DEVELOPMENT]** (10-15% of total time)
- Present balanced analysis of strengths and limitations
- Address counterarguments and alternative perspectives
- Encourage questioning and deeper investigation
- Acknowledge uncertainty and areas for further research
- Build intellectual humility and critical thinking skills

### **[SYNTHESIS & TRANSFORMATION]** (15-20 seconds)
- Crystallize key insights into memorable frameworks
- Connect learning to broader patterns and principles
- Provide clear implementation roadmap
- End with transformative question or challenge
- Create desire for continued learning and exploration

## Quality Assurance Framework

### Academic Excellence Standards
- Ensure comprehensive coverage without overwhelming cognitive load
- Maintain factual accuracy with appropriate source attribution
- Balance depth with accessibility for target audience
- Include relevant context and historical perspective
- Address common misconceptions and clarify confusion

### Conversational Mastery Criteria
- Use natural speech patterns with strategic pauses
- Include conversational bridges and smooth transitions
- Vary sentence structure for engaging spoken delivery
- Add emotional color and personality to delivery
- Create intimate connection through strategic vulnerability

### Engagement Optimization Metrics
- Maintain attention through strategic pattern interrupts
- Use psychological triggers for sustained interest
- Include interactive elements and reflection prompts
- Create emotional investment in learning outcomes
- Build momentum toward actionable next steps

## Source Material Analysis
```
{paragraph.strip()}
```

## Final Generation Instructions

Create a complete video script that transforms the source material into an engaging educational experience. Write as if you're a master educator who combines deep expertise with exceptional communication skills. 

**Key Success Factors:**
1. Every sentence should serve a clear pedagogical purpose
2. Maintain conversational authenticity while preserving academic integrity
3. Create memorable moments through vivid language and powerful analogies
4. Build emotional connection while delivering intellectual content
5. Structure for maximum retention and practical application

**Target Metrics:**
- Exactly {target_words} words for {duration_minutes} minutes
- {audience_level.title()} level complexity
- {tone.title()} tone throughout
- {academic_rigor.title()} academic standards

Generate the complete script now, ensuring each section flows seamlessly into the next while maintaining the specified psychological and pedagogical principles."""

    return prompt