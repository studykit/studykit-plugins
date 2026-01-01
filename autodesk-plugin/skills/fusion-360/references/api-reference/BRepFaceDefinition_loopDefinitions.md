# BRepFaceDefinition.loopDefinitions Property

Parent Object: [BRepFaceDefinition](BRepFaceDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFaceDefinition.h>

## Description

Provides access to the BRepLoopDefinitions object associated with this BRepFaceDefinition. It's through the returned collection that you can create new BRepLoopDefinition objects.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFaceDefinition\_var" is a variable referencing a BRepFaceDefinition object. |

"bRepFaceDefinition\_var" is a variable referencing a BRepFaceDefinition object. ```` ``` #include <Fusion/BRep/BRepFaceDefinition.h>  // Get the value of the property. Ptr<BRepLoopDefinitions> propertyValue = bRepFaceDefinition_var->loopDefinitions(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepLoopDefinitions](BRepLoopDefinitions.htm).

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