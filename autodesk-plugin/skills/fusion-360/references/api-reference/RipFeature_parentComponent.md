# RipFeature.parentComponent Property

Parent Object: [RipFeature](RipFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeature.h>

## Description

Returns the parent component that owns this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeature\_var" is a variable referencing a RipFeature object. |

"ripFeature\_var" is a variable referencing a RipFeature object. ```` ``` #include <Fusion/SheetMetal/RipFeature.h>  // Get the value of the property. Ptr<Component> propertyValue = ripFeature_var->parentComponent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |