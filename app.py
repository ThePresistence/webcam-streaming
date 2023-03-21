# import av
# import cv2
# import numpy as np
# import streamlit as st
# from streamlit_webrtc import WebRtcMode, webrtc_streamer, RTCConfiguration

# def video_frame_callback(frame):
#     img = frame.to_ndarray(format="bgr24")

#     flipped = img[::-1,:,:] if flip else img

#     return av.VideoFrame.from_ndarray(flipped, format="bgr24")

# # webrtc_ctx = webrtc_streamer(
# # 	key="object-detection", 
# #     mode=WebRtcMode.SENDRECV,
# #     rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}, # 'turn:my-turn-server.mycompany.com:19403 # stun:stun.l.google.com:19302
# #     video_frame_callback=video_frame_callback,
# #     # media_stream_constraints={"video": True, "audio": False},
# #     async_processing=True,
# # )

# webrtc_streamer(
#     key="key", 
#     mode=WebRtcMode.SENDRECV,
#     rtc_configuration=RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}), 
#     async_processing=True,
#     video_frame_callback=video_frame_callback

# 	)

from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import av
import cv2


cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

class VideoProcessor:
	def recv(self, frame):
		frm = frame.to_ndarray(format="bgr24")

		faces = cascade.detectMultiScale(cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY), 1.1, 3)

		for x,y,w,h in faces:
			cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 3)

		return av.VideoFrame.from_ndarray(frm, format='bgr24')

webrtc_streamer(key="key", video_processor_factory=VideoProcessor,
				rtc_configuration=RTCConfiguration(
					{"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
					)
	)