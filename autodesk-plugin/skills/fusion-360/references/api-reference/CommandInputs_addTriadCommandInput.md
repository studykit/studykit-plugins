# CommandInputs.addTriadCommandInput Method

Parent Object: [CommandInputs](CommandInputs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandInputs.h>

## Description

Adds a new triad command input to the command. The input is initially invisible to allow you to define the desired behavior and then set the isVisible property to true when you're ready to display the triad.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandInputs\_var" is a variable referencing a [CommandInputs](CommandInputs.htm) object.```` ``` returnValue = commandInputs_var.addTriadCommandInput(id, transform) ``` ```` |

"commandInputs\_var" is a variable referencing a [CommandInputs](CommandInputs.htm) object.  ```` ``` #include <Core/UserInterface/CommandInputs.h>  returnValue = commandInputs_var->addTriadCommandInput(id, transform); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TriadCommandInput](TriadCommandInput.htm) | Returns the created TriadCommandInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The unique ID of this command input. It must be unique with respect to the other inputs associated with this command. |
| transform | [Matrix3D](Matrix3D.htm) | Defines the initial position and orientation of the manipulator. |

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |