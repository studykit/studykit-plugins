# InCanvasRendering.renderComplete Event

Parent Object: [InCanvasRendering](InCanvasRendering.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/InCanvasRendering.h>

## Description

The RenderEvent event fires when the rendering has reached the quality that was specified when the rendering started. This event is only fired when using advanced rendering (the isAdvanced property is True). To save the finished rendering, use the saveImage method.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* ```` ``` # Import fusion360utils folder, which includes event_utils.py. from ...lib import fusion360utils as futil ``` ```` *-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. local_handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "inCanvasRendering_var" is a variable referencing an InCanvasRendering object. # "inCanvasRendering_renderComplete" is the event handler function. futil.add_handler(inCanvasRendering_var.renderComplete, inCanvasRendering_renderComplete, local_handlers=local_handlers) ``` ```` *-------- Event handler function definition ---------* ```` ``` # Event handler for the renderComplete event. def inCanvasRendering_renderComplete(args: adsk.fusion.RenderEventArgs):     # Code to react to the event.     app.log('In inCanvasRendering_renderComplete event handler.') ``` ```` |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "inCanvasRendering_var" is a variable referencing an InCanvasRendering object. # "MyRenderCompleteHandler" is the name of the class that handles the event. onRenderComplete = MyRenderCompleteHandler() inCanvasRendering_var.renderComplete.add(onRenderComplete) handlers.append(onRenderComplete) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the renderComplete event. class MyRenderCompleteHandler(adsk.fusion.RenderEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.fusion.RenderEventArgs):         # Code to react to the event.         app.log('In MyRenderCompleteHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Fusion/Render/InCanvasRendering.h> #include <Fusion/Render/RenderEvent.h> #include <Fusion/Render/RenderEventHandler.h> #include <Fusion/Render/RenderEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the renderComplete event. ``` ````* class MyRenderCompleteEventHandler : public adsk::fusion::RenderEventHandler { public:  void notify(const Ptr<RenderEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyRenderCompleteEventHandler event handler.");  } } \_renderComplete;  *--------- Connect the handler to the event. ---------* ```` ``` // "inCanvasRendering_var" is a variable referencing an InCanvasRendering object. // Connect the handler function to the event. Ptr<RenderEvent> renderCompleteEvent = inCanvasRendering_var->renderComplete(); if (!renderCompleteEvent)     return;  bool isOk = renderCompleteEvent->add(&_renderComplete); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [RenderEvent](RenderEvent.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |