# UserInterface.workspaceDeactivated Event

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

The workspaceDeactivated event fires at the VERY end of a workspace being deactivated. The client can add or remove WorkspaceEventHandlers from the WorkspaceEvent.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "userInterface_var" is a variable referencing a UserInterface object. # "MyWorkspaceDeactivatedHandler" is the name of the class that handles the event. onWorkspaceDeactivated = MyWorkspaceDeactivatedHandler() userInterface_var.workspaceDeactivated.add(onWorkspaceDeactivated) handlers.append(onWorkspaceDeactivated) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the workspaceDeactivated event. class MyWorkspaceDeactivatedHandler(adsk.core.WorkspaceEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.WorkspaceEventArgs):         # Code to react to the event.         app.log('In MyWorkspaceDeactivatedHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/UserInterface.h> #include <Core/UserInterface/WorkspaceEvent.h> #include <Core/UserInterface/WorkspaceEventHandler.h> #include <Core/UserInterface/WorkspaceEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the workspaceDeactivated event. ``` ````* class MyWorkspaceDeactivatedEventHandler : public adsk::core::WorkspaceEventHandler { public:  void notify(const Ptr<WorkspaceEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyWorkspaceDeactivatedEventHandler event handler.");  } } \_workspaceDeactivated;  *--------- Connect the handler to the event. ---------* ```` ``` // "userInterface_var" is a variable referencing a UserInterface object. // Connect the handler function to the event. Ptr<WorkspaceEvent> workspaceDeactivatedEvent = userInterface_var->workspaceDeactivated(); if (!workspaceDeactivatedEvent)     return;  bool isOk = workspaceDeactivatedEvent->add(&_workspaceDeactivated); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [WorkspaceEvent](WorkspaceEvent.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |