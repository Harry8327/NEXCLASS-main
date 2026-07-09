# NexClass 🎓

**Mark attendance for a whole class from one photo, or verify students by voice — no more calling out names one by one.**

🔗 **Live Demo:** [nex-class-landing-page.vercel.app](https://nex-class-landing-page.vercel.app/)

---

## What it does

I built NexClass to get rid of manual roll calls. It gives teachers two ways to take attendance automatically:

- **Photo-based attendance** — upload one photo of the class, and it picks out every student's face and marks them present.
- **Voice-based attendance** — students can also be checked in one at a time just by speaking, using their voice as ID.

Teachers get a dashboard to manage subjects, check attendance logs, and pull CSV reports. Students get their own dashboard to see how their attendance looks across subjects, in real time.

## Features

- 📸 **Multi-face recognition** — spot every student in one class photo instead of matching faces one at a time
- 🎙️ **Voice verification** — attendance by voice, no camera needed
- 📱 **QR-code enrollment** — students join a course by scanning a code
- 👩‍🏫 **Teacher dashboard** — manage subjects, check logs, download CSV reports
- 🎓 **Student dashboard** — real-time attendance tracking
- 🔐 **Supabase backend** — handles login, real-time sync, and stores attendance records

## Tech Stack

| Layer | Technology |
|---|---|
| App | [Streamlit](https://streamlit.io/) |
| Landing page | Flask |
| Face recognition | [face_recognition](https://github.com/ageitgey/face_recognition), Dlib |
| Voice recognition | [Resemblyzer](https://github.com/resemble-ai/Resemblyzer), Librosa |
| Backend | [Supabase](https://supabase.com/) (PostgreSQL, Auth, Realtime) |
| Language | Python |

## How it works

1. A teacher creates a course and generates a QR code for students to enroll.
2. For photo attendance, the teacher uploads one class photo. NexClass finds all the faces, matches them to enrolled students, and marks them present.
3. For voice attendance, students are checked in one at a time by speaking.
4. Everything syncs to Supabase right away, so both dashboards update instantly.

## Getting Started

```bash
# Clone the repo
git clone https://github.com/Harry8327/NEXCLASS-main.git
cd NEXCLASS-main

# Install dependencies
pip install -r requirements.txt

# Add your Supabase credentials to .streamlit/secrets.toml

# Run the app
streamlit run app.py
```

## Project Structure

```
NEXCLASS-main/
├── .streamlit/       # Streamlit configuration & secrets
├── src/              # Core application logic (recognition, dashboards, etc.)
├── app.py            # App entry point
└── requirements.txt  # Python dependencies
```

## What's next

- [ ] Attendance analytics and trend charts for teachers
- [ ] Support multiple photos per session for better accuracy in bigger classes
- [ ] Mobile-friendly capture flow

## Author

Built by [Harsh Goyal](https://github.com/Harry8327)
