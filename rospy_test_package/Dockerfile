FROM ros:noetic

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    python3-rosdep \
    python3-rosinstall \
    && rm -rf /var/lib/apt/lists/*


ENV ROS_WS=/root/catkin_ws
RUN mkdir -p $ROS_WS/src
WORKDIR $ROS_WS/src

COPY . ~/catkin_ws/src/

# install ros package
RUN rosdep init && \
    rosdep update --rosdistro $ROS_DISTRO \
    && rm -rf /var/lib/apt/lists/*
    #rosdep install -y \
    # --from-paths \
    #    /home/benceubuntu/catkin_ws/src/ &&\
    # --ignore-src && \
    #rosdep update -y && \
    #catkin_make && \
    #rm -rf /var/lib/apt/lists/*

#RUN catkin config \
#      --extend /opt/ros/$ROS_DISTRO && \
#    catkin build \
#      rospy_test_package

RUN sed --in-place --expression \
      '$isource "$ROS_WS/devel/setup.bash"' \
      /ros_entrypoint.sh

CMD ["roslaunch"]

