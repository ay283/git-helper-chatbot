# git-helper-chatbot

# Git Helper Chatbot

A Python-based command-line chatbot that guides users through common Git tasks, including resolving merge conflicts, fixing push/pull errors, and undoing commits.

---

## Setup / Installation

**Clone the repository**  
```bash
git clone https://github.com/ay283/git-helper-chatbot.git
cd git-helper-chatbot
```

**Ensure Python 3.x is installed**
Check your Python version:
```bash
python3 --version
```

**Run the chatbot**
```bash
python3 git_helper_chatbot.py
```

## Approach

CLI-based design: Text interface for simplicity and accessibility

Typing effect: Simulates natural conversation using sys.stdout.write and time.sleep

Modular structure: Functions for handling merge conflicts, push/pull errors, undoing commits, and other issues

Interactive prompts: Guides users step-by-step and validates input to handle errors

Loops: Allow retries for invalid inputs and ensure smooth user experience

## Example Usage

## Notes

Designed for beginner and intermediate Git users

Can be extended to handle more Git scenarios or improved with a GUI in the future
