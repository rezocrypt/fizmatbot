# Import libraries
from datetime import datetime
import pytz



# Class and rest times
first_class = [0,45]
first_rest  = [45,50]
second_class = [50,95]
second_rest = [95,100]
third_class = [100,145]
third_rest  = [145,175]
fourth_class = [175,220]
fourth_rest = [220,225]
fifth_class = [225,270]
fifth_rest = [270,275]
sixth_class = [275,320]
sixth_rest = [320,325]
seventh_class = [325,370]
seventh_rest = [370,375]


# Main function
def Main():

    # Make some important variables
    tz = pytz.timezone("Etc/GMT-4")
    time_ = datetime.now()
    time = time_.replace(tzinfo=tz)
    hour = time.hour + 4
    minute = time.minute


    spended_minutes = ((hour*60)+minute)-((8*60)+30)

    # Check if school is open in that TIME
    if ((spended_minutes > seventh_rest[1]) or (spended_minutes < first_class[0])):
        info_dict = {}
        info_dict["wichest"] = "Ավարտ"
        info_dict["type"] = "Ավարտ"
        info_dict["spend_time"] = 0
        info_dict["left_time"] = 0
        info_dict["spended_minutes"] = spended_minutes
        return info_dict

    # First class or rest check
    elif ((spended_minutes >= first_class[0]) and (spended_minutes <= first_class[1])):
        info_dict = {}
        info_dict["wichest"] = "Առաջին"
        info_dict["type"] = "դաս"                               
        info_dict["spend_time"] = spended_minutes-first_class[0]
        info_dict["left_time"] = first_class[1]-spended_minutes
        info_dict["spended_minutes"] = spended_minutes
        return info_dict
    elif ((spended_minutes > first_rest[0]) and (spended_minutes < first_rest[1])):
        info_dict = {}
        info_dict["wichest"] = "Առաջին"
        info_dict["type"] = "դասամիջոց"
        info_dict["spend_time"] = spended_minutes-first_rest[0]                          
        info_dict["left_time"] = first_rest[1]-spended_minutes
        info_dict["spended_minutes"] = spended_minutes
        return info_dict

    # Second class or rest check
    elif ((spended_minutes >= second_class[0]) and (spended_minutes <= second_class[1])):
        info_dict = {}
        info_dict["wichest"] = "Երկրորդ"
        info_dict["type"] = "դաս"                                          
        info_dict["spend_time"] = spended_minutes- second_class[0]        
        info_dict["left_time"] = second_class[1]-spended_minutes
        info_dict["spended_minutes"] = spended_minutes
        return info_dict
    elif ((spended_minutes > second_rest[0]) and (spended_minutes < second_rest[1])):
        info_dict = {}
        info_dict["wichest"] = "Երկրորդ"
        info_dict["type"] = "դասամիջոց"
        info_dict["spend_time"] = spended_minutes-second_rest[0]
        info_dict["left_time"] = second_rest[1]-spended_minutes
        info_dict["spended_minutes"] = spended_minutes
        return info_dict

    # Third class or rest check
    elif ((spended_minutes >= third_class[0]) and (spended_minutes <= third_class[1])):
        info_dict = {}
        info_dict["wichest"] = "Երրորդ"
        info_dict["type"] = "դաս"
        info_dict["spend_time"] = spended_minutes-third_class[0]
        info_dict["left_time"] = third_class[1]-spended_minutes
        info_dict["spended_minutes"] = spended_minutes
        return info_dict
    elif ((spended_minutes > third_rest[0]) and (spended_minutes < third_rest[1])):
        info_dict = {}
        info_dict["wichest"] = "Երրորդ"
        info_dict["type"] = "դասամիջոց"
        info_dict["spend_time"] = spended_minutes-third_rest[0]
        info_dict["left_time"] = third_rest[1]-spended_minutes
        info_dict["spended_minutes"] = spended_minutes
        return info_dict

    # Fourth class or rest check
    elif ((spended_minutes >= fourth_class[0]) and (spended_minutes <= fourth_class[1])):
        info_dict = {}
        info_dict["wichest"] = "Չորրորդ"
        info_dict["type"] = "դաս"
        info_dict["spend_time"] = spended_minutes-fourth_class[0]
        info_dict["left_time"] = fourth_class[1]-spended_minutes
        info_dict["spended_minutes"] = spended_minutes
        return info_dict
    elif ((spended_minutes > fourth_rest[0]) and (spended_minutes < fourth_rest[1])):
        info_dict = {}
        info_dict["wichest"] = "Չորրորդ"
        info_dict["type"] = "դասամիջոց"
        info_dict["spend_time"] = spended_minutes-fourth_rest[0]
        info_dict["left_time"] = fourth_rest[1]-spended_minutes
        info_dict["spended_minutes"] = spended_minutes
        return info_dict

    # Fifth class or rest check
    elif ((spended_minutes >= fifth_class[0]) and (spended_minutes <= fifth_class[1])):                                                        
        info_dict = {}
        info_dict["wichest"] = "Հինգերորդ"
        info_dict["type"] = "դաս"
        info_dict["spend_time"] = spended_minutes-fifth_class[0]
        info_dict["left_time"] = fifth_class[1]-spended_minutes
        info_dict["spended_minutes"] = spended_minutes
        return info_dict
    elif ((spended_minutes > fifth_rest[0]) and (spended_minutes < fifth_rest[1])):
        info_dict = {}
        info_dict["wichest"] = "Հինգերորդ"
        info_dict["type"] = "դասամիջոց"
        info_dict["spend_time"] = spended_minutes-fifth_rest[0]
        info_dict["left_time"] = fifth_rest[1]-spended_minutes
        info_dict["spended_minutes"] = spended_minutes
        return info_dict

    # Sixth class or rest check
    elif ((spended_minutes >= sixth_class[0]) and (spended_minutes <= sixth_class[1])):
        info_dict = {}
        info_dict["wichest"] = "Վեցերորդ"
        info_dict["type"] = "դաս"
        info_dict["spend_time"] = spended_minutes-sixth_class[0]
        info_dict["left_time"] = sixth_class[1]-spended_minutes
        info_dict["spended_minutes"] = spended_minutes
        return info_dict
    elif ((spended_minutes > sixth_rest[0]) and (spended_minutes < sixth_rest[1])):
        info_dict = {}
        info_dict["wichest"] = "Վեցերորդ"
        info_dict["type"] = "դասամիջոց"
        info_dict["spend_time"] = spended_minutes-sixth_rest[0]
        info_dict["left_time"] = sixth_rest[1]-spended_minutes
        info_dict["spended_minutes"] = spended_minutes
        return info_dict
    
    # Seventh class or rest check
    elif ((spended_minutes >= seventh_class[0]) and (spended_minutes <= seventh_class[1])):
        info_dict = {}
        info_dict["wichest"] = "Յոթերորդ"
        info_dict["type"] = "դաս"
        info_dict["spend_time"] = spended_minutes-seventh_class[0]
        info_dict["left_time"] = seventh_class[1]-spended_minutes
        info_dict["spended_minutes"] = spended_minutes
        return info_dict
    elif ((spended_minutes > seventh_rest[0]) and (spended_minutes < seventh_rest[1])):
        info_dict = {}
        info_dict["wichest"] = "Յոթերորդ"
        info_dict["type"] = "դասամիջոց"
        info_dict["spend_time"] = spended_minutes-seventh_rest[0]
        info_dict["left_time"] = seventh_rest[1]-spended_minutes
        info_dict["spended_minutes"] = spended_minutes
        return info_dict
