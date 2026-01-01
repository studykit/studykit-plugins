# BRepLumpDefinition.shellDefinitions Property

Parent Object: [BRepLumpDefinition](BRepLumpDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLumpDefinition.h>

## Description

Provides access to the BRepShellDefinitions object associated with this BRepLumpDefinition. It's through the returned collection that you can create new BRepShellDefinition objects.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLumpDefinition\_var" is a variable referencing a BRepLumpDefinition object. |

"bRepLumpDefinition\_var" is a variable referencing a BRepLumpDefinition object. ```` ``` #include <Fusion/BRep/BRepLumpDefinition.h>  // Get the value of the property. Ptr<BRepShellDefinitions> propertyValue = bRepLumpDefinition_var->shellDefinitions(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepShellDefinitions](BRepShellDefinitions.htm).

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