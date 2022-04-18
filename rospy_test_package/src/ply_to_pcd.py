#! /usr/bin/env python3
import open3d as o3d
#import pclpy 
#from pclpy import pcl
#import pcl

val = input("Input ply: ")
print(val)

pcd = o3d.io.read_point_cloud(val)
output = input("Kimeneti fájl: ")
print(output)
o3d.io.write_point_cloud(output, pcd)
