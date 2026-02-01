# Component.constructionAxes Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Returns the construction axes collection associated with this component. This provides access to the existing construction axes and supports the creation of new construction axes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. Ptr<ConstructionAxes> propertyValue = component_var->constructionAxes(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConstructionAxes](ConstructionAxes.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |