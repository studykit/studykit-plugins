# UserInterface.workspacePreActivate Event

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

The workspacePreActivate event fires at the VERY start of a workspace being activated. The client can add or remove WorkspaceEventHandlers from the WorkspaceEvent.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "userInterface_var" is a variable referencing a UserInterface object. # "MyWorkspacePreActivateHandler" is the name of the class that handles the event. onWorkspacePreActivate = MyWorkspacePreActivateHandler() userInterface_var.workspacePreActivate.add(onWorkspacePreActivate) handlers.append(onWorkspacePreActivate) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the workspacePreActivate event. class MyWorkspacePreActivateHandler(adsk.core.WorkspaceEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.WorkspaceEventArgs):         # Code to react to the event.         app.log('In MyWorkspacePreActivateHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/UserInterface.h> #include <Core/UserInterface/WorkspaceEvent.h> #include <Core/UserInterface/WorkspaceEventHandler.h> #include <Core/UserInterface/WorkspaceEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the workspacePreActivate event. ``` ````* class MyWorkspacePreActivateEventHandler : public adsk::core::WorkspaceEventHandler { public:  void notify(const Ptr<WorkspaceEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyWorkspacePreActivateEventHandler event handler.");  } } \_workspacePreActivate;  *--------- Connect the handler to the event. ---------* ```` ``` // "userInterface_var" is a variable referencing a UserInterface object. // Connect the handler function to the event. Ptr<WorkspaceEvent> workspacePreActivateEvent = userInterface_var->workspacePreActivate(); if (!workspacePreActivateEvent)     return;  bool isOk = workspacePreActivateEvent->add(&_workspacePreActivate); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [WorkspaceEvent](WorkspaceEvent.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |