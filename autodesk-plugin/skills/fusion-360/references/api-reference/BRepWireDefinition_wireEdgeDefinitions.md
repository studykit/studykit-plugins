# BRepWireDefinition.wireEdgeDefinitions Property

Parent Object: [BRepWireDefinition](BRepWireDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWireDefinition.h>

## Description

Provides access to the BRepWireEdgeDefinitions object associated with the parent BRepWireDefinition object. It's through the returned collection that you can create new BRepWireEdgeDefinitions objects.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWireDefinition\_var" is a variable referencing a BRepWireDefinition object. |

"bRepWireDefinition\_var" is a variable referencing a BRepWireDefinition object. ```` ``` #include <Fusion/BRep/BRepWireDefinition.h>  // Get the value of the property. Ptr<BRepWireEdgeDefinitions> propertyValue = bRepWireDefinition_var->wireEdgeDefinitions(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepWireEdgeDefinitions](BRepWireEdgeDefinitions.htm).

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