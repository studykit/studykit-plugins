# BRepBodyDefinition.lumpDefinitions Property

Parent Object: [BRepBodyDefinition](BRepBodyDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBodyDefinition.h>

## Description

Provides access to the BRepLumpDefinitions object associated with this BRepBodyDefinition. It's through the returned collection that you can create new BRepLumpDefinition objects.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBodyDefinition\_var" is a variable referencing a BRepBodyDefinition object. |

"bRepBodyDefinition\_var" is a variable referencing a BRepBodyDefinition object. ```` ``` #include <Fusion/BRep/BRepBodyDefinition.h>  // Get the value of the property. Ptr<BRepLumpDefinitions> propertyValue = bRepBodyDefinition_var->lumpDefinitions(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepLumpDefinitions](BRepLumpDefinitions.htm).

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