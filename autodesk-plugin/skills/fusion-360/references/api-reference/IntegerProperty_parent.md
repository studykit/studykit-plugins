# IntegerProperty.parent Property

Parent Object: [IntegerProperty](IntegerProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/IntegerProperty.h>

## Description

Returns the parent of this property.For properties associated with an appearance this will return the parent Appearance. For properties associated with a material, this will return the parent Material. For other types of properties, this will return the PropertyGroup it is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerProperty\_var" is a variable referencing an IntegerProperty object. |

"integerProperty\_var" is a variable referencing an IntegerProperty object. ```` ``` #include <Core/Application/IntegerProperty.h>  // Get the value of the property. Ptr<Base> propertyValue = integerProperty_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |