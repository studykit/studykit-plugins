# UnfoldFeature.isSuppressed Property

Parent Object: [UnfoldFeature](UnfoldFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/UnfoldFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unfoldFeature\_var" is a variable referencing a UnfoldFeature object. |

"unfoldFeature\_var" is a variable referencing a UnfoldFeature object. ```` ``` #include <Fusion/SheetMetal/UnfoldFeature.h>  // Get the value of the property. boolean propertyValue = unfoldFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = unfoldFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |