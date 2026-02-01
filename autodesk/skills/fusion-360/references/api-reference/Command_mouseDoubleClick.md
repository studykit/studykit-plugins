# Command.mouseDoubleClick Event

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Gets an event that is fired when the mouse is double-clicked, (clicked twice within the time specified by a system setting.)

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "MyMouseDoubleClickHandler" is the name of the class that handles the event. onMouseDoubleClick = MyMouseDoubleClickHandler() command_var.mouseDoubleClick.add(onMouseDoubleClick) handlers.append(onMouseDoubleClick) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the mouseDoubleClick event. class MyMouseDoubleClickHandler(adsk.core.MouseEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.MouseEventArgs):         # Code to react to the event.         app.log('In MyMouseDoubleClickHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/Command.h> #include <Core/UserInterface/MouseEvent.h> #include <Core/UserInterface/MouseEventHandler.h> #include <Core/UserInterface/MouseEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the mouseDoubleClick event. ``` ````* class MyMouseDoubleClickEventHandler : public adsk::core::MouseEventHandler { public:  void notify(const Ptr<MouseEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyMouseDoubleClickEventHandler event handler.");  } } \_mouseDoubleClick;  *--------- Connect the handler to the event. ---------* ```` ``` // "command_var" is a variable referencing a Command object. // Connect the handler function to the event. Ptr<MouseEvent> mouseDoubleClickEvent = command_var->mouseDoubleClick(); if (!mouseDoubleClickEvent)     return;  bool isOk = mouseDoubleClickEvent->add(&_mouseDoubleClick); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [MouseEvent](MouseEvent.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |