# BRepLoopDefinition.bRepCoEdgeDefinitions Property

Parent Object: [BRepLoopDefinition](BRepLoopDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoopDefinition.h>

## Description

Provides access to the BRepCoEdgeDefinitions object associated with the parent BRepFaceDefinition object. It's through the returned collection that you can create new BRepCoEdgeDefinition objects.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLoopDefinition\_var" is a variable referencing a BRepLoopDefinition object. |

"bRepLoopDefinition\_var" is a variable referencing a BRepLoopDefinition object. ```` ``` #include <Fusion/BRep/BRepLoopDefinition.h>  // Get the value of the property. Ptr<BRepCoEdgeDefinitions> propertyValue = bRepLoopDefinition_var->bRepCoEdgeDefinitions(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepCoEdgeDefinitions](BRepCoEdgeDefinitions.htm).

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