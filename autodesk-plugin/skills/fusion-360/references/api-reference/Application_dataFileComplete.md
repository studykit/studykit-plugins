# Application.dataFileComplete Event

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

The dataFileComplete event fires when a data file upload has completed including any cloud side translations.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "application_var" is a variable referencing an Application object. # "MyDataFileCompleteHandler" is the name of the class that handles the event. onDataFileComplete = MyDataFileCompleteHandler() application_var.dataFileComplete.add(onDataFileComplete) handlers.append(onDataFileComplete) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the dataFileComplete event. class MyDataFileCompleteHandler(adsk.core.DataEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.DataEventArgs):         # Code to react to the event.         app.log('In MyDataFileCompleteHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/Application/Application.h> #include <Core/Dashboard/DataEvent.h> #include <Core/Dashboard/DataEventHandler.h> #include <Core/Dashboard/DataEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the dataFileComplete event. ``` ````* class MyDataFileCompleteEventHandler : public adsk::core::DataEventHandler { public:  void notify(const Ptr<DataEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyDataFileCompleteEventHandler event handler.");  } } \_dataFileComplete;  *--------- Connect the handler to the event. ---------* ```` ``` // "application_var" is a variable referencing an Application object. // Connect the handler function to the event. Ptr<DataEvent> dataFileCompleteEvent = application_var->dataFileComplete(); if (!dataFileCompleteEvent)     return;  bool isOk = dataFileCompleteEvent->add(&_dataFileComplete); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [DataEvent](DataEvent.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Save and Insert File API Sample](SaveAndInsertSample_Sample.htm) | Demonstrates creating save a new file and then inserting it into a design. To use this sample, have a design open that has been saved and run the script. It will create a new design that contains a cylinder, save it to the same folder the active design was saved to, and then insert it into the active design. |

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |