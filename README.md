  📖 Madlib Generator

A Python program that reads a story template from a text file and lets you fill in the blanks to create a funny, personalized story!

   📋 About

Mad Libs is a classic word game where blanks in a story are filled in without knowing the context — leading to hilarious results. This project reads a story from `story1.txt`, detects all the blanks using regex, prompts you for words, and then prints the completed story.

   ⚙️ How It Works

- The story template is stored in `story1.txt` with placeholders like `{noun}`, `{verb}`, `{adjective}`, etc.
- The program reads the file and extracts all placeholders using `re.findall()`
- You're prompted to fill in each blank one by one
- The final story is assembled using Python's `.format()` and displayed

   🚀 How to Run

```bash
python madlib.py
```

Make sure `story1.txt` is in the same folder.

  Sample Interaction:  
```
Do you want to:
1. Play
2. Quit
Press 1/2: 1

Enter a noun: rocket
Enter a verb: exploded
...
(your hilarious story appears here)
```

   🛠️ Built With

- Python 3
- `re` module (regex)
- `os`, `time` modules
- File I/O

   📁 File Structure

```
Madlib-Generator/
├── madlib.py
└── story1.txt
```

   💡 Concepts Used

- Regular expressions (`re.findall`)
- File reading
- Dictionary and string formatting
- Loops and user input

---
 Part of my Python beginner projects series 🐍 
