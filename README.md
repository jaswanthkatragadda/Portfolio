# Portfolio Site

A dark, modern portfolio site. Three files, no build step, no dependencies.

## Open it in VS Code

1. Unzip this folder and open it in VS Code (`File > Open Folder...`).
2. Install the **Live Server** extension (search "Live Server" by Ritwick Dey in the Extensions panel).
3. Right-click `index.html` → **Open with Live Server**. It'll open in your browser and auto-refresh as you edit.

## What to edit# Jaswanth Portfolio

A clean, responsive portfolio website built with HTML, CSS, and JavaScript.

## Live Demo

- Frontend: https://your-netlify-url.netlify.app
- Backend API: https://portfolio-t20f.onrender.com

## Features

- Responsive one-page portfolio layout
- Dark and light theme toggle
- Contact form for visitors to send messages
- Project showcase section
- Mobile-friendly navigation
- Deployed frontend and backend setup

## Tech Stack

- HTML
- CSS
- JavaScript
- Python
- Flask
- SQLite
- Render
- Netlify

## Project Structure

```text
portfolio claude 2/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── script.js
├── backend/
│   └── app.py
├── requirements.txt
├── README.md
└── messages.db
```

## Local Development

1. Open the project folder in VS Code.
2. Start the backend:

```bash
cd backend
python app.py
```

3. Open the frontend in a browser or use Live Server.

## Environment Variables

For the backend to send emails, set these environment variables:

```bash
EMAIL_USERNAME=your-email@gmail.com
EMAIL_PASSWORD=your-gmail-app-password
RECEIVER_EMAIL=your-email@gmail.com
```

Use a Gmail App Password for `EMAIL_PASSWORD`.

## Contact Form

Visitors can submit:

- Name
- Email
- Message

The message is stored in SQLite and emailed to the configured receiver.

## Deployment

This project is deployed using:

- Netlify for the frontend
- Render for the backend

## License

This project is for personal portfolio use.

## Author

Jaswanth Katragadda

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
