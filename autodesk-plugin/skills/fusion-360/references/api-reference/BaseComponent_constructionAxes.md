# BaseComponent.constructionAxes Property

Parent Object: [BaseComponent](BaseComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/BaseComponent.h>

## Description

Returns the construction axes collection associated with this component. This provides access to the existing construction axes and supports the creation of new construction axes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseComponent\_var" is a variable referencing a BaseComponent object. |

"baseComponent\_var" is a variable referencing a BaseComponent object. ```` ``` #include <Fusion/Components/BaseComponent.h>  // Get the value of the property. Ptr<ConstructionAxes> propertyValue = baseComponent_var->constructionAxes(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConstructionAxes](ConstructionAxes.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |