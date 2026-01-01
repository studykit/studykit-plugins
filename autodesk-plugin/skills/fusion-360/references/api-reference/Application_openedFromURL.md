# Application.openedFromURL Event

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

The openedFromURL event fires after the user has clicked a link in a web page that uses the Fusion protocol handler to create a new using an existing file as the initial contents and that operation has completed.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "application_var" is a variable referencing an Application object. # "MyOpenedFromURLHandler" is the name of the class that handles the event. onOpenedFromURL = MyOpenedFromURLHandler() application_var.openedFromURL.add(onOpenedFromURL) handlers.append(onOpenedFromURL) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the openedFromURL event. class MyOpenedFromURLHandler(adsk.core.WebRequestEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.WebRequestEventArgs):         # Code to react to the event.         app.log('In MyOpenedFromURLHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/Application/Application.h> #include <Core/Application/WebRequestEvent.h> #include <Core/Application/WebRequestEventHandler.h> #include <Core/Application/WebRequestEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the openedFromURL event. ``` ````* class MyOpenedFromURLEventHandler : public adsk::core::WebRequestEventHandler { public:  void notify(const Ptr<WebRequestEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyOpenedFromURLEventHandler event handler.");  } } \_openedFromURL;  *--------- Connect the handler to the event. ---------* ```` ``` // "application_var" is a variable referencing an Application object. // Connect the handler function to the event. Ptr<WebRequestEvent> openedFromURLEvent = application_var->openedFromURL(); if (!openedFromURLEvent)     return;  bool isOk = openedFromURLEvent->add(&_openedFromURL); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [WebRequestEvent](WebRequestEvent.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |