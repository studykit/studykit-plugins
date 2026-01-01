# HttpRequest.completed Event

Parent Object: [HttpRequest](HttpRequest.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpRequest.h>

## Description

The completed event fires when the request has completed. This event will fire on successful or failure.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "httpRequest_var" is a variable referencing a HttpRequest object. # "MyCompletedHandler" is the name of the class that handles the event. onCompleted = MyCompletedHandler() httpRequest_var.completed.add(onCompleted) handlers.append(onCompleted) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the completed event. class MyCompletedHandler(adsk.core.HttpEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.HttpEventArgs):         # Code to react to the event.         app.log('In MyCompletedHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/Application/HttpRequest.h> #include <Core/Application/HttpEvent.h> #include <Core/Application/HttpEventHandler.h> #include <Core/Application/HttpEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the completed event. ``` ````* class MyCompletedEventHandler : public adsk::core::HttpEventHandler { public:  void notify(const Ptr<HttpEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyCompletedEventHandler event handler.");  } } \_completed;  *--------- Connect the handler to the event. ---------* ```` ``` // "httpRequest_var" is a variable referencing a HttpRequest object. // Connect the handler function to the event. Ptr<HttpEvent> completedEvent = httpRequest_var->completed(); if (!completedEvent)     return;  bool isOk = completedEvent->add(&_completed); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [HttpEvent](HttpEvent.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |