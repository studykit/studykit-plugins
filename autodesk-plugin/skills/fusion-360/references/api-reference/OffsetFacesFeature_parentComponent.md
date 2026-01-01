# OffsetFacesFeature.parentComponent Property

Parent Object: [OffsetFacesFeature](OffsetFacesFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFacesFeature.h>

## Description

Returns the parent component that owns this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFacesFeature\_var" is a variable referencing an OffsetFacesFeature object. |

"offsetFacesFeature\_var" is a variable referencing an OffsetFacesFeature object. ```` ``` #include <Fusion/Features/OffsetFacesFeature.h>  // Get the value of the property. Ptr<Component> propertyValue = offsetFacesFeature_var->parentComponent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |