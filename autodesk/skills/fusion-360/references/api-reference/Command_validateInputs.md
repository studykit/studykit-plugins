# Command.validateInputs Event

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Gets an event that is fired to allow you to check if the current state of the inputs are valid for execution.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* ```` ``` # Import fusion360utils folder, which includes event_utils.py. from ...lib import fusion360utils as futil ``` ```` *-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. local_handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "command_validateInputs" is the event handler function. futil.add_handler(command_var.validateInputs, command_validateInputs, local_handlers=local_handlers) ``` ```` *-------- Event handler function definition ---------* ```` ``` # Event handler for the validateInputs event. def command_validateInputs(args: adsk.core.ValidateInputsEventArgs):     # Code to react to the event.     app.log('In command_validateInputs event handler.') ``` ```` |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "MyValidateInputsHandler" is the name of the class that handles the event. onValidateInputs = MyValidateInputsHandler() command_var.validateInputs.add(onValidateInputs) handlers.append(onValidateInputs) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the validateInputs event. class MyValidateInputsHandler(adsk.core.ValidateInputsEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.ValidateInputsEventArgs):         # Code to react to the event.         app.log('In MyValidateInputsHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/Command.h> #include <Core/UserInterface/ValidateInputsEvent.h> #include <Core/UserInterface/ValidateInputsEventHandler.h> #include <Core/UserInterface/ValidateInputsEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the validateInputs event. ``` ````* class MyValidateInputsEventHandler : public adsk::core::ValidateInputsEventHandler { public:  void notify(const Ptr<ValidateInputsEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyValidateInputsEventHandler event handler.");  } } \_validateInputs;  *--------- Connect the handler to the event. ---------* ```` ``` // "command_var" is a variable referencing a Command object. // Connect the handler function to the event. Ptr<ValidateInputsEvent> validateInputsEvent = command_var->validateInputs(); if (!validateInputsEvent)     return;  bool isOk = validateInputsEvent->add(&_validateInputs); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [ValidateInputsEvent](ValidateInputsEvent.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |