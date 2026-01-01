# SelectionCommandInput.addSelection Method

Parent Object: [SelectionCommandInput](SelectionCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionCommandInput.h>

## Description

Adds the selection to the list of selections associated with this input. This method is not valid within the commandCreated event but must be used later in the command lifetime. If you want to pre-populate the selection when the command is starting, you can use this method in the activate method of the Command. It's also valid to use in other events once the command is running, such as the validateInputs event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionCommandInput\_var" is a variable referencing a [SelectionCommandInput](SelectionCommandInput.htm) object.```` ``` returnValue = selectionCommandInput_var.addSelection(selection) ``` ```` |

"selectionCommandInput\_var" is a variable referencing a [SelectionCommandInput](SelectionCommandInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if a selection to the entity was added to this input. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selection | [Base](Base.htm) | The entity to add a selection of to this input. The addition may fail if the entity does not match the selection filter, or adding it would exceed the limits. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |