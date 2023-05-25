;; Auto-generated. Do not edit!


(when (boundp 'oogway_search_service::service)
  (if (not (find-package "OOGWAY_SEARCH_SERVICE"))
    (make-package "OOGWAY_SEARCH_SERVICE"))
  (shadow 'service (find-package "OOGWAY_SEARCH_SERVICE")))
(unless (find-package "OOGWAY_SEARCH_SERVICE::SERVICE")
  (make-package "OOGWAY_SEARCH_SERVICE::SERVICE"))
(unless (find-package "OOGWAY_SEARCH_SERVICE::SERVICEREQUEST")
  (make-package "OOGWAY_SEARCH_SERVICE::SERVICEREQUEST"))
(unless (find-package "OOGWAY_SEARCH_SERVICE::SERVICERESPONSE")
  (make-package "OOGWAY_SEARCH_SERVICE::SERVICERESPONSE"))

(in-package "ROS")





(defclass oogway_search_service::serviceRequest
  :super ros::object
  :slots (_angular_velocity ))

(defmethod oogway_search_service::serviceRequest
  (:init
   (&key
    ((:angular_velocity __angular_velocity) 0.0)
    )
   (send-super :init)
   (setq _angular_velocity (float __angular_velocity))
   self)
  (:angular_velocity
   (&optional __angular_velocity)
   (if __angular_velocity (setq _angular_velocity __angular_velocity)) _angular_velocity)
  (:serialization-length
   ()
   (+
    ;; float32 _angular_velocity
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _angular_velocity
       (sys::poke _angular_velocity (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _angular_velocity
     (setq _angular_velocity (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass oogway_search_service::serviceResponse
  :super ros::object
  :slots (_success ))

(defmethod oogway_search_service::serviceResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass oogway_search_service::service
  :super ros::object
  :slots ())

(setf (get oogway_search_service::service :md5sum-) "c3f0723336176df636671fb21af3864b")
(setf (get oogway_search_service::service :datatype-) "oogway_search_service/service")
(setf (get oogway_search_service::service :request) oogway_search_service::serviceRequest)
(setf (get oogway_search_service::service :response) oogway_search_service::serviceResponse)

(defmethod oogway_search_service::serviceRequest
  (:response () (instance oogway_search_service::serviceResponse :init)))

(setf (get oogway_search_service::serviceRequest :md5sum-) "c3f0723336176df636671fb21af3864b")
(setf (get oogway_search_service::serviceRequest :datatype-) "oogway_search_service/serviceRequest")
(setf (get oogway_search_service::serviceRequest :definition-)
      "float32 angular_velocity
---
bool success

")

(setf (get oogway_search_service::serviceResponse :md5sum-) "c3f0723336176df636671fb21af3864b")
(setf (get oogway_search_service::serviceResponse :datatype-) "oogway_search_service/serviceResponse")
(setf (get oogway_search_service::serviceResponse :definition-)
      "float32 angular_velocity
---
bool success

")



(provide :oogway_search_service/service "c3f0723336176df636671fb21af3864b")


