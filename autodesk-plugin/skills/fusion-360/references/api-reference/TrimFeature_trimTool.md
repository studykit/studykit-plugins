# TrimFeature.trimTool Property

Parent Object: [TrimFeature](TrimFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeature.h>

## Description

Gets and sets the entity (a patch body, B-Rep face, construction plane or sketch curve) that intersects the trim tool.

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeature\_var" is a variable referencing a TrimFeature object.  ```` ``` # Get the value of the property. propertyValue = trimFeature_var.trimTool  # Set the value of the property. trimFeature_var.trimTool = propertyValue ``` ```` |

"trimFeature\_var" is a variable referencing a TrimFeature object. ```` ``` #include <Fusion/Features/TrimFeature.h>  // Get the value of the property. Ptr<Base> propertyValue = trimFeature_var->trimTool();  // Set the value of the property, where value_var is a Base. bool returnValue = trimFeature_var->trimTool(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |