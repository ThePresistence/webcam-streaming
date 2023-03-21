import av
import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    flipped = img[::-1,:,:] if flip else img

    return av.VideoFrame.from_ndarray(flipped, format="bgr24")

# webrtc_ctx = webrtc_streamer(
# 	key="object-detection", 
#     mode=WebRtcMode.SENDRECV,
#     rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}, # 'turn:my-turn-server.mycompany.com:19403 # stun:stun.l.google.com:19302
#     video_frame_callback=video_frame_callback,
#     # media_stream_constraints={"video": True, "audio": False},
#     async_processing=True,
# )

webrtc_streamer(
    key="key", 
    video_processor_factory=VideoProcessor,
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}), 
    async_processing=True,
    video_frame_callback=video_frame_callback

	)