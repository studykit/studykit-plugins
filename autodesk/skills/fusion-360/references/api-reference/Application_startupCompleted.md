# Application.startupCompleted Event

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

The startupCompleted event fires after Fusion has completed its initialization. This includes initialization of all the Add-ins loaded at startup. The client can add or remove ApplicationEventHandlers from the ApplicationEvent.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "application_var" is a variable referencing an Application object. # "MyStartupCompletedHandler" is the name of the class that handles the event. onStartupCompleted = MyStartupCompletedHandler() application_var.startupCompleted.add(onStartupCompleted) handlers.append(onStartupCompleted) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the startupCompleted event. class MyStartupCompletedHandler(adsk.core.ApplicationEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.ApplicationEventArgs):         # Code to react to the event.         app.log('In MyStartupCompletedHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/Application/Application.h> #include <Core/Application/ApplicationEvent.h> #include <Core/Application/ApplicationEventHandler.h> #include <Core/Application/ApplicationEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the startupCompleted event. ``` ````* class MyStartupCompletedEventHandler : public adsk::core::ApplicationEventHandler { public:  void notify(const Ptr<ApplicationEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyStartupCompletedEventHandler event handler.");  } } \_startupCompleted;  *--------- Connect the handler to the event. ---------* ```` ``` // "application_var" is a variable referencing an Application object. // Connect the handler function to the event. Ptr<ApplicationEvent> startupCompletedEvent = application_var->startupCompleted(); if (!startupCompletedEvent)     return;  bool isOk = startupCompletedEvent->add(&_startupCompleted); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns an [ApplicationEvent](ApplicationEvent.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Application Event API Sample](ApplicationEventSample_Sample.htm) | Add-In that demonstrates application events. To use this sample, create a new folder using the name you want to use for the new add-in. Inside the folder, create a new file that is the same name as the folder but has a .py extension. Copy the code below into the .py file. Create another file that is the same name as the folder but has a .manifest extension and copy the JSON data below into that file. { "autodeskProduct": "Fusion360", "type": "addin", "author": "", "description": { "": "" }, "supportedOS": "windows|mac", "editEnabled": true } Run the "Scripts and Add-Ins" command and click the green plus button near the top of the dialog. Browse to the location where you created the folder and select the folder. The add-in should now be displayed in the list of add-ins on the "Add-Ins" tab of the dialog. Select the add-in and click the "Run" button. This will load the add-in and when any of the application events occurr that it is watching for it will report them in the TEXT COMMAND window. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |