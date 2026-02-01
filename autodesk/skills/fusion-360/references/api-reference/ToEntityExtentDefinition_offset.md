# ToEntityExtentDefinition.offset Property

Parent Object: [ToEntityExtentDefinition](ToEntityExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ToEntityExtentDefinition.h>

## Description

Returns the current offset. If the EntityExtentDefinition object has been created statically and isn't associated with a feature this will return a ValueInput object. If the EntityExtentDefinition object is obtained from a feature this will return a ModelParameter object. You can use properties of the parameter to edit its value which will result in the feature updating.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toEntityExtentDefinition\_var" is a variable referencing a ToEntityExtentDefinition object. |

"toEntityExtentDefinition\_var" is a variable referencing a ToEntityExtentDefinition object. ```` ``` #include <Fusion/Features/ToEntityExtentDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = toEntityExtentDefinition_var->offset(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |