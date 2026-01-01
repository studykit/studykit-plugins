# Design.namedViews Property

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Returns the NamedViews object associated with this product. The NamedViews collection provides access to the named views defined in this product and supports the creation of new named views.

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a Design object. |

"design\_var" is a variable referencing a Design object. ```` ``` #include <Fusion/Fusion/Design.h>  // Get the value of the property. Ptr<NamedViews> propertyValue = design_var->namedViews(); ``` ```` |

## Property Value

This is a read only property whose value is a [NamedViews](NamedViews.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |