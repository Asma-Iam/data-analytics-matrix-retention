# Instructions

Covid-19 has had a significant impact on businesses.

As a data analyst, you will study the impact of Covid-19 on the retention of Greenweez users.

## 📁 Setup

To make challenge completion simpler, we have added terminal instructions to challenges that have test suites.

If you haven't already, **copy the terminal instructions at the top of this page and run them in your terminal**.

This will:

- Download a repository containing all of the files for this challenge from github
- Create and navigate to a directory (folder) for this challenge in your terminal
- Set up a new github repository
- Open the challenge in vs code
- Run the test suite for this challenge

Run the following command in the terminal to check you are in the right directory:

```bash
pwd
```

Your result should look like this:

```bash
~/code/<user.github_nickname>/{{ local_path_to("06-Python/04-Python-For-Analysis/03-Matrix-Retention") }}/
```

❌ If it doesn't, consult a TA!

✅ If it does, then you are ready to take on this challenge!

## Jupyter Notebooks

**📍 In your terminal**, run this command to start Jupyter:

```bash
jupyter notebook
```

This will:

1. Start a Jupyter server in your terminal
2. Open your web browser automatically
3. Show a file browser with your challenge files

**👉 Click on the `.ipynb` file to open your challenge notebook.**

## 💻 Working with Multiple Terminal Tabs

**Important:** When you run `jupyter notebook`, it will start a server that keeps running in your terminal. This means you won't be able to run other commands (like git commands) in that same terminal tab.

### Here's what to do:

1. **Open a new terminal tab** (usually `Cmd + T` on Mac or `Ctrl + Shift + T` on Windows/Linux)
2. Use this new tab for running git commands (`git add`, `git commit`, etc.)
3. Keep the original tab running Jupyter Notebook - don't close it while you're working!

### When you're finished with the challenge:

1. **Save your notebook** (File → Save in Jupyter, or `Cmd/Ctrl + S`)
2. Go back to the terminal tab where Jupyter is running
3. Press `Ctrl + C` to stop the Jupyter server
4. You'll see a message asking: `Shutdown this notebook server (y/[n])?`
5. Type `y` and press Enter to confirm

Now you can use that terminal tab for other commands again! ✅

## 🧪 Understanding the Automated Tests

This challenge includes automated tests to validate your work. Here's what you need to know:

### ⚠️ First Run: Tests Will Fail

**Don't worry!** When you first run the challenge setup, all tests will fail. This is expected - you haven't written any code yet.

Once you complete the exercises in the notebook and run tests again, they should pass.

### What Are Test Parameters?

Tests check specific **variables** in your code to ensure you've completed the required steps. For example, a test might check:

- That a variable called `result` exists and contains a value
- That `word_count` is an integer with the correct number
- That your function returns the expected output

**Important:** Follow the variable names specified in the instructions. If the instructions say "store your result in `greeting`", the test will look for a variable called exactly `greeting`.

### Reading Test Error Messages

When a test fails, you'll see an error message. Here's how to interpret it:

```python
AssertionError: Expected word_count to equal 5, got 3
```

#### What this tells you

- **What was checked:** `word_count` value
- **What was expected:** 5
- **What you have:** 3
- **How to fix:** Check how you're counting words in your string

### Common Test Patterns

- **Value checks:** `AssertionError: Expected 42, got 40` → Review your calculation
- **Type checks:** `AssertionError: Expected list, got str` → Check the data type you're returning
- **Existence checks:** `AttributeError: 'ChallengeResult' object has no attribute 'greeting'` → You didn't create or didn't name a required variable
- **Length checks:** `AssertionError: Expected list of length 5, got 3` → Check what you're including in your list

### Tips for Success

🔍 **Follow variable names exactly** as specified in the instructions
🔍 **Read error messages carefully** - they tell you what's wrong
🔍 **Check your variable names** - `Greeting` ≠ `greeting`
👍 **You can add extra code** for exploration - tests only check for what's required
♻️ **Run tests frequently** to catch issues early

## 🚀 Test Your Solution

After completing the exercises in your notebook:

**📍 In your terminal** (use your second terminal tab - keep Jupyter running in the first), run:

```bash
make
```

This will run all tests and show you which parts are complete and which need more work.

💡 **Tip:** Run `make` frequently as you work through the notebook to catch issues early!
