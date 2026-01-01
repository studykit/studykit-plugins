# Application.openingFromURL Event

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

The openingFromURL event fires when the user has clicked a link in a web page that uses the Fusion protocol handler to create a new file using an existing file as the initial contents. This event is fired at the beginning of the request but before Fusion has take any action so that it's still possible to cancel the operation.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "application_var" is a variable referencing an Application object. # "MyOpeningFromURLHandler" is the name of the class that handles the event. onOpeningFromURL = MyOpeningFromURLHandler() application_var.openingFromURL.add(onOpeningFromURL) handlers.append(onOpeningFromURL) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the openingFromURL event. class MyOpeningFromURLHandler(adsk.core.WebRequestEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.WebRequestEventArgs):         # Code to react to the event.         app.log('In MyOpeningFromURLHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/Application/Application.h> #include <Core/Application/WebRequestEvent.h> #include <Core/Application/WebRequestEventHandler.h> #include <Core/Application/WebRequestEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the openingFromURL event. ``` ````* class MyOpeningFromURLEventHandler : public adsk::core::WebRequestEventHandler { public:  void notify(const Ptr<WebRequestEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyOpeningFromURLEventHandler event handler.");  } } \_openingFromURL;  *--------- Connect the handler to the event. ---------* ```` ``` // "application_var" is a variable referencing an Application object. // Connect the handler function to the event. Ptr<WebRequestEvent> openingFromURLEvent = application_var->openingFromURL(); if (!openingFromURLEvent)     return;  bool isOk = openingFromURLEvent->add(&_openingFromURL); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [WebRequestEvent](WebRequestEvent.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |