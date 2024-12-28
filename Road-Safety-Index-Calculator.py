class RoadSafetyIndexCalculator:
    def __init__(self, road_condition, traffic_density, weather_condition, speed_limit, road_type, accident_history):
        self.road_condition = road_condition
        self.traffic_density = traffic_density
        self.weather_condition = weather_condition
        self.speed_limit = speed_limit
        self.road_type = road_type
        self.accident_history = accident_history

    def calculate_index(self):
       
        safety_index = 100

        if self.road_condition == "slippery":
            safety_index -= 20
        elif self.road_condition == "wet":
            safety_index -= 10
        elif self.road_condition == "icy":
            safety_index -= 30
 
        if self.traffic_density == "high":
            safety_index -= 20
        elif self.traffic_density == "moderate":
            safety_index -= 10
 
        if self.weather_condition == "rainy":
            safety_index -= 15
        elif self.weather_condition == "foggy":
            safety_index -= 25

        if self.speed_limit > 100:
            safety_index -= 10
        elif self.speed_limit < 30:
            safety_index += 5  

      
        if self.road_type == "city":
            safety_index -= 15
        elif self.road_type == "rural":
            safety_index -= 10
      
        if self.accident_history > 5:
            safety_index -= 30
        elif self.accident_history > 2:
            safety_index -= 15

        if safety_index < 0:
            safety_index = 0

        return safety_index

    def get_safety_level(self):
        score = self.calculate_index()
        if score >= 80:
            return f"Road is safe with a Safety Index of {score}/100."
        elif 50 <= score < 80:
            return f"Moderately safe road with a Safety Index of {score}/100."
        else:
            return f"Road is dangerous with a Safety Index of {score}/100."


if __name__ == "__main__":
  
    road_condition = input("Enter road condition (clear, slippery, wet, icy): ").lower()
    traffic_density = input("Enter traffic density (low, moderate, high): ").lower()
    weather_condition = input("Enter weather condition (sunny, rainy, foggy): ").lower()
    speed_limit = int(input("Enter speed limit (km/h): "))
    road_type = input("Enter road type (highway, city, rural): ").lower()
    accident_history = int(input("Enter number of accidents in the last year: "))

    calculator = RoadSafetyIndexCalculator(road_condition, traffic_density, weather_condition, speed_limit, road_type, accident_history)

    print(calculator.get_safety_level())
