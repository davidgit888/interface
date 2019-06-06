#ifndef _WATERMARK_H_
#define _WATERMARK_H_

#include <opencv2/opencv.hpp>
#include <iostream>

extern "C" {
std::string watermarkDetect(cv::Mat & srcImgRGB);
int addFunction(int a,int b);
}
#endif
