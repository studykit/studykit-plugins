# CAM.setupChanged Event

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

The SetupChanged event fires when a setup is modified.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "cAM_var" is a variable referencing a CAM object. # "MySetupChangedHandler" is the name of the class that handles the event. onSetupChanged = MySetupChangedHandler() cAM_var.setupChanged.add(onSetupChanged) handlers.append(onSetupChanged) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the setupChanged event. class MySetupChangedHandler(adsk.cam.SetupChangeEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.cam.SetupChangeEventArgs):         # Code to react to the event.         app.log('In MySetupChangedHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Cam/CAM/CAM.h> #include <Cam/CAM/SetupChangeEvent.h> #include <Cam/CAM/SetupChangeEventHandler.h> #include <Cam/CAM/SetupChangeEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the setupChanged event. ``` ````* class MySetupChangedEventHandler : public adsk::cam::SetupChangeEventHandler { public:  void notify(const Ptr<SetupChangeEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MySetupChangedEventHandler event handler.");  } } \_setupChanged;  *--------- Connect the handler to the event. ---------* ```` ``` // "cAM_var" is a variable referencing a CAM object. // Connect the handler function to the event. Ptr<SetupChangeEvent> setupChangedEvent = cAM_var->setupChanged(); if (!setupChangedEvent)     return;  bool isOk = setupChangedEvent->add(&_setupChanged); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [SetupChangeEvent](SetupChangeEvent.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |