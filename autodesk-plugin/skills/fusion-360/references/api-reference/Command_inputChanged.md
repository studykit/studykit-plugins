# Command.inputChanged Event

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Gets an event that is fired whenever an input value is changed.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "MyInputChangedHandler" is the name of the class that handles the event. onInputChanged = MyInputChangedHandler() command_var.inputChanged.add(onInputChanged) handlers.append(onInputChanged) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the inputChanged event. class MyInputChangedHandler(adsk.core.InputChangedEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.InputChangedEventArgs):         # Code to react to the event.         app.log('In MyInputChangedHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/Command.h> #include <Core/UserInterface/InputChangedEvent.h> #include <Core/UserInterface/InputChangedEventHandler.h> #include <Core/UserInterface/InputChangedEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the inputChanged event. ``` ````* class MyInputChangedEventHandler : public adsk::core::InputChangedEventHandler { public:  void notify(const Ptr<InputChangedEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyInputChangedEventHandler event handler.");  } } \_inputChanged;  *--------- Connect the handler to the event. ---------* ```` ``` // "command_var" is a variable referencing a Command object. // Connect the handler function to the event. Ptr<InputChangedEvent> inputChangedEvent = command_var->inputChanged(); if (!inputChangedEvent)     return;  bool isOk = inputChangedEvent->add(&_inputChanged); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns an [InputChangedEvent](InputChangedEvent.htm).

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [InputChangedEvent](InputChangedEvent.htm) | Returns an InputChangedEvent object that is used to connect and release from the event. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Command Inputs API Sample](CommandInputsSample_Sample.htm) | Creates a command dialog that demonstrates all of the available command inputs.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |