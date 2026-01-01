# AlongEdgeRipFeatureDefinition.ripEdge Property

Parent Object: [AlongEdgeRipFeatureDefinition](AlongEdgeRipFeatureDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/AlongEdgeRipFeatureDefinition.h>

## Description

Gets and sets the input edge for an along edge rip.

## Syntax

* [Python](#Python)
* [C++](#C++)

"alongEdgeRipFeatureDefinition\_var" is a variable referencing an AlongEdgeRipFeatureDefinition object. |

"alongEdgeRipFeatureDefinition\_var" is a variable referencing an AlongEdgeRipFeatureDefinition object. ```` ``` #include <Fusion/SheetMetal/AlongEdgeRipFeatureDefinition.h>  // Get the value of the property. Ptr<BRepEdge> propertyValue = alongEdgeRipFeatureDefinition_var->ripEdge();  // Set the value of the property, where value_var is a BRepEdge. bool returnValue = alongEdgeRipFeatureDefinition_var->ripEdge(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BRepEdge](BRepEdge.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |