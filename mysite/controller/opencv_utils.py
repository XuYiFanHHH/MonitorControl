import cv2 as cv

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.url = "rtsp://admin:admin@59.66.68.38:554/cam/realmonitor?channel=1&subtype=0"
        self.video = cv.VideoCapture(self.url)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        _, image = self.video.read()
        
        # image = Image.fromarray(image)
        # img = self.yolo.detect_image(image)
        # img = np.array(img)

        ret, jpeg = cv.imencode('.jpg', image)
        return jpeg.tobytes()

    def get_array_frame(self):
        _, image = self.video.read()
        return image


def video_demo():  
    #打开0号摄像头，捕捉该摄像头实时信息  
    #参数0代表摄像头的编号  
    #有多个摄像头的情况下，可用编号打开摄像头  
    #若是加载视频，则将参数改为视频路径，cv.VideoCapture加载视频是没有声音的，OpenCV只对视频的每一帧进行分析  
    capture=cv.VideoCapture(0)  
    while(True):  
        #获取视频的返回值 ref 和视频中的每一帧 frame  
        ref,frame=capture.read()  
          
        #加入该段代码将使拍出来的画面呈现镜像效果  
        #第二个参数为视频是否上下颠倒 0为上下颠倒 1为不进行上下颠倒  
        frame= cv.flip(frame,1)  
          
        #将每一帧在窗口中显示出来  
        cv.imshow("video",frame)  
          
        #设置视频刷新频率，单位为毫秒  
        #返回值为键盘按键的值  
        c=cv.waitKey(5)  
          
        #27为 Esc 按键的返回值  
        if c==27:  
            break

def capture_pic():
    capture = cv.VideoCapture(0)
    _, frame = capture.read()
    cv.destroyAllWindows()
    return frame

if __name__ == "__main__":
    vc = VideoCamera()
    img = vc.get_frame()
    img.show()
    vc.close_session()