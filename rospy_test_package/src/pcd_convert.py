#! /usr/bin/env python3
import open3d as o3d
#import pclpy 
#from pclpy import pcl
#import pcl


mesh = o3d.io.read_triangle_mesh("/home/benceubuntu/catkin_ws/src/pointcloud/PLY/UjPLY40.ply")
pointcloud = mesh.sample_points_poisson_disk(100000)

# you can plot and check
#o3d.visualization.draw_geometries([mesh])
o3d.visualization.draw_geometries([pointcloud])

#pcl.save(pointcloud, "pointcld.pcd")

o3d.io.write_point_cloud("/home/benceubuntu/catkin_ws/src/pointcloud/PCD/pointcloud_PCD.pcd", pointcloud)
