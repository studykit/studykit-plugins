# AlongPathTextDefinition.path Property

Parent Object: [AlongPathTextDefinition](AlongPathTextDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/AlongPathTextDefinition.h>

## Description

Get and sets the entity that defines the path for the text. This can be a SketchCurve or BRepEdge object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"alongPathTextDefinition\_var" is a variable referencing an AlongPathTextDefinition object. |

"alongPathTextDefinition\_var" is a variable referencing an AlongPathTextDefinition object. ```` ``` #include <Fusion/Sketch/AlongPathTextDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = alongPathTextDefinition_var->path();  // Set the value of the property, where value_var is a Base. bool returnValue = alongPathTextDefinition_var->path(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |