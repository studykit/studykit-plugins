# AngleExtentDefinition.parentFeature Property

Parent Object: [AngleExtentDefinition](AngleExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/AngleExtentDefinition.h>

## Description

Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"angleExtentDefinition\_var" is a variable referencing an AngleExtentDefinition object. |

"angleExtentDefinition\_var" is a variable referencing an AngleExtentDefinition object. ```` ``` #include <Fusion/Features/AngleExtentDefinition.h>  // Get the value of the property. Ptr<Feature> propertyValue = angleExtentDefinition_var->parentFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [Feature](Feature.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |