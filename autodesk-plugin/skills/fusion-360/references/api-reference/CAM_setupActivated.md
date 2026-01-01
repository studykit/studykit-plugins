# CAM.setupActivated Event

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

The SetupActivated event fires when a setup is activated.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "cAM_var" is a variable referencing a CAM object. # "MySetupActivatedHandler" is the name of the class that handles the event. onSetupActivated = MySetupActivatedHandler() cAM_var.setupActivated.add(onSetupActivated) handlers.append(onSetupActivated) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the setupActivated event. class MySetupActivatedHandler(adsk.cam.SetupEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.cam.SetupEventArgs):         # Code to react to the event.         app.log('In MySetupActivatedHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Cam/CAM/CAM.h> #include <Cam/CAM/SetupEvent.h> #include <Cam/CAM/SetupEventHandler.h> #include <Cam/CAM/SetupEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the setupActivated event. ``` ````* class MySetupActivatedEventHandler : public adsk::cam::SetupEventHandler { public:  void notify(const Ptr<SetupEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MySetupActivatedEventHandler event handler.");  } } \_setupActivated;  *--------- Connect the handler to the event. ---------* ```` ``` // "cAM_var" is a variable referencing a CAM object. // Connect the handler function to the event. Ptr<SetupEvent> setupActivatedEvent = cAM_var->setupActivated(); if (!setupActivatedEvent)     return;  bool isOk = setupActivatedEvent->add(&_setupActivated); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [SetupEvent](SetupEvent.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |