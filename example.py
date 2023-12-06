import pybullet as p
import pybullet_data
import time

# Initial environment set-up
physics_client = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
plane = p.loadURDF("plane.urdf")
control_dt = 1. / 240.

# Camera properties
camera_distance = 0.8
camera_yaw = 135.0
camera_pitch = -45.0
camera_target_position = [0.0, 0.0, 0.3]

# Set camera properties
p.resetDebugVisualizerCamera(camera_distance, camera_yaw, camera_pitch, camera_target_position)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)

# Object start pose
object1_start_position = [0.0, 0.0, 0.1]
object1_start_orientation_e = [0.0, 0.0, 0.0]
object1_start_orientation_q = p.getQuaternionFromEuler(object1_start_orientation_e)

# You can load more objects like this:
object2_start_position = [-0.5, 0.0, 0.1]
object2_start_orientation_e = [0.0, 0.0, 0.0]
object2_start_orientation_q = p.getQuaternionFromEuler(object2_start_orientation_e)

object3_start_position = [0.0, -0.5, 0.1]
object3_start_orientation_e = [0.0, 0.0, 0.0]
object3_start_orientation_q = p.getQuaternionFromEuler(object3_start_orientation_e)
# etc.

# Scale of the objects
global_scaling = 0.08

# Load the object in the environment
object1_model = p.loadURDF("ycb_assets/002_master_chef_can.urdf", object1_start_position, object1_start_orientation_q, useFixedBase=False, globalScaling=global_scaling)

# You can load more objects like this:
object2_model = p.loadURDF("ycb_assets/003_cracker_box.urdf", object2_start_position, object2_start_orientation_q, useFixedBase=False, globalScaling=global_scaling)
object3_model = p.loadURDF("ycb_assets/004_sugar_box.urdf", object3_start_position, object3_start_orientation_q, useFixedBase=False, globalScaling=global_scaling)
# etc.

# Keep the simulation running
while True:
    p.stepSimulation()
    time.sleep(control_dt)
