# Application.mfgdmDataReady Event

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

The mfgdmDataReady event fires when the MFGDM data structure for a document has been updated and properties to IDs and structure from the data model is ready.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "application_var" is a variable referencing an Application object. # "MyMfgdmDataReadyHandler" is the name of the class that handles the event. onMfgdmDataReady = MyMfgdmDataReadyHandler() application_var.mfgdmDataReady.add(onMfgdmDataReady) handlers.append(onMfgdmDataReady) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the mfgdmDataReady event. class MyMfgdmDataReadyHandler(adsk.core.MFGDMDataEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.MFGDMDataEventArgs):         # Code to react to the event.         app.log('In MyMfgdmDataReadyHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/Application/Application.h> #include <Core/Application/MFGDMDataEvent.h> #include <Core/Application/MFGDMDataEventHandler.h> #include <Core/Application/MFGDMDataEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the mfgdmDataReady event. ``` ````* class MyMfgdmDataReadyEventHandler : public adsk::core::MFGDMDataEventHandler { public:  void notify(const Ptr<MFGDMDataEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyMfgdmDataReadyEventHandler event handler.");  } } \_mfgdmDataReady;  *--------- Connect the handler to the event. ---------* ```` ``` // "application_var" is a variable referencing an Application object. // Connect the handler function to the event. Ptr<MFGDMDataEvent> mfgdmDataReadyEvent = application_var->mfgdmDataReady(); if (!mfgdmDataReadyEvent)     return;  bool isOk = mfgdmDataReadyEvent->add(&_mfgdmDataReady); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [MFGDMDataEvent](MFGDMDataEvent.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Gets all properties using GraphQL](FetchBulkComponentProperties_Sample.htm) | Fetches bulk component properties of the root component and from occurrences via single GraphQL query. |
| [Get part number using GraphQL](FetchPartNumberForComponents_Sample.htm) | Fetches part number of root component and from occurrences via GQL query. |
| [Set part number using GraphQL](SetPartNumberUsingGraphQL_Sample.htm) | Sets part number of root component and from occurrences via GQL query. |

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |