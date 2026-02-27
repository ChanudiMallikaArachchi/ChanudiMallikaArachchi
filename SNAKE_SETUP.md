# GitHub Snake Animation Setup

## Option 1: Use the Live Snake Graph (Easiest - No Setup Required)

The snake animation is already added to your README using this URL:
```
https://ghchart.rshah.org/ChanudiMallikaArachchi
```

This is a live graph that automatically shows your contribution snake. Just make sure you have commits on GitHub!

---

## Option 2: Generate a Custom Snake Animation (Optional - More Customizable)

If you want a custom animated snake that lives in your repo:

### Step 1: Go to GitHub Actions
Navigate to: https://github.com/ChanudiMallikaArachchi/ChanudiMallikaArachchi/actions

### Step 2: Create a New Workflow
1. Click "New workflow"
2. Search for "Python script" or create your own

### Step 3: Use this workflow code:

```yaml
name: Generate Snake

on:
  schedule:
    - cron: "0 */4 * * *"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  generate:
    runs-on: ubuntu-latest
    timeout-minutes: 5

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Generate Snake
        uses: Platane/snk@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          svg_path: output/snake.svg

      - name: Commit and Push
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add -A
          git commit -m "Update snake animation" || exit 0
          git push
```

### Step 4: Run the workflow
1. Go to your workflow
2. Click "Run workflow"

---

## Your Current GitHub Stats URLs

The stats in your README already use your username correctly:
- Stats: `https://github-readme-stats.vercel.app/api?username=ChanudiMallikaArachchi`
- Streak: `https://github-readme-streak-stats.herokuapp.com/?user=ChanudiMallikaArachchi`

These will work automatically once you have commits on GitHub!

---

## What You Need To Do:

1. **Make some commits** to your GitHub account to see the stats and snake animation
2. **Push your first real code** - create a repository with actual code
3. The stats will show "0 contributions" until you have commits on GitHub

The snake graph will appear automatically when you have contributions!
