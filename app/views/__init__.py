from .Course import course_bp
from .Student import student_bp
from .Teacher import teacher_bp
from .JoinRequest import join_request_bp

blueprints = (student_bp, course_bp, teacher_bp, join_request_bp)