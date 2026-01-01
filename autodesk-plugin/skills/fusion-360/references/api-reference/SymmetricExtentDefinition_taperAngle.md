# SymmetricExtentDefinition.taperAngle Property

Parent Object: [SymmetricExtentDefinition](SymmetricExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SymmetricExtentDefinition.h>

## Description

Returns the current taper angle. If the SymmetricExtentDefinition object has been created statically and isn't associated with a feature this will return a ValueInput object. If the SymmetricExtentDefinition object is obtained from a feature this will return a ModelParameter object. You can use properties of the parameter to edit its value which will result in the feature updating.

## Syntax

* [Python](#Python)
* [C++](#C++)

"symmetricExtentDefinition\_var" is a variable referencing a SymmetricExtentDefinition object. |

"symmetricExtentDefinition\_var" is a variable referencing a SymmetricExtentDefinition object. ```` ``` #include <Fusion/Features/SymmetricExtentDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = symmetricExtentDefinition_var->taperAngle(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |