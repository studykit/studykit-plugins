# SphereFeature.isSuppressed Property

Parent Object: [SphereFeature](SphereFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SphereFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sphereFeature\_var" is a variable referencing a SphereFeature object. |

"sphereFeature\_var" is a variable referencing a SphereFeature object. ```` ``` #include <Fusion/Features/SphereFeature.h>  // Get the value of the property. boolean propertyValue = sphereFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = sphereFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |