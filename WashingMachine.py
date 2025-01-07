import time

def washing_machine_cycle():
    # Time duration for each stage (in seconds)
    wash_duration = 15  # Wash
    rinse_duration = 10  # Rinse
    spin_duration = 5    # Spin

    while True:
        # Wash stage
        print("Washing: START")
        time.sleep(wash_duration)
        
        print("Washing: DONE")
        time.sleep(1)  # Time to transition to next stage
        
        # Rinse stage
        print("Rinsing: START")
        time.sleep(rinse_duration)
        
        print("Rinsing: DONE")
        time.sleep(1)  # Time to transition to next stage
        
        # Spin stage
        print("Spinning: START")
        time.sleep(spin_duration)
        
        print("Spinning: DONE")
        time.sleep(1)  # Time to transition before repeating cycle

# Run the washing machine cycle
washing_machine_cycle()
