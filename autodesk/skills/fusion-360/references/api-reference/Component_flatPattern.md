# Component.flatPattern Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Gets the existing flat pattern or returns null in the case where a flat pattern doesn't exist in this component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. Ptr<FlatPattern> propertyValue = component_var->flatPattern(); ``` ```` |

## Property Value

This is a read only property whose value is a [FlatPattern](FlatPattern.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |