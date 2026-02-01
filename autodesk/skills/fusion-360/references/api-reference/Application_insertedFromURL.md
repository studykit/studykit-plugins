# Application.insertedFromURL Event

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

The insertedFromURL event fires after the user has clicked a link in a web page that uses the Fusion protocol handler to insert a file as new component and that operation has completed.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "application_var" is a variable referencing an Application object. # "MyInsertedFromURLHandler" is the name of the class that handles the event. onInsertedFromURL = MyInsertedFromURLHandler() application_var.insertedFromURL.add(onInsertedFromURL) handlers.append(onInsertedFromURL) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the insertedFromURL event. class MyInsertedFromURLHandler(adsk.core.WebRequestEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.WebRequestEventArgs):         # Code to react to the event.         app.log('In MyInsertedFromURLHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/Application/Application.h> #include <Core/Application/WebRequestEvent.h> #include <Core/Application/WebRequestEventHandler.h> #include <Core/Application/WebRequestEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the insertedFromURL event. ``` ````* class MyInsertedFromURLEventHandler : public adsk::core::WebRequestEventHandler { public:  void notify(const Ptr<WebRequestEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyInsertedFromURLEventHandler event handler.");  } } \_insertedFromURL;  *--------- Connect the handler to the event. ---------* ```` ``` // "application_var" is a variable referencing an Application object. // Connect the handler function to the event. Ptr<WebRequestEvent> insertedFromURLEvent = application_var->insertedFromURL(); if (!insertedFromURLEvent)     return;  bool isOk = insertedFromURLEvent->add(&_insertedFromURL); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [WebRequestEvent](WebRequestEvent.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |