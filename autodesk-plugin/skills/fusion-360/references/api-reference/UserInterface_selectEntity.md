# UserInterface.selectEntity Method

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

Supports the selection of a single entity. This provides a simple way to prompt the user for for a selection in a script. If you need more control over the selection a command should be created and a SelectionCommandInput used.

## Remarks

The selectEntity method is not supported within any of the Command related events.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterface\_var" is a variable referencing a [UserInterface](UserInterface.htm) object.```` ``` returnValue = userInterface_var.selectEntity(prompt, filter) ``` ```` |

"userInterface\_var" is a variable referencing a [UserInterface](UserInterface.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Selection](Selection.htm) | Returns a Selection object that provides access the selected entity through it's "entity" property along with the location in space where the entity was selected. Asserts if the selection is aborted. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| prompt | string | The prompt displayed to the user during the selection. |
| filter | string | A string defining the types of entities valid for selection. The valid list of selection filters can be found here: [Selection Filters](SelectionFilters_UM.htm). You can combine multiple types by using a comma delimiter. For example, the string "PlanarFaces,ConstructionPlanes" will allow the selection of either a planar face or a construction plane. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |