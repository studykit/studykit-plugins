# FormFeature.parentComponent Property

Parent Object: [FormFeature](FormFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FormFeature.h>

## Description

Returns the parent component that owns this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"formFeature\_var" is a variable referencing a FormFeature object. |

"formFeature\_var" is a variable referencing a FormFeature object. ```` ``` #include <Fusion/Features/FormFeature.h>  // Get the value of the property. Ptr<Component> propertyValue = formFeature_var->parentComponent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |