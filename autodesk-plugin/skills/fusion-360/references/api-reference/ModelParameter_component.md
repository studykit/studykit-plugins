# ModelParameter.component Property

Parent Object: [ModelParameter](ModelParameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ModelParameter.h>

## Description

Returns the Component containing the ModelParameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"modelParameter\_var" is a variable referencing a ModelParameter object. |

"modelParameter\_var" is a variable referencing a ModelParameter object. ```` ``` #include <Fusion/Fusion/ModelParameter.h>  // Get the value of the property. Ptr<Component> propertyValue = modelParameter_var->component(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |