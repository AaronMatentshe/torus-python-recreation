Python Torus
Let me walk you through how I re-created the famous 3D rotating torus (donut shape) using ASCII art, focusing  and following the maths behind it.
1. Understanding 3D Projection
To render a 3D object onto a 2D screen, I needed to project points from 3D space to 2D. Starting with a 3D point (x,y,z), I calculated its position on the 2D screen (x′,y′) by using a fixed distance K2from the viewer (at the origin). The projection formula, derived from similar triangles, scales x and y based on their depth z:
x’ = (K1*x)/(z+k2)
y′= (K1*y)/(z+k2)
Here, K1 and K2 are constants I chose to control the size and perspective of the donut. I could tweak these to zoom in or out, or adjust how exaggerated the depth looked.
2. Using a Z-Buffer
To ensure that the closest parts of the donut were drawn on top when plotting points, I used a Z-buffer to track the depth of each pixel. Before plotting a new point, I checked the Z-buffer to see if it was closer than the existing pixel. If it was, I updated the pixel; otherwise, I left it unchanged. This approach made the donut appear more realistic and 3D.
3. Building the Torus (Donut)
Next, I had to actually generate the donut. The torus is essentially a circle rotated around an axis. So I started with a basic 2D circle, with radius R1, centered at (R2,0,0)(R2, 0, 0)(R2,0,0) in 3D space. The coordinates for a point on that circle are:
x=R2+R1⋅cos(θ) 
 y=R1⋅sin(θ)
 z=0
By changing θ from 0 to 2π, I could trace out the circle.
4. Rotating the Circle to Form the Donut
To turn this 2D circle into a 3D torus, I needed to rotate the circle around the y-axis (the vertical axis of the donut) by an angle ϕ. For this, I used a simple rotation matrix:
        cos(ϕ)     0      -sin(ϕ)                                                    
            0            1               0                    
          sin(ϕ)     0      cos(ϕ)                              
Applying this matrix to my circle’s coordinates gave me a full 3D point on the torus:
x=R2+R1⋅cos(θ))⋅cos(ϕ)
y=R1⋅sin(θ)
z=−R2+R1⋅cos(θ))⋅sin(ϕ)
Now, I had a formula for a point on the torus surface, and by sweeping both θ and ϕ, I could generate the entire shape.
5. Animating the Donut
But I didn’t want a static donut; I wanted it to spin! To animate it, I applied additional rotations around the x-axis and z-axis. This involved multiplying the coordinates by more rotation matrices.
For instance, to rotate around the x-axis by an angle A, I used:
        1              0                  0                                         
         0          cos(A)          -sin(A)                                                           
         0          Sin(A)          Cos(A)        
And similarly for the z-axis with angle B. This made the donut rotate smoothly in 3D space.
6. Lighting and Shading
To make the donut look even cooler, I added lighting. For each point on the surface, I calculated its brightness based on how much light was hitting it. To do this, I first had to compute the surface normal at each point — basically, the direction perpendicular to the surface at that point.
Starting with the normal of the circle (cos(θ),sin(θ),0), I applied the same rotations that I used for the points on the torus. This gave me the surface normal at each point.
The lighting came from calculating the dot product of the normal vector with the light direction. I picked the light direction as (0,1,−1), coming from behind and above the viewer. The dot product told me the angle between the surface and the light — a bigger dot product meant more light hit the surface, making it brighter. I mapped the brightness to different ASCII characters like .,-~:;=!*#$@, with darker characters for less light and brighter ones for more light.
7. Projecting and Plotting
Once I had the 3D coordinates of a point and its brightness, I projected it onto the 2D screen using the projection formula I started with:

x’ = (K1*x)/(z+k2)
y′= (K1*y)/(z+k2)

I’d then check the Z-buffer to make sure it wasn’t hidden by something in front, and finally, I’d plot the corresponding ASCII character.
8. The Final Result
After implementing all the math and rotations, I created a spinning ASCII art torus. By adjusting parameters like R1, R2, K1, and K2, I controlled the size, distance, and perspective of the donut, while shading enhanced its 3D appearance.
Translating mathematical formulas into code is a blend of precision and creativity. Though the math behind rendering a torus can seem complex, breaking it down into rotations and projections simplifies the process. Python's straightforward syntax and robust libraries make it an excellent choice for visualizing such shapes.
I must acknowledge that this work is based on Andy Sloane's original C/C++ code. I've adapted his efficient solution into Python, maintaining the underlying principles while making it more accessible for Python users.

"Donut math: how donut.c works" blog post by Andy Sloane”(original work)
https://www.a1k0n.net/2011/07/20/donut-math.html
