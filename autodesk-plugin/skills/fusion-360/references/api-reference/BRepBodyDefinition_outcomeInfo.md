# BRepBodyDefinition.outcomeInfo Property

Parent Object: [BRepBodyDefinition](BRepBodyDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBodyDefinition.h>

## Description

Returns an array of strings that contain information about the outcome of the previous call of the createBody method. This is especially useful when the createBody method fails, (returns null), because it provides information about why the failure occurred. It can also sometimes provide some information even when createBody succeeds.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBodyDefinition\_var" is a variable referencing a BRepBodyDefinition object.  ```` ``` # Get the value of the property. propertyValue = bRepBodyDefinition_var.outcomeInfo ``` ```` |

"bRepBodyDefinition\_var" is a variable referencing a BRepBodyDefinition object. ```` ``` #include <Fusion/BRep/BRepBodyDefinition.h>  // Get the value of the property. std::vector<string> propertyValue = bRepBodyDefinition_var->outcomeInfo(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BRep Body definition Sample](BRepBodyDefinition_Sample.htm) | Demonstrates creating BRep bodies by BRepBodyDefinition. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |