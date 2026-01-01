# OneSideToExtentDefinition.parentFeature Property

Parent Object: [OneSideToExtentDefinition](OneSideToExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OneSideToExtentDefinition.h>

## Description

Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"oneSideToExtentDefinition\_var" is a variable referencing an OneSideToExtentDefinition object. |

"oneSideToExtentDefinition\_var" is a variable referencing an OneSideToExtentDefinition object. ```` ``` #include <Fusion/Features/OneSideToExtentDefinition.h>  // Get the value of the property. Ptr<Feature> propertyValue = oneSideToExtentDefinition_var->parentFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [Feature](Feature.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |