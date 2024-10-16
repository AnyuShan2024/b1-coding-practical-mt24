class Controller:
    def __init__(self):
        """
        Parent class for any type of controller.
        """
        pass

    def compute_action(self, current_value: float, reference_value: float) -> float:
        """
        Placeholder method to compute the control action. Should be implemented by subclasses.
        
        Args:
            current_value (float): The current observed value (e.g., depth of the submarine).
            reference_value (float): The reference value at the current time step.
        
        Returns:
            float: The control action to be applied.
        """

        raise NotImplementedError("This method should be overridden by subclasses")
    
class PDController(Controller):
    def __init__(self, Kp: float, Kd: float):
        """
        PD Controller subclass. Implements a Proportional-Derivative control scheme for tracking.
        
        Args:
            Kp (float): Proportional gain.
            Kd (float): Derivative gain.
        """
        super().__init__()
        self.Kp = Kp  # Proportional gain
        self.Kd = Kd  # Derivative gain
        self.last_error = 0.0  # To store the previous error value
    
    def compute_action(self, current_value: float, reference_value: float) -> float:
        """
        Computes the control action using PD control for tracking a time-varying reference.
        
        Args:
            current_value (float): The current observed value (e.g., depth of the submarine).
            reference_value (float): The reference value to track at the current time step.
        
        Returns:
            float: The control action to be applied.
        """
        # Calculate the error (difference between reference and current value)
        error = reference_value - current_value

        # Calculate the proportional term
        proportional = self.Kp * error

        # Calculate the derivative term (rate of change of error)
        derivative = self.Kd * (error - self.last_error)

        # Store the current error for the next time step
        self.last_error = error

        # The control action is the sum of the proportional and derivative terms
        return proportional + derivative