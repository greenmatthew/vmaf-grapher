class Frame:
    """
    Represents a frame with various video quality metrics as extracted from VMAF analysis.

    Attributes:
        frame_num (int): Frame number.
        int_motion2 (float): The motion value calculated by the VMAF model at a specific scale.
        int_motion (float): The motion value calculated by the VMAF model.
        int_adm2 (float): The ADM value calculated by the VMAF model.
        int_adm_scale0 (float): The ADM scale 0 value calculated by the VMAF model.
        int_adm_scale1 (float): The ADM scale 1 value calculated by the VMAF model.
        int_adm_scale2 (float): The ADM scale 2 value calculated by the VMAF model.
        int_adm_scale3 (float): The ADM scale 3 value calculated by the VMAF model.
        int_vif_scale0 (float): The VIF scale 0 value calculated by the VMAF model.
        int_vif_scale1 (float): The VIF scale 1 value calculated by the VMAF model.
        int_vif_scale2 (float): The VIF scale 2 value calculated by the VMAF model.
        int_vif_scale3 (float): The VIF scale 3 value calculated by the VMAF model.
        vmaf (float): The overall VMAF score for the frame.
    """

    def __init__(self, frame_num: int, int_motion2: float, int_motion: float, int_adm2: float, int_adm_scale0: float,
                 int_adm_scale1: float, int_adm_scale2: float, int_adm_scale3: float, int_vif_scale0: float,
                 int_vif_scale1: float, int_vif_scale2: float, int_vif_scale3: float, vmaf: float):
        """
        Initializes a new instance of the Frame class with all necessary metrics.
        """
        self.frame_num = frame_num
        self.int_motion2 = int_motion2
        self.int_motion = int_motion
        self.int_adm2 = int_adm2
        self.int_adm_scale0 = int_adm_scale0
        self.int_adm_scale1 = int_adm_scale1
        self.int_adm_scale2 = int_adm_scale2
        self.int_adm_scale3 = int_adm_scale3
        self.int_vif_scale0 = int_vif_scale0
        self.int_vif_scale1 = int_vif_scale1
        self.int_vif_scale2 = int_vif_scale2
        self.int_vif_scale3 = int_vif_scale3
        self.vmaf = vmaf

    @staticmethod
    def from_strings(frame_num: str, int_motion2: str, int_motion: str, int_adm2: str, int_adm_scale0: str,
                    int_adm_scale1: str, int_adm_scale2: str, int_adm_scale3: str, int_vif_scale0: str,
                    int_vif_scale1: str, int_vif_scale2: str, int_vif_scale3: str, vmaf: str):
        """
        Factory method to create a Frame instance from string inputs, converting them to appropriate data types.

        Args:
            frame_num (str): The frame number as a string.
            All other arguments are metric values as strings, which are described in the class attributes.

        Returns:
            Frame: A new Frame instance with all attributes converted to their appropriate data types.
        """
        return Frame(
            int(frame_num), float(int_motion2), float(int_motion), float(int_adm2), float(int_adm_scale0),
            float(int_adm_scale1), float(int_adm_scale2), float(int_adm_scale3), float(int_vif_scale0),
            float(int_vif_scale1), float(int_vif_scale2), float(int_vif_scale3), float(vmaf)
        )

    def __repr__(self):
        """
        Returns a string representation of the Frame instance.

        Returns:
            str: A string representation of the frame's metrics.
        """
        return (f"Frame(frame_num={self.frame_num}, int_motion2={self.int_motion2}, int_motion={self.int_motion}, "
                f"int_adm2={self.int_adm2}, int_adm_scale0={self.int_adm_scale0}, int_adm_scale1={self.int_adm_scale1}, "
                f"int_adm_scale2={self.int_adm_scale2}, int_adm_scale3={self.int_adm_scale3}, "
                f"int_vif_scale0={self.int_vif_scale0}, int_vif_scale1={self.int_vif_scale1}, "
                f"int_vif_scale2={self.int_vif_scale2}, int_vif_scale3={self.int_vif_scale3}, vmaf={self.vmaf})")
