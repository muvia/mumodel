import bpy

_sceneName = "Scene"
_scene = bpy.data.scenes[_sceneName] 

#THIS IS another version of render strip. it uses the "Animation" button
#to let Blender render the whole strip, instead of rendering each one.
def renderStripAnim(prefix, frameini, frameend, framestep):
    print("-------------------------------------------")
    _scene.frame_start = frameini
    _scene.frame_end = frameend
    _scene.frame_step = framestep
    _scene.render.filepath = "//render/"+prefix + "/"
    _scene.spritesheet.filepath = _scene.render.filepath + prefix + "_sprite.png"
    bpy.ops.render.render(animation=True)
    bpy.ops.render.spritify()

def renderAllStripAnim(prefix, frameini, frameend, framestep):
    _scene.camera = bpy.data.objects["CameraFront"]
    renderStripAnim(prefix+"_front", frameini, frameend, framestep)
    _scene.camera = bpy.data.objects["CameraRight"]
    renderStripAnim(prefix+"_right", frameini, frameend, framestep)
    _scene.camera = bpy.data.objects["CameraLeft"]
    renderStripAnim(prefix+"_left", frameini, frameend, framestep)
    _scene.camera = bpy.data.objects["CameraBack"]
    renderStripAnim(prefix+"_back", frameini, frameend, framestep)
        

renderAllStripAnim("side_walk", 1, 8, 1)
    
