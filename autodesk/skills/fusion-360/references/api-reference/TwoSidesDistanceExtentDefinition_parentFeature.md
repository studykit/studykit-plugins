# TwoSidesDistanceExtentDefinition.parentFeature Property

Parent Object: [TwoSidesDistanceExtentDefinition](TwoSidesDistanceExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TwoSidesDistanceExtentDefinition.h>

## Description

Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"twoSidesDistanceExtentDefinition\_var" is a variable referencing a TwoSidesDistanceExtentDefinition object. |

"twoSidesDistanceExtentDefinition\_var" is a variable referencing a TwoSidesDistanceExtentDefinition object. ```` ``` #include <Fusion/Features/TwoSidesDistanceExtentDefinition.h>  // Get the value of the property. Ptr<Feature> propertyValue = twoSidesDistanceExtentDefinition_var->parentFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [Feature](Feature.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |