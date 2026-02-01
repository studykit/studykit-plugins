# Command.keyUp Event

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Gets an event that is fired when a key on the keyboard goes up.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "MyKeyUpHandler" is the name of the class that handles the event. onKeyUp = MyKeyUpHandler() command_var.keyUp.add(onKeyUp) handlers.append(onKeyUp) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the keyUp event. class MyKeyUpHandler(adsk.core.KeyboardEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.KeyboardEventArgs):         # Code to react to the event.         app.log('In MyKeyUpHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/Command.h> #include <Core/UserInterface/KeyboardEvent.h> #include <Core/UserInterface/KeyboardEventHandler.h> #include <Core/UserInterface/KeyboardEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the keyUp event. ``` ````* class MyKeyUpEventHandler : public adsk::core::KeyboardEventHandler { public:  void notify(const Ptr<KeyboardEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyKeyUpEventHandler event handler.");  } } \_keyUp;  *--------- Connect the handler to the event. ---------* ```` ``` // "command_var" is a variable referencing a Command object. // Connect the handler function to the event. Ptr<KeyboardEvent> keyUpEvent = command_var->keyUp(); if (!keyUpEvent)     return;  bool isOk = keyUpEvent->add(&_keyUp); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [KeyboardEvent](KeyboardEvent.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |