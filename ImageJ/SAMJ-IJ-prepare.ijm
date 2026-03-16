// 0) Load the time series of images for the cell aggregation experiment.
//setTool("point");
// 1) Use the point selection tool to mark a point inside each cell-filled microwell. 
// 2) Press the “t” key to add the selected point to the ROI manager.
// 3) Repeat this procedure until all microwells of interest are selected
// 4) Run the provided script.
// A folder will be automatically created (named after the image title) to save the selected ROIs for further analysis.
main_image_name = getTitle();
main_image_nameshort = substring(main_image_name,0,main_image_name.length-4);
print(main_image_nameshort);
//current_name = main_image_nameshort + "-1.tif";
dir = getDirectory("image");
dirR = dir + main_image_nameshort + "/";
if (!File.exists(dirR)) {
    File.makeDirectory(dirR);
    print("Folder created: " + dirR);
}
roiManager("Save", dirR + "RoiSet0.zip");
roiManager("Delete");
