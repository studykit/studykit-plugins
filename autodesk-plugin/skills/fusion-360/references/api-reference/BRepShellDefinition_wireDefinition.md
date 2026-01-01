# BRepShellDefinition.wireDefinition Property

Parent Object: [BRepShellDefinition](BRepShellDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShellDefinition.h>

## Description

Returns the single BRepWireDefinition associated with this shell definition.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepShellDefinition\_var" is a variable referencing a BRepShellDefinition object. |

"bRepShellDefinition\_var" is a variable referencing a BRepShellDefinition object. ```` ``` #include <Fusion/BRep/BRepShellDefinition.h>  // Get the value of the property. Ptr<BRepWireDefinition> propertyValue = bRepShellDefinition_var->wireDefinition(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepWireDefinition](BRepWireDefinition.htm).

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