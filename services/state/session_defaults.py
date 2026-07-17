import streamlit as st

def initial_session_defaults():
    defaults = {
        "reps": 0,
        "target_sets": 0,
        "reps_per_set": 0,
        "sets_completed": 0,
        "current_set_reps": 0,
        "workout_complete": False,
        "last_notified_sets_completed": 0,
        "last_notified_workout_complete": False,
        "last_saved_sets_completed": 0,
        "set_cycle_started_at": 0.0,
        "last_exercise_type": "Squats",

        # workout plan (set before starting)
        "workout_started": False,
        "plan_exercise": "Squats",
        "plan_sets": 3,
        "plan_reps": 10,

        # common angles
        "knee_angle": 0,
        "back_angle": 0,
        "elbow_angle": 0,
        "front_knee_angle": 0,
        "back_knee_angle": 0,
        "torso_angle": 0,
        "shoulder_angle": 0,
        "hip_angle": 0,
        "arm_angle": 0,
        "hold_time": 0,

        # Status fields
        "depth_status": "N/A",
        "body_alignment": "N/A",
        "hip_status": "N/A",
        "shoulder_status": "N/A",
        "swing_status": "N/A",
        "extension_status": "N/A",
        "back_arch_status": "N/A",
        "balance_status": "N/A",
        "curl_range_status": "N/A",
        "raise_height_status": "N/A",
        "leg_spread_status": "N/A",
        "sync_status": "N/A",
        "range_status": "N/A",
        "neck_alignment": "N/A",
        "curl_status": "N/A",
        "shoulder_alignment": "N/A",
        "pace_status": "N/A",
        "jump_status": "N/A",
        "back_alignment": "N/A",
        "lift_status": "N/A",
        "hip_hinge_status": "N/A",
        "form_status": "N/A",
        "hip_alignment": "N/A",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value