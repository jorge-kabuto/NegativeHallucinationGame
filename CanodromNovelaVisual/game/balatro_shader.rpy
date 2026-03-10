#Use in an image like:
#[screens.rpy] add gui.main_menu_background at balatro_default
#[script.rpy]  scene background_image at balatro_default
transform balatro_default:
    shader "balatro"
    
    # Color control. Order is: outer, inner, transition
    u_color_1 (0.871, 0.267, 0.231, 1.0)
    u_color_2 (0.0, 0.42, 0.706, 1.0)
    u_color_3 (0.086, 0.137, 0.145, 1.0)
    
    # Rotation control
    u_spin_rotation -2.0
    u_spin_speed 7.0
    u_is_rotate False
    u_spin_ease 1.0
    u_spin_amount 0.25
    
    u_offset (0.0,0.0)
    u_contrast 3.5
    u_lighting 0.4
    u_pixel_filter 745.0 # Total pixels. Leave at 99999 to avoid pixelization effect
    
    pause 1.0/60 #Divide by desired framerate
    repeat

# Created by xxidbr9 at https://www.shadertoy.com/view/XXtBRr
# Original by localthunk (https://www.playbalatro.com)
# Renpy version by Jkabuto
init python:
    renpy.register_shader("balatro", variables=
    """
        uniform float u_time;
        uniform vec2 u_drawable_size;
        uniform vec4 u_color_1;
        uniform vec4 u_color_2;
        uniform vec4 u_color_3;
        uniform vec2 u_offset;
        uniform float u_spin_rotation;
        uniform float u_spin_speed;
        uniform float u_contrast;
        uniform float u_lighting;
        uniform float u_spin_amount;
        uniform float u_pixel_filter;
        uniform float u_spin_ease;
        uniform bool u_is_rotate;

        varying vec2 v_tex_coord;
        varying vec2 v_coord;

        attribute vec2 a_tex_coord;

    """, vertex_300="""
        v_tex_coord = a_tex_coord;
        //v_coord = u_drawable_size * vec2(gl_Position.x * .5 + .5, -gl_Position.y * .5 + .5);
        v_coord = vec2(v_tex_coord.x,1.0-v_tex_coord.y) * u_drawable_size;
    """, fragment_300="""
        #define PI 3.14159265359

        vec2 screenSize = u_drawable_size;
        vec2 outer_uv = v_coord/u_drawable_size.xy;
        vec2 screen_coords = outer_uv * u_drawable_size.xy;

        float pixel_size = length(screenSize.xy) / u_pixel_filter;
        vec2 uv = (floor(v_coord.xy*(1./pixel_size))*pixel_size - 0.5*screenSize.xy)/length(screenSize.xy) - u_offset;
        float uv_len = length(uv);
        
        float speed = (u_spin_rotation*u_spin_ease*0.2);
        if(u_is_rotate){
        speed = u_time * speed;
        }
        speed += 302.2;
        float new_pixel_angle = atan(uv.y, uv.x) + speed - u_spin_ease*20.*(1.*u_spin_amount*uv_len + (1. - 1.*u_spin_amount));
        vec2 mid = (screenSize.xy/length(screenSize.xy))/2.;
        uv = (vec2((uv_len * cos(new_pixel_angle) + mid.x), (uv_len * sin(new_pixel_angle) + mid.y)) - mid);
        
        uv *= 30.;
        speed = u_time*(u_spin_speed);
        vec2 uv2 = vec2(uv.x+uv.y);
        
        for(int i=0; i < 5; i++) {
            uv2 += sin(max(uv.x, uv.y)) + uv;
            uv  += 0.5*vec2(cos(5.1123314 + 0.353*uv2.y + speed*0.131121),sin(uv2.x - 0.113*speed));
            uv  -= 1.0*cos(uv.x + uv.y) - 1.0*sin(uv.x*0.711 - uv.y);
        }
        
        float contrast_mod = (0.25*u_contrast + 0.5*u_spin_amount + 1.2);
        float paint_res = min(2., max(0.,length(uv)*(0.035)*contrast_mod));
        float c1p = max(0.,1. - contrast_mod*abs(1.-paint_res));
        float c2p = max(0.,1. - contrast_mod*abs(paint_res));
        float c3p = 1. - min(1., c1p + c2p);
        float light = (u_lighting - 0.2)*max(c1p*5. - 4., 0.) + u_lighting*max(c2p*5. - 4., 0.);
        gl_FragColor = (0.3/u_contrast)*u_color_1 + (1. - 0.3/u_contrast)*(u_color_1*c1p + u_color_2*c2p + vec4(c3p*u_color_3.rgb, c3p*u_color_1.a)) + light;
    """)