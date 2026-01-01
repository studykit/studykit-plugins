# Occurrence.initialTransform Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Gets and sets the initial position of the occurrence. Setting the initial transform is not valid for all occurrences. For instance, this operation could fail if the occurrence is created by a pattern among other cases. To determine if setting the initial transform is possible, use the isValidForEditInitialPosition property. If this property returns false, attempting to set the initial transform will result in failure.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object. |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = occurrence_var->initialTransform();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = occurrence_var->initialTransform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version November 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |