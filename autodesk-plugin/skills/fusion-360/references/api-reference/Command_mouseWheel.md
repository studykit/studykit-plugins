# Command.mouseWheel Event

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Gets an event that is fired when the mouse wheel is rotated.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "MyMouseWheelHandler" is the name of the class that handles the event. onMouseWheel = MyMouseWheelHandler() command_var.mouseWheel.add(onMouseWheel) handlers.append(onMouseWheel) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the mouseWheel event. class MyMouseWheelHandler(adsk.core.MouseEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.MouseEventArgs):         # Code to react to the event.         app.log('In MyMouseWheelHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/Command.h> #include <Core/UserInterface/MouseEvent.h> #include <Core/UserInterface/MouseEventHandler.h> #include <Core/UserInterface/MouseEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the mouseWheel event. ``` ````* class MyMouseWheelEventHandler : public adsk::core::MouseEventHandler { public:  void notify(const Ptr<MouseEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyMouseWheelEventHandler event handler.");  } } \_mouseWheel;  *--------- Connect the handler to the event. ---------* ```` ``` // "command_var" is a variable referencing a Command object. // Connect the handler function to the event. Ptr<MouseEvent> mouseWheelEvent = command_var->mouseWheel(); if (!mouseWheelEvent)     return;  bool isOk = mouseWheelEvent->add(&_mouseWheel); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [MouseEvent](MouseEvent.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |