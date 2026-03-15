import math
def maximum_height(launch_velocity, launch_angle):
    # [LaunchVelocity]^2*(Sin([LaunchAngle]*(22/7)/180))^2/(2*9.8)
    return (launch_velocity ** 2) * (math.sin(launch_angle * (22 / 7) / 180) ** 2) / (2 * 9.8)
def horizontal_distance(launch_velocity, launch_angle):
    # Range(Horizontal distance) =(([LaunchVelocity]^2)*Round(Sin(2*[LaunchAngle]*(3.1416)/180),6))/9.8
    return ((launch_velocity ** 2) * round(math.sin(2 * launch_angle * (3.1416)/180), 6)) / 9.8
def flight_time(launch_velocity, launch_angle):
    #timetaken to reach maximum height =([LaunchVelocity]*Sin([LaunchAngle]*(22/7)/180))/9.8
    return (launch_velocity * math.sin(launch_angle * (22 / 7) / 180)) / 9.8
def main():
    launch_velocity = float(input("Enter the launch velocity (m/s): "))
    launch_angle = float(input("Enter the launch angle (degrees): "))
    
    max_height = maximum_height(launch_velocity, launch_angle)
    horiz_distance = horizontal_distance(launch_velocity, launch_angle)
    time_of_flight = flight_time(launch_velocity, launch_angle)   # Total time of flight is double the time to reach max height
    
    print(f"Maximum Height: {max_height:.2f} meters")
    print(f"Horizontal Distance: {horiz_distance:.2f} meters")
    print(f"Time of Flight: {time_of_flight:.2f} seconds")

if __name__ == '__main__':
    main()