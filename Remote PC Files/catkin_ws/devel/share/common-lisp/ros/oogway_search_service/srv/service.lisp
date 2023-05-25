; Auto-generated. Do not edit!


(cl:in-package oogway_search_service-srv)


;//! \htmlinclude service-request.msg.html

(cl:defclass <service-request> (roslisp-msg-protocol:ros-message)
  ((angular_velocity
    :reader angular_velocity
    :initarg :angular_velocity
    :type cl:float
    :initform 0.0))
)

(cl:defclass service-request (<service-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <service-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'service-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name oogway_search_service-srv:<service-request> is deprecated: use oogway_search_service-srv:service-request instead.")))

(cl:ensure-generic-function 'angular_velocity-val :lambda-list '(m))
(cl:defmethod angular_velocity-val ((m <service-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader oogway_search_service-srv:angular_velocity-val is deprecated.  Use oogway_search_service-srv:angular_velocity instead.")
  (angular_velocity m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <service-request>) ostream)
  "Serializes a message object of type '<service-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angular_velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <service-request>) istream)
  "Deserializes a message object of type '<service-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angular_velocity) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<service-request>)))
  "Returns string type for a service object of type '<service-request>"
  "oogway_search_service/serviceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'service-request)))
  "Returns string type for a service object of type 'service-request"
  "oogway_search_service/serviceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<service-request>)))
  "Returns md5sum for a message object of type '<service-request>"
  "c3f0723336176df636671fb21af3864b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'service-request)))
  "Returns md5sum for a message object of type 'service-request"
  "c3f0723336176df636671fb21af3864b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<service-request>)))
  "Returns full string definition for message of type '<service-request>"
  (cl:format cl:nil "float32 angular_velocity~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'service-request)))
  "Returns full string definition for message of type 'service-request"
  (cl:format cl:nil "float32 angular_velocity~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <service-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <service-request>))
  "Converts a ROS message object to a list"
  (cl:list 'service-request
    (cl:cons ':angular_velocity (angular_velocity msg))
))
;//! \htmlinclude service-response.msg.html

(cl:defclass <service-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass service-response (<service-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <service-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'service-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name oogway_search_service-srv:<service-response> is deprecated: use oogway_search_service-srv:service-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <service-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader oogway_search_service-srv:success-val is deprecated.  Use oogway_search_service-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <service-response>) ostream)
  "Serializes a message object of type '<service-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <service-response>) istream)
  "Deserializes a message object of type '<service-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<service-response>)))
  "Returns string type for a service object of type '<service-response>"
  "oogway_search_service/serviceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'service-response)))
  "Returns string type for a service object of type 'service-response"
  "oogway_search_service/serviceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<service-response>)))
  "Returns md5sum for a message object of type '<service-response>"
  "c3f0723336176df636671fb21af3864b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'service-response)))
  "Returns md5sum for a message object of type 'service-response"
  "c3f0723336176df636671fb21af3864b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<service-response>)))
  "Returns full string definition for message of type '<service-response>"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'service-response)))
  "Returns full string definition for message of type 'service-response"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <service-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <service-response>))
  "Converts a ROS message object to a list"
  (cl:list 'service-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'service)))
  'service-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'service)))
  'service-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'service)))
  "Returns string type for a service object of type '<service>"
  "oogway_search_service/service")