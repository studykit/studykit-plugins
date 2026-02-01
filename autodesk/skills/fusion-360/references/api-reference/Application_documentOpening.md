# Application.documentOpening Event

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

The DocumentOpening event fires at the VERY start of a document being opened. There is no promise that the document will be opened, hence a documentOpened event may not follow.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* ```` ``` # Import fusion360utils folder, which includes event_utils.py. from ...lib import fusion360utils as futil ``` ```` *-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. local_handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "application_var" is a variable referencing an Application object. # "application_documentOpening" is the event handler function. futil.add_handler(application_var.documentOpening, application_documentOpening, local_handlers=local_handlers) ``` ```` *-------- Event handler function definition ---------* ```` ``` # Event handler for the documentOpening event. def application_documentOpening(args: adsk.core.DocumentEventArgs):     # Code to react to the event.     app.log('In application_documentOpening event handler.') ``` ```` |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "application_var" is a variable referencing an Application object. # "MyDocumentOpeningHandler" is the name of the class that handles the event. onDocumentOpening = MyDocumentOpeningHandler() application_var.documentOpening.add(onDocumentOpening) handlers.append(onDocumentOpening) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the documentOpening event. class MyDocumentOpeningHandler(adsk.core.DocumentEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.DocumentEventArgs):         # Code to react to the event.         app.log('In MyDocumentOpeningHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/Application/Application.h> #include <Core/Application/DocumentEvent.h> #include <Core/Application/DocumentEventHandler.h> #include <Core/Application/DocumentEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the documentOpening event. ``` ````* class MyDocumentOpeningEventHandler : public adsk::core::DocumentEventHandler { public:  void notify(const Ptr<DocumentEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyDocumentOpeningEventHandler event handler.");  } } \_documentOpening;  *--------- Connect the handler to the event. ---------* ```` ``` // "application_var" is a variable referencing an Application object. // Connect the handler function to the event. Ptr<DocumentEvent> documentOpeningEvent = application_var->documentOpening(); if (!documentOpeningEvent)     return;  bool isOk = documentOpeningEvent->add(&_documentOpening); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [DocumentEvent](DocumentEvent.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |