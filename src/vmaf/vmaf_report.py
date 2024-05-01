import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

from .frame import Frame
from .metric import Metric

class VMAFReport:
    """
    Represents a VMAF report, encapsulating the data found in a VMAF XML output.

    Attributes:
        version (str): The version of the VMAF tool used to generate the report.
        params (dict): Parameters that specify the configuration of the VMAF analysis,
                       such as the quality width and height of the video.
        fyi (dict): Informational data about the VMAF process, like frames per second.
        frames (list('Frame')): A list of Frame objects, each representing metrics computed for a single video frame.
        metrics (dict('string', 'Metric')): A list of Metric objects, representing aggregated metrics across all frames.
    """

    def __init__(self, version: str):
        """
        Initializes a new instance of the VMAFReport class.

        Args:
            version (str): The version identifier of the VMAF tool.
        """
        self.version = version
        self.params = {}  # Parameters like qualityWidth and qualityHeight
        self.fyi = {}     # Information like fps
        self.frames = []  # List to store Frame objects
        self.metrics = {} # List to store Metric objects representing pooled metrics

    def __repr__(self):
        """
        Returns a string representation of the VMAFReport instance.

        Returns:
            str: A string representation of the VMAF report including version, parameters, and metrics.
        """
        return (f"VMAFReport(version={self.version}, params={self.params}, fyi={self.fyi}, "
                f"frames={len(self.frames)} frames, metrics={self.metrics})")
    
    @staticmethod
    def from_file(file_path: str) -> 'VMAFReport':
        """
        Parses a VMAF XML file and constructs a VMAFReport object from it.

        Args:
            file_path (str): The path to the VMAF XML file.

        Returns:
            VMAFReport: A VMAFReport object populated with data from the XML file.
        """
        tree = ET.parse(file_path)
        root = tree.getroot()
        report = VMAFReport(root.attrib['version'])
        
        # Process parameters
        params = root.find('params')
        if params is not None:
            # Update to access attributes of the <params> element directly
            report.params = {key: value for key, value in params.attrib.items()}
        
        # Process fyi
        fyi = root.find('fyi')
        if fyi is not None:
            # Update to access attributes of the <fyi> element directly
            report.fyi = {key: value for key, value in fyi.attrib.items()}

        # Process frames
        frames = root.find('frames')
        if frames is not None:
            for frame in frames.findall('frame'):
                report.frames.append(Frame.from_strings(
                    frame_num=frame.attrib['frameNum'],
                    int_motion2=frame.attrib['integer_motion2'],
                    int_motion=frame.attrib['integer_motion'],
                    int_adm2=frame.attrib['integer_adm2'],
                    int_adm_scale0=frame.attrib['integer_adm_scale0'],
                    int_adm_scale1=frame.attrib['integer_adm_scale1'],
                    int_adm_scale2=frame.attrib['integer_adm_scale2'],
                    int_adm_scale3=frame.attrib['integer_adm_scale3'],
                    int_vif_scale0=frame.attrib['integer_vif_scale0'],
                    int_vif_scale1=frame.attrib['integer_vif_scale1'],
                    int_vif_scale2=frame.attrib['integer_vif_scale2'],
                    int_vif_scale3=frame.attrib['integer_vif_scale3'],
                    vmaf=frame.attrib['vmaf']))

        # Process pooled metrics
        pooled_metrics = root.find('pooled_metrics')
        if pooled_metrics is not None:
            for metric in pooled_metrics.findall('metric'):
                report.metrics[metric.attrib['name']] = Metric.from_strings(
                    name=metric.attrib['name'],
                    min=metric.attrib['min'],
                    max=metric.attrib['max'],
                    mean=metric.attrib['mean'],
                    harmonic_mean=metric.attrib['harmonic_mean'])

        return report
    
    def show_graph(self, downsample_factor=1):
        """
        Plots the VMAF scores of all frames in the report as a line graph with the area under the curve filled,
        with optional downsampling.

        Args:
            downsample_factor (int): The factor by which to downsample the data; default is 1 (no downsampling).
        """
        # Apply downsampling
        vmaf_scores = [frame.vmaf for i, frame in enumerate(self.frames) if i % downsample_factor == 0]
        frame_numbers = [frame.frame_num for i, frame in enumerate(self.frames) if i % downsample_factor == 0]

        plt.figure(figsize=(12, 6))
        plt.fill_between(frame_numbers, vmaf_scores, color="skyblue", alpha=0.4)  # Fill under the line
        plt.plot(frame_numbers, vmaf_scores, label='VMAF Score per Frame', color='SlateBlue', alpha=0.6)  # Line on top
        plt.title('VMAF Score Trend')
        plt.xlabel('Frame Number')
        plt.ylabel('VMAF Score')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Show interactive tools in matplotlib
        # plt.ion()  # Turn on interactive mode
        plt.show()
