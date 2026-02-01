# Application.dataFileCopyComplete Event

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

The dataFileCopyComplete event fires when a data file copy has completed including any PIM Data copy.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "application_var" is a variable referencing an Application object. # "MyDataFileCopyCompleteHandler" is the name of the class that handles the event. onDataFileCopyComplete = MyDataFileCopyCompleteHandler() application_var.dataFileCopyComplete.add(onDataFileCopyComplete) handlers.append(onDataFileCopyComplete) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the dataFileCopyComplete event. class MyDataFileCopyCompleteHandler(adsk.core.DataEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.DataEventArgs):         # Code to react to the event.         app.log('In MyDataFileCopyCompleteHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/Application/Application.h> #include <Core/Dashboard/DataEvent.h> #include <Core/Dashboard/DataEventHandler.h> #include <Core/Dashboard/DataEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the dataFileCopyComplete event. ``` ````* class MyDataFileCopyCompleteEventHandler : public adsk::core::DataEventHandler { public:  void notify(const Ptr<DataEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyDataFileCopyCompleteEventHandler event handler.");  } } \_dataFileCopyComplete;  *--------- Connect the handler to the event. ---------* ```` ``` // "application_var" is a variable referencing an Application object. // Connect the handler function to the event. Ptr<DataEvent> dataFileCopyCompleteEvent = application_var->dataFileCopyComplete(); if (!dataFileCopyCompleteEvent)     return;  bool isOk = dataFileCopyCompleteEvent->add(&_dataFileCopyComplete); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [DataEvent](DataEvent.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |