# Portfolio Site

A dark, modern portfolio site. Three files, no build step, no dependencies.

## Open it in VS Code

1. Unzip this folder and open it in VS Code (`File > Open Folder...`).
2. Install the **Live Server** extension (search "Live Server" by Ritwick Dey in the Extensions panel).
3. Right-click `index.html` → **Open with Live Server**. It'll open in your browser and auto-refresh as you edit.

## What to edit

- **`index.html`** — all your content lives here:
  - Hero section — your name, tagline, and short intro
  - `#about` — a longer bio paragraph and your focus areas
  - `#projects` — one `<article class="project-card">` block per project. Copy/paste the block to add more. Replace the description, tags, and the two `href="#"` links (demo + source).
  - `#contact` — swap `your-username` in the GitHub and LinkedIn links for your real profile URLs.
- **`css/style.css`** — colors and layout. The palette variables are at the top (`:root`) if you want to tweak the accent colors.
- **`js/script.js`** — handles the mobile menu toggle. You shouldn't need to touch this unless you're adding features.

## Deploying it

Once you're happy with it, the easiest free hosting options are:
- **GitHub Pages** — push this folder to a repo, enable Pages in repo settings.
- **Netlify** or **Vercel** — drag-and-drop the folder in their dashboard.

No build step is needed for either.
