# BaseComponent.propertyGroups Property

Parent Object: [BaseComponent](BaseComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/BaseComponent.h>

## Description

Returns the PropertyGroups object associated with this component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseComponent\_var" is a variable referencing a BaseComponent object. |

"baseComponent\_var" is a variable referencing a BaseComponent object. ```` ``` #include <Fusion/Components/BaseComponent.h>  // Get the value of the property. Ptr<PropertyGroups> propertyValue = baseComponent_var->propertyGroups(); ``` ```` |

## Property Value

This is a read only property whose value is a [PropertyGroups](PropertyGroups.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |