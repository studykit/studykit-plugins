# RevolveFeature.parentComponent Property

Parent Object: [RevolveFeature](RevolveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeature.h>

## Description

Returns the parent component that owns this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeature\_var" is a variable referencing a RevolveFeature object. |

"revolveFeature\_var" is a variable referencing a RevolveFeature object. ```` ``` #include <Fusion/Features/RevolveFeature.h>  // Get the value of the property. Ptr<Component> propertyValue = revolveFeature_var->parentComponent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |