# BaseComponent.constructionPoints Property

Parent Object: [BaseComponent](BaseComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/BaseComponent.h>

## Description

Returns the construction points collection associated with this component. This provides access to the existing construction points and supports the creation of new construction points.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseComponent\_var" is a variable referencing a BaseComponent object. |

"baseComponent\_var" is a variable referencing a BaseComponent object. ```` ``` #include <Fusion/Components/BaseComponent.h>  // Get the value of the property. Ptr<ConstructionPoints> propertyValue = baseComponent_var->constructionPoints(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConstructionPoints](ConstructionPoints.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |