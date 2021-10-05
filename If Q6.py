def driver_speed(speed):
    if speed<=70:
        print("ok")
    elif speed>70:
        point=speed-70
        point1=point/5
        if point1<12:
            print("point:",point1)
        else:
            print("license suspended")
    
driver_speed(56)
driver_speed(80)
driver_speed(135)