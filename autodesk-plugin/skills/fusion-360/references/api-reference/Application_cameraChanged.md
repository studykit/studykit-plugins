# Application.cameraChanged Event

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

The cameraChanged event fires immediately after a change in the camera has been made. Camera changes happen when user changes the view by rotating, zooming in or out, panning, changing from parallel to perspective, or when the extents of the viewport changes.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* ```` ``` # Import fusion360utils folder, which includes event_utils.py. from ...lib import fusion360utils as futil ``` ```` *-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. local_handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "application_var" is a variable referencing an Application object. # "application_cameraChanged" is the event handler function. futil.add_handler(application_var.cameraChanged, application_cameraChanged, local_handlers=local_handlers) ``` ```` *-------- Event handler function definition ---------* ```` ``` # Event handler for the cameraChanged event. def application_cameraChanged(args: adsk.core.CameraEventArgs):     # Code to react to the event.     app.log('In application_cameraChanged event handler.') ``` ```` |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "application_var" is a variable referencing an Application object. # "MyCameraChangedHandler" is the name of the class that handles the event. onCameraChanged = MyCameraChangedHandler() application_var.cameraChanged.add(onCameraChanged) handlers.append(onCameraChanged) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the cameraChanged event. class MyCameraChangedHandler(adsk.core.CameraEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.CameraEventArgs):         # Code to react to the event.         app.log('In MyCameraChangedHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/Application/Application.h> #include <Core/Application/CameraEvent.h> #include <Core/Application/CameraEventHandler.h> #include <Core/Application/CameraEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the cameraChanged event. ``` ````* class MyCameraChangedEventHandler : public adsk::core::CameraEventHandler { public:  void notify(const Ptr<CameraEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyCameraChangedEventHandler event handler.");  } } \_cameraChanged;  *--------- Connect the handler to the event. ---------* ```` ``` // "application_var" is a variable referencing an Application object. // Connect the handler function to the event. Ptr<CameraEvent> cameraChangedEvent = application_var->cameraChanged(); if (!cameraChangedEvent)     return;  bool isOk = cameraChangedEvent->add(&_cameraChanged); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [CameraEvent](CameraEvent.htm).

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |