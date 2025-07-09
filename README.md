#  Text2Shorts: Automated Educational Video Script Generator with Audio Narration

## 📘 Overview

**Text2Shorts** is a modular Python framework that transforms long-form textual content into **scripted, voice-narrated short-form educational videos**. It is designed to:

* Convert complex paragraphs into engaging, time-bound, conversational scripts.
* Optimize tone, academic rigor, and audience targeting.
* Clean, segment, and narrate scripts using Amazon Polly.
* Prepare outputs for downstream animation workflows (e.g., Manim).

---

## 🗂️ Project Structure

```bash
./
├── SRC/
│   ├── AmazonPollyTTS.py        # Polly TTS wrapper for voice generation
│   ├── PromptBuilder.py         # Conversational script prompt generator
│   └── ScriptCleaner.py         # Script tokenizer, cleaner, and analyzer
├── AudioOutput.mp3              # Sample MP3 output of synthesized audio
├── Text2ShortsNotebook.ipynb    # Main notebook to run the pipeline
├── README.md                    # This file
├── LICENSE                      # Project license
└── .gitignore                   # Ignore rules for Python environment
```

---

## 🧰 Features

### 🔧 1. PromptBuilder

* Generates highly customized prompts for AI models to convert raw paragraphs into well-structured video scripts.
* Incorporates:

  * Audience level (e.g., beginner, expert)
  * Tone (e.g., explanatory, inspirational)
  * Academic rigor (light to scholarly)
  * Duration targeting
  * Visual and interactive cues
  * Advanced engagement strategies

📁 Located in: `SRC/PromptBuilder.py`

---

### 🧼 2. ScriptCleaner

* Cleans and tokenizes the video script output using segment labels like:

  * **\[MAGNETIC HOOK]**
  * **\[CONTEXT FOUNDATION]**
  * **\[CORE KNOWLEDGE TRANSFER]**
* Extracts:

  * Visual cues, structural transitions, viewer challenges
  * Audio narration script (cleaned of visual markup)
* Provides segment summaries and exports to animation-friendly format.

📁 Located in: `SRC/ScriptCleaner.py`

---

### 🗣️ 3. AmazonPollyTTS

* Synthesizes voice-over audio using AWS Polly.
* Generates and saves `.mp3` files from input text.
* Supports voice selection (e.g., Joanna, Matthew).

📁 Located in: `SRC/AmazonPollyTTS.py`

---

## ⚙️ Usage

### 🧪 Run the Jupyter Notebook

```bash
jupyter notebook Text2ShortsNotebook.ipynb
```

### 🧭 Pipeline Steps

1. **Provide raw paragraph input**
2. **Generate prompt using `PromptBuilder`**
3. **Feed the prompt into a language model (e.g., OpenAI, Gemini)**
4. **Tokenize and segment the output using `ScriptCleaner`**
5. **Clean audio narration text**
6. **Use `AmazonPollyTTS` to generate narration**
7. *(Optional)* Export for video rendering (e.g., Manim integration)

---

## 🧑‍💻 Example

```python
from SRC.PromptBuilder import get_enhanced_conversational_script_prompt
from SRC.ScriptCleaner import tokenize_video_script
from SRC.AmazonPollyTTS import polly_speak_text

# Step 1: Generate script prompt
prompt = get_enhanced_conversational_script_prompt(paragraph="What is the Black-Scholes model?")

# Step 2: Send prompt to LLM (e.g., OpenAI/Gemini) and get script

# Step 3: Tokenize and clean
segments = tokenize_video_script(script_output)
clean_audio_text = segments['magnetic_hook'].audio_script

# Step 4: Narrate the script
polly_speak_text(clean_audio_text)
```

---

## 🎯 Target Applications

* Short-form educational videos
* Animated explainers and science communication
* Voice-over driven motion graphics
* Learning content generation (YouTube, MOOCs, Reels)

---

## 🧩 Dependencies

Install dependencies using:

```bash
pip install -r requirements.txt
```

Sample `requirements.txt`:

```
boto3
pydub
notebook
```

⚠️ AWS credentials are required for Polly access.

---

## 📌 Notes

* This repository focuses on **educational content** and **learning retention**.
* The final animation/rendering pipeline is under active development.
* Suitable for integration with animation libraries like **Manim**, **D-ID**, or **RunwayML**.

---

## 🤝 Contributing

Pull requests are welcome! Please ensure:

* Code is modular and well-commented.
* Features are tested in the notebook before submission.
* Follow [PEP8](https://peps.python.org/pep-0008/) conventions.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## ⭐ Support

If you find this project useful or inspiring, please consider giving it a **⭐ star** on [GitHub](https://github.com/GARV-PATEL-11/Text-2-shorts) — it helps others discover the project and motivates continued development.

---

