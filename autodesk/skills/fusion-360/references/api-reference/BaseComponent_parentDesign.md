# BaseComponent.parentDesign Property

Parent Object: [BaseComponent](BaseComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/BaseComponent.h>

## Description

Returns the parent product this component is owned by.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseComponent\_var" is a variable referencing a BaseComponent object. |

"baseComponent\_var" is a variable referencing a BaseComponent object. ```` ``` #include <Fusion/Components/BaseComponent.h>  // Get the value of the property. Ptr<Design> propertyValue = baseComponent_var->parentDesign(); ``` ```` |

## Property Value

This is a read only property whose value is a [Design](Design.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |