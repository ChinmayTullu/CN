import random
import time
    
def receive_ack(frame):
    time.sleep(1)
    if random.randint(0,9)<(prob/10):
        print(f"Frame {frame} lost.")
        return False
    else:
        print(f"Frame {frame} received. Sending ACK.")
        return True

window_size=int(input("Enter window size (N): "))
total_frames=int(input("Enter total number of frames: "))
prob=int(input("Enter the probability of frame loss(0-100): "))

random.seed(time.time())
current_frame=0
last_acked_frame=-1

while current_frame<total_frames:
    for i in range(window_size):
        if current_frame+i<total_frames:
            print(f"Sending frame {current_frame+i}")
            time.sleep(1)
            
    for i in range(window_size):
        if current_frame+i<total_frames:
            if receive_ack(current_frame+i):
                last_acked_frame=current_frame+i
            else:
                break
                
    current_frame=last_acked_frame+1

    if current_frame<total_frames and current_frame <=last_acked_frame:
        print(f"Timeout! Retransmitting from frame {current_frame}...\n")

print("All frames sent and acknowledged.")
