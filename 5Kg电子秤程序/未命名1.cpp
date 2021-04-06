#include <opencv2/opencv.hpp>
#include <iostream>
#include <math.h>
 
using namespace cv;
using namespace std;
 
int main( )
{
	Mat  src_img,gray_img, binary_img;
    src_img = imread("d:/20200505_234426.jpg");
	if (src_img.empty()) 
	{
		printf("could not load the image...\n");
		return -1;
	}
	namedWindow("原图", CV_WINDOW_AUTOSIZE);
	imshow("原图", src_img);
	cvtColor(src_img, gray_img, COLOR_BGR2GRAY);   // 彩色图转化为灰度图
 
	// 将灰度图像进行二值分割
	threshold(gray_img, binary_img, 0, 255, THRESH_BINARY|THRESH_TRIANGLE);
	imshow("二值图", binary_img);
 
	// 形态学操作
	Mat kernel = getStructuringElement(MORPH_RECT, Size(5,5), Point(-1, -1));     //获取矩形结构元
	erode(binary_img, binary_img, kernel, Point(-1, -1), 1);
	dilate(binary_img, binary_img, kernel, Point(-1, -1), 1);
	imshow("膨胀运算", binary_img);
 
 
	// 连通区域计数
	vector<vector<Point>> contours;
	findContours(binary_img, contours, CV_RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);
 
	// draw result
	Mat markers = Mat::zeros(src_img.size(), CV_8UC3);
	RNG rng(12345);
	for (size_t t = 0; t < contours.size(); ++t) 
	{
		drawContours(markers, contours, static_cast<int>(t), Scalar(rng.uniform(0, 255), rng.uniform(0, 255), rng.uniform(0, 255)),
			-1, 8, Mat());
	}
	printf("检测的结果（数目） : %d", contours.size());
	imshow("最终结果", markers);
 
	waitKey(0);
	return 0;
}

