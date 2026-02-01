# UserInterface.workspaceActivated Event

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

The workspaceActivated event fires at the VERY end of a workspace being activated. The client can add or remove WorkspaceEventHandlers from the WorkspaceEvent.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "userInterface_var" is a variable referencing a UserInterface object. # "MyWorkspaceActivatedHandler" is the name of the class that handles the event. onWorkspaceActivated = MyWorkspaceActivatedHandler() userInterface_var.workspaceActivated.add(onWorkspaceActivated) handlers.append(onWorkspaceActivated) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the workspaceActivated event. class MyWorkspaceActivatedHandler(adsk.core.WorkspaceEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.WorkspaceEventArgs):         # Code to react to the event.         app.log('In MyWorkspaceActivatedHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/UserInterface.h> #include <Core/UserInterface/WorkspaceEvent.h> #include <Core/UserInterface/WorkspaceEventHandler.h> #include <Core/UserInterface/WorkspaceEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the workspaceActivated event. ``` ````* class MyWorkspaceActivatedEventHandler : public adsk::core::WorkspaceEventHandler { public:  void notify(const Ptr<WorkspaceEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyWorkspaceActivatedEventHandler event handler.");  } } \_workspaceActivated;  *--------- Connect the handler to the event. ---------* ```` ``` // "userInterface_var" is a variable referencing a UserInterface object. // Connect the handler function to the event. Ptr<WorkspaceEvent> workspaceActivatedEvent = userInterface_var->workspaceActivated(); if (!workspaceActivatedEvent)     return;  bool isOk = workspaceActivatedEvent->add(&_workspaceActivated); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [WorkspaceEvent](WorkspaceEvent.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |