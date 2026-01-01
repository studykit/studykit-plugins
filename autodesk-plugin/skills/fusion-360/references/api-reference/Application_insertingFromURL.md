# Application.insertingFromURL Event

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

The insertingFromURL event fires when the user has clicked a link in a web page that uses the Fusion protocol handler to insert a file as new component. This event is fired at the beginning of the request but before Fusion has take any action so that it's still possible to cancel the operation.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "application_var" is a variable referencing an Application object. # "MyInsertingFromURLHandler" is the name of the class that handles the event. onInsertingFromURL = MyInsertingFromURLHandler() application_var.insertingFromURL.add(onInsertingFromURL) handlers.append(onInsertingFromURL) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the insertingFromURL event. class MyInsertingFromURLHandler(adsk.core.WebRequestEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.WebRequestEventArgs):         # Code to react to the event.         app.log('In MyInsertingFromURLHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/Application/Application.h> #include <Core/Application/WebRequestEvent.h> #include <Core/Application/WebRequestEventHandler.h> #include <Core/Application/WebRequestEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the insertingFromURL event. ``` ````* class MyInsertingFromURLEventHandler : public adsk::core::WebRequestEventHandler { public:  void notify(const Ptr<WebRequestEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyInsertingFromURLEventHandler event handler.");  } } \_insertingFromURL;  *--------- Connect the handler to the event. ---------* ```` ``` // "application_var" is a variable referencing an Application object. // Connect the handler function to the event. Ptr<WebRequestEvent> insertingFromURLEvent = application_var->insertingFromURL(); if (!insertingFromURLEvent)     return;  bool isOk = insertingFromURLEvent->add(&_insertingFromURL); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [WebRequestEvent](WebRequestEvent.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |