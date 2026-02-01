# SymmetricExtentDefinition.parentFeature Property

Parent Object: [SymmetricExtentDefinition](SymmetricExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SymmetricExtentDefinition.h>

## Description

Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"symmetricExtentDefinition\_var" is a variable referencing a SymmetricExtentDefinition object. |

"symmetricExtentDefinition\_var" is a variable referencing a SymmetricExtentDefinition object. ```` ``` #include <Fusion/Features/SymmetricExtentDefinition.h>  // Get the value of the property. Ptr<Feature> propertyValue = symmetricExtentDefinition_var->parentFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [Feature](Feature.htm).

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |