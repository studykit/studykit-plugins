# DistanceExtentDefinition.parentFeature Property

Parent Object: [DistanceExtentDefinition](DistanceExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DistanceExtentDefinition.h>

## Description

Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"distanceExtentDefinition\_var" is a variable referencing a DistanceExtentDefinition object. |

"distanceExtentDefinition\_var" is a variable referencing a DistanceExtentDefinition object. ```` ``` #include <Fusion/Features/DistanceExtentDefinition.h>  // Get the value of the property. Ptr<Feature> propertyValue = distanceExtentDefinition_var->parentFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [Feature](Feature.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |