# OffsetFacesFeature.isSuppressed Property

Parent Object: [OffsetFacesFeature](OffsetFacesFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFacesFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFacesFeature\_var" is a variable referencing an OffsetFacesFeature object. |

"offsetFacesFeature\_var" is a variable referencing an OffsetFacesFeature object. ```` ``` #include <Fusion/Features/OffsetFacesFeature.h>  // Get the value of the property. boolean propertyValue = offsetFacesFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = offsetFacesFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |