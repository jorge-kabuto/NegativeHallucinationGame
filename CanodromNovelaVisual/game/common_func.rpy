define prev_was_menu = False
init python:

    # renpy.exports.get_sdl_window_pointer()

    def color(what, color, character, **kwargs):
        renpy.exports.say(None, f"{{color={color}}}{character}{{/color}} — \n" + what, **kwargs)
    
    def tw(what,  **kwargs):
        color(what, "#a50606", "{shader=jitter:(1.5,1.5)}THE TWICE SHADOWED{/shader}", **kwargs)
    def e(what,  **kwargs):
        color(what, "#00bd94", "???", **kwargs)
    
    # def get_default_textshader():
    #     return "typewriter"
    # config.default_textshader = "default"
    # config.textshader_callbacks["default"] = get_default_textshader

    def menu_prev_line(name):

        if renpy.last_say().what is not None and store.prev_was_menu:
            import re
            statement = re.sub("{color.*color}", "", store.last_choice_label)
            preferences.text_cps = 0
            renpy.exports.say(None, "{nw}{color=[youtext]}??? —" + statement + "{/color}")
            preferences.text_cps = 80
            store.prev_was_menu = False

        if renpy.last_say().what is not None and "menu-nvl" in name:
            store.prev_was_menu = True
        
    config.statement_callbacks.append(menu_prev_line)