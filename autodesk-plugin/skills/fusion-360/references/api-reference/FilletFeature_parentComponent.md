# FilletFeature.parentComponent Property

Parent Object: [FilletFeature](FilletFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeature.h>

## Description

Returns the parent component that owns this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeature\_var" is a variable referencing a FilletFeature object. |

"filletFeature\_var" is a variable referencing a FilletFeature object. ```` ``` #include <Fusion/Features/FilletFeature.h>  // Get the value of the property. Ptr<Component> propertyValue = filletFeature_var->parentComponent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |