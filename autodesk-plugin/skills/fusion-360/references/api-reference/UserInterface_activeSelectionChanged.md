# UserInterface.activeSelectionChanged Event

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

This event fires whenever the contents of the active selection changes. This occurs as the user selects or unselects entities while using the Fusion Select command. The Select command is the default command that is always running if no other command is active. Pressing Escape terminates the currently active command and starts the Select command. If the Select command is running and you press Escape, it terminates the current Select command and starts a new one.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* ```` ``` # Import fusion360utils folder, which includes event_utils.py. from ...lib import fusion360utils as futil ``` ```` *-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. local_handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "userInterface_var" is a variable referencing a UserInterface object. # "userInterface_activeSelectionChanged" is the event handler function. futil.add_handler(userInterface_var.activeSelectionChanged, userInterface_activeSelectionChanged, local_handlers=local_handlers) ``` ```` *-------- Event handler function definition ---------* ```` ``` # Event handler for the activeSelectionChanged event. def userInterface_activeSelectionChanged(args: adsk.core.ActiveSelectionEventArgs):     # Code to react to the event.     app.log('In userInterface_activeSelectionChanged event handler.') ``` ```` |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "userInterface_var" is a variable referencing a UserInterface object. # "MyActiveSelectionChangedHandler" is the name of the class that handles the event. onActiveSelectionChanged = MyActiveSelectionChangedHandler() userInterface_var.activeSelectionChanged.add(onActiveSelectionChanged) handlers.append(onActiveSelectionChanged) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the activeSelectionChanged event. class MyActiveSelectionChangedHandler(adsk.core.ActiveSelectionEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.ActiveSelectionEventArgs):         # Code to react to the event.         app.log('In MyActiveSelectionChangedHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/UserInterface.h> #include <Core/UserInterface/ActiveSelectionEvent.h> #include <Core/UserInterface/ActiveSelectionEventHandler.h> #include <Core/UserInterface/ActiveSelectionEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the activeSelectionChanged event. ``` ````* class MyActiveSelectionChangedEventHandler : public adsk::core::ActiveSelectionEventHandler { public:  void notify(const Ptr<ActiveSelectionEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyActiveSelectionChangedEventHandler event handler.");  } } \_activeSelectionChanged;  *--------- Connect the handler to the event. ---------* ```` ``` // "userInterface_var" is a variable referencing a UserInterface object. // Connect the handler function to the event. Ptr<ActiveSelectionEvent> activeSelectionChangedEvent = userInterface_var->activeSelectionChanged(); if (!activeSelectionChangedEvent)     return;  bool isOk = activeSelectionChangedEvent->add(&_activeSelectionChanged); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns an [ActiveSelectionEvent](ActiveSelectionEvent.htm).

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |