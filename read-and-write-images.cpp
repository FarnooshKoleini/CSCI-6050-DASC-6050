/*
	this code demonstrates how to read and 
	write images using OpenCV
*/


#include <iostream>
#include <string>
#include <sstream>
using namespace std;

// OpenCV includes
#include "opencv2/core.hpp"
#include "opencv2/highgui.hpp"
using namespace cv;

int main( int argc, const char** argv )
{
	if (argc != 2) {
		std::cerr << "usage: " << argv[0] << " <path to image file>" << std::endl;
		return 0;
	}

	std::string img_file_path = argv[1];

	// read a color image
	Mat clr_img = imread(img_file_path);

	// read a color image as a grayscale image
	// note the second argument to imread()
	Mat gsc_img = imread(img_file_path, 0);
	
	// write image to current directory on disk
	imwrite("akshara_gsc.jpg", gsc_img);
	
	// choose a pixel
	int row_num = clr_img.rows-1;
	int col_num = clr_img.cols-1;

	// read the color pixel (R, G, and B) values into a vector
	Vec3b pixel = clr_img.at<Vec3b>(row_num, col_num);

	// print the RGB values
	cout << "Pixel value (B,G,R): (" << (int)pixel[0] << "," << (int)pixel[1] << "," << (int)pixel[2] << ")" << endl;
	
	// display the color image
	imshow("Color image", clr_img);

	// display the grayscale image
	imshow("Grayscale image", gsc_img);
	
	// wait for any key press to close image display windows
	waitKey(0);

	return 0;
}