cv::Mat img = cv::imread("pic1.jpg");
for(int j=0;j<img.rows;j++)
    {
    for (int i=0;i<img.cols;i++)
      {
        std::cout << "Matrix of image loaded is: " << img.at<uchar>(i,j);
      }
    }