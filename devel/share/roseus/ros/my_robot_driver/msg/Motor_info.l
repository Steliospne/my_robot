;; Auto-generated. Do not edit!


(when (boundp 'my_robot_driver::Motor_info)
  (if (not (find-package "MY_ROBOT_DRIVER"))
    (make-package "MY_ROBOT_DRIVER"))
  (shadow 'Motor_info (find-package "MY_ROBOT_DRIVER")))
(unless (find-package "MY_ROBOT_DRIVER::MOTOR_INFO")
  (make-package "MY_ROBOT_DRIVER::MOTOR_INFO"))

(in-package "ROS")
;;//! \htmlinclude Motor_info.msg.html


(defclass my_robot_driver::Motor_info
  :super ros::object
  :slots (_state ))

(defmethod my_robot_driver::Motor_info
  (:init
   (&key
    ((:state __state) "")
    )
   (send-super :init)
   (setq _state (string __state))
   self)
  (:state
   (&optional __state)
   (if __state (setq _state __state)) _state)
  (:serialization-length
   ()
   (+
    ;; string _state
    4 (length _state)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _state
       (write-long (length _state) s) (princ _state s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _state
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get my_robot_driver::Motor_info :md5sum-) "af6d3a99f0fbeb66d3248fa4b3e675fb")
(setf (get my_robot_driver::Motor_info :datatype-) "my_robot_driver/Motor_info")
(setf (get my_robot_driver::Motor_info :definition-)
      "string state
")



(provide :my_robot_driver/Motor_info "af6d3a99f0fbeb66d3248fa4b3e675fb")


