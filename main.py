import math

screen_width = 24
screen_height = 24

theta_spacing = 0.07
phi_spacing = 0.02

R1 = 1
R2 = 2
K2 = 5
K1 = screen_width * K2 * 3 / (8 * (R1 + R2))


def render_frame(A, B):
    output = [[' ' for _ in range(screen_height)] for _ in range(screen_width)]
    zbuffer = [[0 for _ in range(screen_height)] for _ in range(screen_width)]

    num_theta_steps = int(2 * math.pi / theta_spacing)
    num_phi_steps = int(2 * math.pi / phi_spacing)

    for i in range(num_theta_steps):
        theta = i * theta_spacing
        costheta = math.cos(theta)
        sintheta = math.sin(theta)

        for j in range(num_phi_steps):
            phi = j * phi_spacing
            cosphi = math.cos(phi)
            sinphi = math.sin(phi)

            circlex = R2 + R1 * costheta
            circley = R1 * sintheta

            x = circlex * (math.cos(B) * cosphi + math.sin(A) * math.sin(B) * sinphi) - circley * math.cos(
                A) * math.sin(B)
            y = circlex * (math.sin(B) * cosphi - math.sin(A) * math.cos(B) * sinphi) + circley * math.cos(
                A) * math.cos(B)
            z = K2 + math.cos(A) * circlex * sinphi + circley * math.sin(A)
            ooz = 1 / z

            xp = int(screen_width / 2 + K1 * ooz * x)
            yp = int(screen_height / 2 - K1 * ooz * y)

            # Check if projected coordinates are within bounds
            if 0 <= xp < screen_width and 0 <= yp < screen_height:
                L = cosphi * costheta * math.sin(B) - math.cos(A) * costheta * sinphi - math.sin(
                    A) * sintheta + math.cos(B) * (math.cos(A) * sintheta - costheta * math.sin(A) * sinphi)

                if L > 0:
                    if ooz > zbuffer[xp][yp]:
                        zbuffer[xp][yp] = ooz
                        luminance_index = int(L * 8)
                        output[xp][yp] = ".,-~:;=!*#$@"[luminance_index]

    for j in range(screen_height):
        print("".join(output[i][j] for i in range(screen_width)))


if __name__ == "__main__":
    for i in range(100000000000):
        render_frame(i * 0.03, i * 0.1)