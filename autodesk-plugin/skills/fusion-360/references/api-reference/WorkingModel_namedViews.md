# WorkingModel.namedViews Property

Parent Object: [WorkingModel](WorkingModel.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/WorkingModel.h>

## Description

Returns the NamedViews object associated with this product. The NamedViews collection provides access to the named views defined in this product and supports the creation of new named views.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workingModel\_var" is a variable referencing a WorkingModel object. |

"workingModel\_var" is a variable referencing a WorkingModel object. ```` ``` #include <Fusion/Fusion/WorkingModel.h>  // Get the value of the property. Ptr<NamedViews> propertyValue = workingModel_var->namedViews(); ``` ```` |

## Property Value

This is a read only property whose value is a [NamedViews](NamedViews.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |