init python:
    
    class TRState(NoRollback):
        def __init__(self):
            self.tex = None
            self.pfp = None
    store.bg_states["TRState"] = TRState()
    
    class TRBackground(renpy.Displayable):

        def __init__(self, child=None, image_path="", **kwargs):
            super(TRBackground, self).__init__(**kwargs)
            self.image_path = image_path

        def render(self, width, height, st, at):
            
            ds = 1.0/1.0
            if store.bg_states["TRState"].tex is None:
                store.bg_states["TRState"].tex = renpy.load_image("images/backgrounds/dark_waters.png")
            if store.bg_states["TRState"].pfp is None:
                store.bg_states["TRState"].pfp = Image(self.image_path)

            buffer_a = renpy.Render(width*ds, height*ds)
            buffer_otl = renpy.Render(width*ds, height*ds)

            pfp_render = renpy.render(store.bg_states["TRState"].pfp, 1000,1000,st,at)
            buffer_otl.blit(pfp_render,(0,0))
            buffer_otl.add_shader("SimpleOutline")
            buffer_otl.add_uniform("u_tex0_size", (width*ds, height*ds))
            buffer_otl.add_uniform("u_radius",20)
            buffer_otl.add_uniform("u_outline_color",(0.2,0.2,1.0))
            buffer_otl.add_uniform("u_should_overlay",True)
            buffer_otl.add_uniform("u_pixel_offset",(0.5,0.125))
            buffer_otl.add_uniform("u_scale",(0.4,0.4)) 

            buffer_a.blit(store.bg_states["TRState"].tex,(0,0))
            buffer_a.add_shader("submerge")
            u = submerge_get_uniforms(st)
            for key, value in u.items():
                buffer_a.add_uniform(key, value)
            
            present = renpy.Render(width, height)

            present.blit(buffer_a,(0,0))
            present.blit(buffer_otl,(0,0))
            renpy.redraw(self, 0)

            return present


label ReflectionIntro:
    default tr_bg = TRBackground(image_path="images/the_reflection_chroma.png")
    scene black
    show expression tr_bg at default_bg

    aaa "Slowly, circumspect neural pathways activate. Your body comes to be."
    aaa "Being, turns out, is pretty rough."
    aaa "You cough violently, your chest jumpstarting a tingling akin to burning."
    aaa "Your eyes open, searing wounds in your face."
    aaa "An enourmous blotch of blue fills your view, although not as dark as before."
    aaa "Catching its shape, you see sharp edges, a perfect prism reflecting potent sunlight."

    aaa "It sits silently. Or rather floats, above coarse and humid sand."
    r "Greetings, new Citizen."
    r "Take your time, this reality can be hard to adjust to for those that have just arrived."
    aaa "Their tone is monotone. They offer no help, although it's unclear how they provide it without limbs."
    aaa "Your breathing steadies, the sharp light becomes more bearable."
    e "...Where am I? What are you supposed to be?"
    aaa "Their surface ripples slightly, its pond-like surface disturbed, but not broken."
    r "All your questions will be answered in time, Citizen."
    r "I am The Reflection, they who orders the world. It is my duty to make sense of this world, imagined as it may be."
    
    # menu(nvl=True):
    #     "And what are you supposed to reflect?":
    #     "What do you even mean by imagined? That felt terrifyingly *real*":
    #     "I almost died here!! And you did nothing at all to help me!":
    #     "*Kick their shiny back-bottom*":
    jump DEBUG_MENU