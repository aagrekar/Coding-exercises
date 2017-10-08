def calc_area(x,y,vx1,vy1,vx2,vy2):
    a = ((x-vx1)**2+(y-vy1)**2)**0.5
    b = ((x-vx2)**2+(y-vy2)**2)**0.5
    c = ((vx2-vx1)**2+(vy2-vy1)**2)**0.5
    s = (a+b+c)/2
    
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    return round(area,4)

def find_min_point(x1,y1,x2,y2,x3,y3):
    points_distance = dict()
    for x in range(min(x1,x2,x3),max(x1,x2,x3)+1):
        for y in range(min(y1,y2,y3),max(y1,y2,y3)+1):
            coord = (x,y)
            print(coord)
            a1 = calc_area(x,y,x1,y1,x2,y2)
            a2 = calc_area(x,y,x1,y1,x3,y3)
            a3 = calc_area(x,y,x2,y2,x3,y3)
            a = calc_area(x1,y1,x2,y2,x3,y3)
            print(a1+a2+a3)
            print(a)
            if a1+a2+a3 == a:
                dist = (x-x1)**2 + (y-y1)**2 + (x-x2)**2 + (y-y2)**2 + (x-x3)**2 + (y-y3)**2
                points_distance.update({(x,y):dist})
            
    points_distance = sorted(points_distance.items(),key = lambda x:(x[1],x[0][0],x[0][1])
    print(points_distance)
    if len(points_distance)>=1:
        return [coord for coord in points_distance[0][0]]
    else:
        return [None, None]
        
print(find_min_point(0,0,2,0,1,2))
