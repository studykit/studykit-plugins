# Application.documentOpened Event

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

The DocumentOpened event fires at the VERY end of a document being opened so the Document object is available to be used.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* ```` ``` # Import fusion360utils folder, which includes event_utils.py. from ...lib import fusion360utils as futil ``` ```` *-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. local_handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "application_var" is a variable referencing an Application object. # "application_documentOpened" is the event handler function. futil.add_handler(application_var.documentOpened, application_documentOpened, local_handlers=local_handlers) ``` ```` *-------- Event handler function definition ---------* ```` ``` # Event handler for the documentOpened event. def application_documentOpened(args: adsk.core.DocumentEventArgs):     # Code to react to the event.     app.log('In application_documentOpened event handler.') ``` ```` |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "application_var" is a variable referencing an Application object. # "MyDocumentOpenedHandler" is the name of the class that handles the event. onDocumentOpened = MyDocumentOpenedHandler() application_var.documentOpened.add(onDocumentOpened) handlers.append(onDocumentOpened) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the documentOpened event. class MyDocumentOpenedHandler(adsk.core.DocumentEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.DocumentEventArgs):         # Code to react to the event.         app.log('In MyDocumentOpenedHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/Application/Application.h> #include <Core/Application/DocumentEvent.h> #include <Core/Application/DocumentEventHandler.h> #include <Core/Application/DocumentEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the documentOpened event. ``` ````* class MyDocumentOpenedEventHandler : public adsk::core::DocumentEventHandler { public:  void notify(const Ptr<DocumentEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyDocumentOpenedEventHandler event handler.");  } } \_documentOpened;  *--------- Connect the handler to the event. ---------* ```` ``` // "application_var" is a variable referencing an Application object. // Connect the handler function to the event. Ptr<DocumentEvent> documentOpenedEvent = application_var->documentOpened(); if (!documentOpenedEvent)     return;  bool isOk = documentOpenedEvent->add(&_documentOpened); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [DocumentEvent](DocumentEvent.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |