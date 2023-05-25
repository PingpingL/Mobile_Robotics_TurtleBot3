import rospy
from oogway_search_service.srv import service

def call_service():
    rospy.wait_for_service('service')
    try:
        serv = rospy.ServiceProxy('service', service)
        response = serv()
        print('test')
        return response.success
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

if __name__ == '__main__':
    print('test2')
    rospy.init_node('interrupt_client')
    rate = rospy.Rate(0.05) # 0.1 Hz, i.e. every 10 seconds
    while not rospy.is_shutdown():
    	print('test3')
    	success = call_service()
    	print("Service call success: %s" % success)
    	rate.sleep()
