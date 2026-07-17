# 🏋️‍♂️ Flexify — AI Real-Time GYM Coach

**🔗 Live app: [flexify.streamlit.app](https://flexify.streamlit.app/)**

Flexify is a real-time AI fitness coach built with Streamlit, MediaPipe pose detection, and an LLM-powered voice pipeline. It watches your workout through your webcam, counts reps, tracks form (joint angles, alignment, depth), and gives you spoken feedback as you train — like having a coach standing next to you.

## ✨ Features

- **Real-time pose tracking** — uses MediaPipe's Pose Landmarker to track 33 body landmarks live from your webcam feed via WebRTC.
- **Automatic rep & set counting** — dedicated detectors per exercise calculate joint angles and count reps based on movement thresholds.
- **Form feedback overlays** — live on-screen cues (depth, alignment, extension, balance) drawn directly on the video feed.
- **AI voice coaching** — an LLM (via Groq) generates contextual coaching feedback, converted to speech and played back during your session.
- **Workout planning** — pick an exercise, set your target sets/reps, and let Flexify auto-stop your session once you've completed your plan.
- **Workout history** — past sessions are saved per user and viewable as an aggregated history table.
- **Simple username-based login** — no passwords, just a unique name to track your own progress.

## 🏃 Supported Exercises

Squats · Push-ups · Bicep Curls (Dumbbell) · Shoulder Press · Lunges · Lateral Raises · Plank · Jumping Jacks · Sit-ups · Crunches · Deadlifts · Tricep Dips · Mountain Climbers · High Knees · Burpees · Glute Bridges · Bent-over Rows (Dumbbell) · Overhead Triceps Extension · Side Lunges · Wall Sit

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI / App framework | [Streamlit](https://streamlit.io/) |
| Live video | [streamlit-webrtc](https://github.com/whitphx/streamlit-webrtc) |
| Pose detection | [MediaPipe Tasks — Pose Landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker) |
| Voice coaching (LLM) | [Groq API](https://groq.com/) |
| Persistence | SQLite |
| Language | Python 3.12 |

## 📁 Project Structure

```
Flexify/
├── main.py                        # App entry point
├── core/
│   └── base_exercise.py           # Shared angle/point calculation logic
├── detectors/                     # One rep-counting detector per exercise
│   ├── squat.py
│   ├── pushup.py
│   ├── biceps_curl.py
│   ├── shoulder_press.py
│   ├── lunges.py
│   └── ...
├── services/
│   ├── auth/                      # Username login wall
│   ├── coaching/                  # LLM + TTS voice pipeline
│   ├── config/                    # Exercise options, pose connections
│   ├── persistence/                # SQLite user/exercise repository
│   ├── state/                     # Session state defaults
│   ├── tracking/                  # Live metrics sync between video + UI
│   ├── ui/                        # CSS / font / style injection
│   └── vision/                    # WebRTC video processor
├── ml_models/                     # MediaPipe .task model file(s)
├── static/                        # CSS and font assets
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python **3.12** (MediaPipe does not yet ship wheels for 3.13 — see note below)
- A [Groq API key](https://console.groq.com/) for voice coaching (optional — the app runs fine without it, just without voice feedback)
- A webcam

### 1. Clone the repository

```bash
git clone https://github.com/AyanJaved/Flexify.git
cd Flexify
```

### 2. Create and activate a virtual environment

Using `uv` (recommended):

```bash
uv python install 3.12
uv venv --python 3.12
# Windows
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

Or with plain `venv`:

```bash
python3.12 -m venv .venv
# Windows
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
# or: pip install -r requirements.txt
```

> **Note:** MediaPipe wheels are currently only published for Python 3.9–3.12. If you're on 3.13, create your virtual environment with 3.12 instead (see step 2).

### 4. Download the pose landmarker model

Flexify uses MediaPipe's lite Pose Landmarker model for real-time performance. Download it into `ml_models/`:

```bash
mkdir -p ml_models
curl -L -o ml_models/pose_landmarker_lite.task https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/1/pose_landmarker_lite.task
```

### 5. Set your Groq API key (optional, for voice coaching)

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_key_here
```

Or add it to `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your_key_here"
```

### 6. Run the app

```bash
streamlit run main.py
```

Open the local URL Streamlit prints (usually `http://localhost:8501`), enter a username, set up your workout plan in the sidebar, and click **Start Workout**.

## 🌐 Camera Connectivity Note

Flexify uses WebRTC to stream your webcam into the browser tab. On some networks (strict NAT, VPNs, corporate firewalls), a STUN-only connection can fail to establish. The app is configured with a public STUN server and a TURN fallback for broader compatibility — for production use, consider swapping in a dedicated TURN provider (e.g. Twilio, Xirsys, or a self-hosted coturn server).

## 🗺️ Roadmap Ideas

- [ ] Support for barbell/equipment-based exercises with occlusion handling
- [ ] Per-exercise difficulty/calibration settings
- [ ] Exportable workout history (CSV/PDF)
- [ ] Multi-camera-angle support for exercises like Deadlifts

## 🤝 Contributing

Issues and pull requests are welcome. If you're adding a new exercise detector, follow the pattern in `detectors/squat.py` and extend `core/base_exercise.py`'s shared `calculate_angle` / `get_point` helpers.

## 📄 License

This project is licensed under the [MIT License](LICENSE).