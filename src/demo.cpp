#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/core/core.hpp>
#include <iostream>
#include <string>
using
namespace  cv;

using
namespace  std;

int main(int argc, char** argv)
{
    int count=100;
    VideoCapture capture(0);
    capture.set(CAP_PROP_FRAME_WIDTH, 1920);
    capture.set(CAP_PROP_FRAME_HEIGHT, 1080);
    while (1)
    {
        Mat frame;
        capture >> frame;

        if (frame.empty()) {
            break;
        }
        int h = frame.rows;
        int w = frame.cols;
        const char *name = "video";
        namedWindow(name, 0);
        imshow(name, frame);
        waitKey(20);
    }
    return 0;
}
