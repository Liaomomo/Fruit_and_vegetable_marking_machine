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
	namedWindow("ԭͼ", CV_WINDOW_AUTOSIZE);
	imshow("ԭͼ", src_img);
	cvtColor(src_img, gray_img, COLOR_BGR2GRAY);   // ��ɫͼת��Ϊ�Ҷ�ͼ
 
	// ���Ҷ�ͼ����ж�ֵ�ָ�
	threshold(gray_img, binary_img, 0, 255, THRESH_BINARY|THRESH_TRIANGLE);
	imshow("��ֵͼ", binary_img);
 
	// ��̬ѧ����
	Mat kernel = getStructuringElement(MORPH_RECT, Size(5,5), Point(-1, -1));     //��ȡ���νṹԪ
	erode(binary_img, binary_img, kernel, Point(-1, -1), 1);
	dilate(binary_img, binary_img, kernel, Point(-1, -1), 1);
	imshow("��������", binary_img);
 
 
	// ��ͨ�������
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
	printf("���Ľ������Ŀ�� : %d", contours.size());
	imshow("���ս��", markers);
 
	waitKey(0);
	return 0;
}

