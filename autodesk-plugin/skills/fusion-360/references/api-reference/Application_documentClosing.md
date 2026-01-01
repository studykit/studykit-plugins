# Application.documentClosing Event

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

The DocumentClosing event fires at the VERY start of a document being closed. User can set the isSaveCanceled property of DocumentEventArgs to true to cancel the document close.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "application_var" is a variable referencing an Application object. # "MyDocumentClosingHandler" is the name of the class that handles the event. onDocumentClosing = MyDocumentClosingHandler() application_var.documentClosing.add(onDocumentClosing) handlers.append(onDocumentClosing) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the documentClosing event. class MyDocumentClosingHandler(adsk.core.DocumentEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.DocumentEventArgs):         # Code to react to the event.         app.log('In MyDocumentClosingHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/Application/Application.h> #include <Core/Application/DocumentEvent.h> #include <Core/Application/DocumentEventHandler.h> #include <Core/Application/DocumentEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the documentClosing event. ``` ````* class MyDocumentClosingEventHandler : public adsk::core::DocumentEventHandler { public:  void notify(const Ptr<DocumentEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyDocumentClosingEventHandler event handler.");  } } \_documentClosing;  *--------- Connect the handler to the event. ---------* ```` ``` // "application_var" is a variable referencing an Application object. // Connect the handler function to the event. Ptr<DocumentEvent> documentClosingEvent = application_var->documentClosing(); if (!documentClosingEvent)     return;  bool isOk = documentClosingEvent->add(&_documentClosing); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [DocumentEvent](DocumentEvent.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Application Event API Sample](ApplicationEventSample_Sample.htm) | Add-In that demonstrates application events. To use this sample, create a new folder using the name you want to use for the new add-in. Inside the folder, create a new file that is the same name as the folder but has a .py extension. Copy the code below into the .py file. Create another file that is the same name as the folder but has a .manifest extension and copy the JSON data below into that file. { "autodeskProduct": "Fusion360", "type": "addin", "author": "", "description": { "": "" }, "supportedOS": "windows|mac", "editEnabled": true } Run the "Scripts and Add-Ins" command and click the green plus button near the top of the dialog. Browse to the location where you created the folder and select the folder. The add-in should now be displayed in the list of add-ins on the "Add-Ins" tab of the dialog. Select the add-in and click the "Run" button. This will load the add-in and when any of the application events occurr that it is watching for it will report them in the TEXT COMMAND window. |

## Version

Introduced in version May 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |