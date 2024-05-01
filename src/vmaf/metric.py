class Metric:
    """
    Represents a metric with its statistical measures from the VMAF XML output.

    Attributes:
        name (str): The name of the metric.
        min (float): The minimum value of the metric.
        max (float): The maximum value of the metric.
        mean (float): The average value of the metric.
        harmonic_mean (float): The harmonic mean of the metric.
    """

    def __init__(self, name: str, min: float, max: float, mean: float, harmonic_mean: float):
        """
        Initializes a new instance of the Metric class.

        Args:
            name (str): The name of the metric.
            min (float): The minimum value of the metric.
            max (float): The maximum value of the metric.
            mean (float): The average value of the metric.
            harmonic_mean (float): The harmonic mean of the metric.
        """
        self.name = name
        self.min = min
        self.max = max
        self.mean = mean
        self.harmonic_mean = harmonic_mean

    @staticmethod
    def from_strings(name: str, min: str, max: str, mean: str, harmonic_mean: str):
        """
        Factory method to create a Metric instance from string inputs.

        Args:
            name (str): The name of the metric.
            min (str): The minimum value of the metric as a string.
            max (str): The maximum value of the metric as a string.
            mean (str): The average value of the metric as a string.
            harmonic_mean (str): The harmonic mean of the metric as a string.

        Returns:
            Metric: A new Metric instance with all attributes converted to float.
        """
        return Metric(name, float(min), float(max), float(mean), float(harmonic_mean))

    def __repr__(self):
        """
        Returns a string representation of the Metric instance.

        Returns:
            str: A string representation of the metric.
        """
        return (f"Metric(name={self.name}, min={self.min}, max={self.max}, "
                f"mean={self.mean}, harmonic_mean={self.harmonic_mean})")
