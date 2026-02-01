# RibFeature.isSuppressed Property

Parent Object: [RibFeature](RibFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RibFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ribFeature\_var" is a variable referencing a RibFeature object. |

"ribFeature\_var" is a variable referencing a RibFeature object. ```` ``` #include <Fusion/Features/RibFeature.h>  // Get the value of the property. boolean propertyValue = ribFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = ribFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |