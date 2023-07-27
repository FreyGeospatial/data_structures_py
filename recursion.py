import copy

cloud_event_1 = {
    "id": "abc123",
    "source": "/example/service",
    "specversion": "1.0",
    "type": "com.example.eventType",
    "data": {
        "message": "Hello, CloudEvents!",
        "count": 42,
        "custom_data": {
            "status": "OK",
            "value": 3.14,
            "extra_level_1": {
                "description": "This is an additional nested level",
                "flag": True
            },
            "extra_level_2": {
                "category": "Testing",
                "result": "Pass",
                "details": {
                    "key1": "value1",
                    "key2": "value2"
                }
            }
        }
    },
    "extensions": {
        "custom_extension": "some value",
        "other_extension": 12345
    }
}

cloud_event_2 = {
    "id": "def456",
    "source": "/another/service",
    "specversion": "1.0",
    "type": "com.example.anotherEventType",
    "data": {
        "message": "Welcome to CloudEvents!",
        "timestamp": "2023-07-27T12:34:56Z",
        "nested_data": {
            "status": "ERROR",
            "value": 7.89,
            "custom_info": {
                "description": "This is a custom nested level",
                "flag": False
            },
            "extra_info": {
                "category": "Development",
                "result": "Fail",
                "details": {
                    "key3": "value3",
                    "key4": "value4"
                }
            }
        }
    },
    "extensions": {
        "custom_extension": "some other value",
        "additional_extension": "extra data"
    }
}




def update_cloud_event_value(cloud_event_dict, location, new_value):
    """
    Update a value in the CloudEvent dictionary based on the specified location.

    Args:
        cloud_event_dict (dict): The dictionary representing the CloudEvent.
        location (list): A list of keys indicating the path to the value to update.
        new_value: The new value to replace the existing value.

    Returns:
        dict: A new dictionary representing the updated CloudEvent with the new value.
    """
    # Create a copy of the original dictionary to avoid modifying it directly
    updated_cloud_event = copy.deepcopy(cloud_event_dict)

    current_dict = updated_cloud_event
    for key in location[:-1]:
        current_dict = current_dict.get(key, {})
    current_dict[location[-1]] = new_value

    return updated_cloud_event


# Example usage:

# Updating value in CloudEvent 1
new_cloud_event_1 = update_cloud_event_value(cloud_event_1, ["data", "custom_data", "status"], "UPDATED") # OG VAKUE: "OK:

print("old cloud event 1:")
print(cloud_event_1)
print()
print()
print("new cloud event 1:")
print()
print(new_cloud_event_1)
print()
print(cloud_event_1 == new_cloud_event_1)


# Updating value in CloudEvent 2
new_cloud_event_2 = update_cloud_event_value(cloud_event_2, ["data", "nested_data", "extra_info", "result"], "Success") # OG VALUE: "FAIL"


print()
print()

print("old cloud event 2")
print(cloud_event_2)
print()
print()
print("new cloud event 2:")
print(new_cloud_event_2)
print(cloud_event_2 == new_cloud_event_2)



def update_cloud_event_value(cloud_event_dict, location, new_value):
    """
    Update a value in the CloudEvent dictionary based on the specified location.

    Args:
        cloud_event_dict (dict): The dictionary representing the CloudEvent.
        location (list): A list of keys indicating the path to the value to update.
        new_value: The new value to replace the existing value.

    Returns:
        dict: A new dictionary representing the updated CloudEvent with the new value.
    """
    def update_recursively(current_dict, keys, new_val):
        if len(keys) == 1:
            current_dict[keys[0]] = new_val
        elif keys[0] in current_dict:
            update_recursively(current_dict[keys[0]], keys[1:], new_val)

    # Create a copy of the original dictionary to avoid modifying it directly
    updated_cloud_event = copy.deepcopy(cloud_event_dict)

    # Call the recursive function to update the value
    update_recursively(updated_cloud_event, location, new_value)

    return updated_cloud_event

cloud_event_1_recursive = update_cloud_event_value(cloud_event_1, ["data", "custom_data", "status"], "BLAH BLAH BLAH")

print()
print()
print("cloud event 1 recursively: ")
print(cloud_event_1_recursive)