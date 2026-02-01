# TextCommandPalette.closed Event

Parent Object: [TextCommandPalette](TextCommandPalette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextCommandPalette.h>

## Description

This event is fired when the user clicks the "Close" button on the palette. You can choose if the "Close" button is available or not when you initially create the palette. When a palette is closed, it still exists but is change to invisible so you can still interact with it and retrieve any needed information and can make it visible again. Use the deleteMe method to delete the palette.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "textCommandPalette_var" is a variable referencing a TextCommandPalette object. # "MyClosedHandler" is the name of the class that handles the event. onClosed = MyClosedHandler() textCommandPalette_var.closed.add(onClosed) handlers.append(onClosed) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the closed event. class MyClosedHandler(adsk.core.UserInterfaceGeneralEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.UserInterfaceGeneralEventArgs):         # Code to react to the event.         app.log('In MyClosedHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/TextCommandPalette.h> #include <Core/UserInterface/UserInterfaceGeneralEvent.h> #include <Core/UserInterface/UserInterfaceGeneralEventHandler.h> #include <Core/UserInterface/UserInterfaceGeneralEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the closed event. ``` ````* class MyClosedEventHandler : public adsk::core::UserInterfaceGeneralEventHandler { public:  void notify(const Ptr<UserInterfaceGeneralEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyClosedEventHandler event handler.");  } } \_closed;  *--------- Connect the handler to the event. ---------* ```` ``` // "textCommandPalette_var" is a variable referencing a TextCommandPalette object. // Connect the handler function to the event. Ptr<UserInterfaceGeneralEvent> closedEvent = textCommandPalette_var->closed(); if (!closedEvent)     return;  bool isOk = closedEvent->add(&_closed); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [UserInterfaceGeneralEvent](UserInterfaceGeneralEvent.htm).

## Version

Introduced in version August 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |